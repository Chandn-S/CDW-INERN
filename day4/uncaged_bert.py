# Ensure necessary libraries are installed
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "transformers", "sentence-transformers"])

from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import torch

# Load pre-trained SentenceTransformer model for similarity
similarity_model = SentenceTransformer('all-MiniLM-L6-v2')

def get_bert_embedding(text):
    # Get embeddings from the SentenceTransformer model
    embeddings = similarity_model.encode(text, convert_to_tensor=True)
    return embeddings

def calculate_similarity(text1, text2):
    embedding1 = get_bert_embedding(text1)
    embedding2 = get_bert_embedding(text2)

    # Calculate cosine similarity
    similarity_score = util.pytorch_cos_sim(embedding1, embedding2).item()
    return similarity_score

# Load pre-trained sentiment analysis model
sentiment_model = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

def analyze_sentiment(text):
    result = sentiment_model(text)[0]
    return result['label'], result['score']

# Example usage with more sentences
text1 = "This is a positive sentence."
text2 = "This is another positive sentence."
text3 = "This is a negative sentence."
text4 = "I love sunny days."
text5 = "Rainy days make me feel sad."

similarity_1_2 = calculate_similarity(text1, text2)
similarity_1_3 = calculate_similarity(text1, text3)
similarity_1_4 = calculate_similarity(text1, text4)
similarity_4_5 = calculate_similarity(text4, text5)

sentiment_1 = analyze_sentiment(text1)
sentiment_2 = analyze_sentiment(text2)
sentiment_3 = analyze_sentiment(text3)
sentiment_4 = analyze_sentiment(text4)
sentiment_5 = analyze_sentiment(text5)

print(f"Similarity between '{text1}' and '{text2}': {similarity_1_2}")
print(f"Similarity between '{text1}' and '{text3}': {similarity_1_3}")
print(f"Similarity between '{text1}' and '{text4}': {similarity_1_4}")
print(f"Similarity between '{text4}' and '{text5}': {similarity_4_5}")

print(f"Sentiment analysis of '{text1}': {sentiment_1}")
print(f"Sentiment analysis of '{text2}': {sentiment_2}")
print(f"Sentiment analysis of '{text3}': {sentiment_3}")
print(f"Sentiment analysis of '{text4}': {sentiment_4}")
print(f"Sentiment analysis of '{text5}': {sentiment_5}")