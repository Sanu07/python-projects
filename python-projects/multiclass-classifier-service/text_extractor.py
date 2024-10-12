# text_extractor.py

import docx
import re
import pandas as pd
from textblob import TextBlob

class TextExtractor:
    @staticmethod
    def read_docx_without_images(file_path):
        doc = docx.Document(file_path)
        full_text = []
        
        for para in doc.paragraphs:
            new_paragraph = []
            for run in para.runs:
                if not run.element.xpath('.//w:drawing') and not run.element.xpath('.//w:pict'):
                    new_paragraph.append(run.text)
            full_text.append(''.join(new_paragraph))
        
        return '\n'.join(full_text)

    @staticmethod
    def extract_transcript_date(text):
        date_pattern = r'Transcript\s*\n([A-Za-z]+\s+\d{1,2},\s+\d{4},\s+\d{1,2}:\d{2}[APM]+)'
        match = re.search(date_pattern, text)
        if match:
            return match.group(1)
        return None

    @staticmethod
    def sanitize_speaker(speaker):
        speaker = speaker.replace('\n', ' ').strip()
        speaker = re.sub(r'\b(?:AM|PM)\b', '', speaker).strip()
        return speaker

    @staticmethod
    def extract_conversations(text):
        lines = text.strip().split('\n', 2)[2]
        lines = '\n'.join(lines.splitlines()[:-1])
        
        pattern = r'([A-Za-z\s]+[A-Za-z])\s+(\d+:\d+)\s*\n([^\n]+(?:\n(?![A-Za-z\s]+\s+\d+:\d+).*)*)'
        matches = re.findall(pattern, lines, re.MULTILINE)
        
        sanitized_matches = [(TextExtractor.sanitize_speaker(speaker), time, conversation.replace('\n', ' ').strip()) for speaker, time, conversation in matches]
        df = pd.DataFrame(sanitized_matches, columns=["Speaker", "Time", "Conversation"])
        df['Conversation'] = df['Conversation'].str.replace('\n', ' ').str.strip()
        
        return df
