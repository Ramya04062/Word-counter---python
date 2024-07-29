import re

def clean_text(text):
    # Remove punctuation and make lowercase
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text


