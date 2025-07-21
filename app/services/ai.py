from textblob import TextBlob

def get_suggestions(text: str):
    blob = TextBlob(text)
    corrected = str(blob.correct())
    return corrected