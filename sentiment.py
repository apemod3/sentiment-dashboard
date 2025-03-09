from transformers import pipeline

# Load the model ONCE to avoid reloading every time (saves time)
classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

def analyze_sentiment(text):
    result = classifier(text)
    return result[0]['label'], result[0]['score']