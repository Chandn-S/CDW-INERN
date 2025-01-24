# Ensure gensim is installed by running the following command in your terminal:
# pip install gensim

from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import numpy as np

# Sample sentences for training the Word2Vec model
sentences = [
    ["This", "is", "a", "positive", "sentence"],
    ["This", "is", "another", "positive", "sentence"],
    ["This", "is", "a", "negative", "sentence"],
    ["I", "love", "sunny", "days"],
    ["Rainy", "days", "make", "me", "feel", "sad"]
]

# Train a Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# Save the model (optional)
model.save("word2vec.model")

def calculate_similarity(text1, text2):
    vector1 = np.mean([model.wv[word] for word in text1.split() if word in model.wv], axis=0)
    vector2 = np.mean([model.wv[word] for word in text2.split() if word in model.wv], axis=0)
    similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    return similarity

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

print(f"Similarity between '{text1}' and '{text2}': {similarity_1_2}")
print(f"Similarity between '{text1}' and '{text3}': {similarity_1_3}")
print(f"Similarity between '{text1}' and '{text4}': {similarity_1_4}")
print(f"Similarity between '{text4}' and '{text5}': {similarity_4_5}")