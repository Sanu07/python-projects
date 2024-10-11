from flask import Flask, request, jsonify
from transformers import AutoModelForSequenceClassification, DistilBertTokenizer
import torch

app = Flask(__name__)

# Load model and tokenizer during startup
model_dir_tech = "tech-classification-V1"
model_dir_difficulty = "difficulty-classification-V1"

model_tech = None
model_difficulty = None
tokenizer_tech = None
tokenizer_difficulty = None
first_request_done = False

def load_model():
    global model_tech, model_difficulty, tokenizer_tech, tokenizer_difficulty
    tokenizer_tech = DistilBertTokenizer.from_pretrained(model_dir_tech)
    model_tech = AutoModelForSequenceClassification.from_pretrained(model_dir_tech)
    model_tech.eval()  # Set technology model to evaluation mode

    tokenizer_difficulty = DistilBertTokenizer.from_pretrained(model_dir_difficulty)
    model_difficulty = AutoModelForSequenceClassification.from_pretrained(model_dir_difficulty)
    model_difficulty.eval()  # Set difficulty model to evaluation mode

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

    for item in data:
        question_id = item.get('id')
        question = item.get('question')

        if not question:
            return jsonify({"error": f"Missing question in item {item}"}), 400

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

    # Return the predictions wrapped in a single JSON response
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
