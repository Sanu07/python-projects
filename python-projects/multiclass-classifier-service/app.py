from flask import Flask, request, jsonify
from transformers import AutoModelForSequenceClassification, DistilBertTokenizer
import torch
from text_extractor import TextExtractor  # Import the TextExtractor class
import os
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load model and tokenizer during startup
model_dir_tech = "tech-classification-V1"
model_dir_difficulty = "difficulty-classification-V1"

model_tech = None
model_difficulty = None
tokenizer_tech = None
tokenizer_difficulty = None
first_request_done = False

# Load trained questions from PKL file
trained_questions = []
similarity_model = None
precomputed_trained_embeddings = None  # Global variable for precomputed embeddings

def load_model():
    global model_tech, model_difficulty, tokenizer_tech, tokenizer_difficulty, trained_questions, similarity_model, precomputed_trained_embeddings, filtered_questions
    tokenizer_tech = DistilBertTokenizer.from_pretrained(model_dir_tech)
    model_tech = AutoModelForSequenceClassification.from_pretrained(model_dir_tech)
    model_tech.eval()  # Set technology model to evaluation mode

    tokenizer_difficulty = DistilBertTokenizer.from_pretrained(model_dir_difficulty)
    model_difficulty = AutoModelForSequenceClassification.from_pretrained(model_dir_difficulty)
    model_difficulty.eval()  # Set difficulty model to evaluation mode
    
    # Load trained questions from PKL
    with open('./pkl/questions_df2.pkl', 'rb') as f:  # Adjust path to your PKL file
        trained_questions = pickle.load(f)
        
    filtered_questions = [q for q in trained_questions.values.flatten().tolist() if not isinstance(q, (int, float))]
    

    # Load the saved SentenceTransformer model
    similarity_model = SentenceTransformer("./pkl/sentence_similarity_detector_model") 

    # Precompute the embeddings for the trained questions
    precomputed_trained_embeddings = similarity_model.encode(filtered_questions)

@app.before_request
def before_any_request():
    global first_request_done
    if not first_request_done:
        load_model()
        first_request_done = True

# POST endpoint to receive questions and predict technology and difficulty
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Expecting a list of {id: <str>, question: <str>} objects

    if not data:
        return jsonify({"error": "Invalid input, expecting a list of questions"}), 400

    predictions = []
    new_questions = []

    for item in data:
        question_id = item.get('id')
        question = item.get('question')

        if not question:
            return jsonify({"error": f"Missing question in item {item}"}), 400
        
        new_questions.append(question)

        # Tokenize the input question for technology model
        inputs_tech = tokenizer_tech(question, return_tensors="pt", padding=True, truncation=True, max_length=512)
        inputs_difficulty = tokenizer_difficulty(question, return_tensors="pt", padding=True, truncation=True, max_length=512)

        # Get predictions from the technology model
        with torch.no_grad():
            outputs_tech = model_tech(**inputs_tech)
            logits_tech = outputs_tech.logits
            probabilities_tech = torch.softmax(logits_tech, dim=1)
            confidence_score_tech, predicted_class_id_tech = torch.max(probabilities_tech, dim=1)

            predicted_class_id_tech = predicted_class_id_tech.item()
            confidence_score_tech = confidence_score_tech.item()

        # Define the label map for technology
        label_map_tech = {0: 'database', 1: 'devops', 2: 'java', 3: 'microservice', 4: 'springboot'}
        predicted_label_tech = label_map_tech.get(predicted_class_id_tech, "Unknown")

        # Get predictions from the difficulty model
        with torch.no_grad():
            outputs_difficulty = model_difficulty(**inputs_difficulty)
            logits_difficulty = outputs_difficulty.logits
            probabilities_difficulty = torch.softmax(logits_difficulty, dim=1)
            confidence_score_difficulty, predicted_class_id_difficulty = torch.max(probabilities_difficulty, dim=1)

            predicted_class_id_difficulty = predicted_class_id_difficulty.item()
            confidence_score_difficulty = confidence_score_difficulty.item()

        # Define the label map for difficulty (adjust according to your difficulty classes)
        label_map_difficulty = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
        predicted_label_difficulty = label_map_difficulty.get(predicted_class_id_difficulty, "Unknown")

        # Append the prediction result with confidence score
        predictions.append({
            "id": question_id,
            "technology": {
                "label": predicted_label_tech,
                "confidence": f"{confidence_score_tech:.3f}"  # Format confidence to 3 significant digits
            },
            "difficulty": {
                "label": predicted_label_difficulty,
                "confidence": f"{confidence_score_difficulty:.3f}"  # Format confidence to 3 significant digits
            }
        })
        
    # Get suggested questions based on the new questions
    suggested_questions = get_similarity(new_questions)

    # Add suggested questions to the predictions
    for i in range(len(predictions)):
        predictions[i]["suggestedQuestions"] = [
        suggested_questions[i * 2],     # First suggestion
        suggested_questions[i * 2 + 1]  # Second suggestion
    ]

    # Return the predictions wrapped in a single JSON response
    return jsonify(predictions)

@app.route('/extract_text', methods=['POST'])
def extract_text():
    if 'docFile' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    doc_file = request.files['docFile']
    file_path = os.path.join('uploads', doc_file.filename)  # Ensure you have an uploads directory

    # Save the uploaded file
    doc_file.save(file_path)

    # Extract text using the TextExtractor class
    transcript_text = TextExtractor.read_docx_without_images(file_path)
    transcript_date = TextExtractor.extract_transcript_date(transcript_text)
    df_conversations = TextExtractor.extract_conversations(transcript_text)

    # Optionally, convert DataFrame to JSON
    conversations_json = df_conversations.to_json(orient='records')

    return jsonify({
        "transcript_date": transcript_date,
        "conversations": conversations_json
    })
    
# Function to compute similarities and get suggested questions
def get_similarity(new_questions):
    global precomputed_trained_embeddings  # Use the precomputed embeddings

    embeddings2 = similarity_model.encode(new_questions)  # Compute embeddings for the new questions

    # Compute similarity between new questions and trained questions
    similarities = np.dot(embeddings2, precomputed_trained_embeddings.T)

    suggested_questions = []
        
    for idx2, sentence2 in enumerate(new_questions):
        top_indices = np.argsort(similarities[idx2])[::-1][:2]
        for idx in top_indices:
            suggested_questions.append(filtered_questions[idx])

    return suggested_questions


if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
