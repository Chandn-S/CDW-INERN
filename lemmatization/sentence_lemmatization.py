#SENTENCE LEMMATIZATION


# Cleaning the texts
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Download stopwords and WordNet resources
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize lemmatizer
wordnet = WordNetLemmatizer()

# Example sentences for demonstration
sentences = ['he is a good boy', 'she is a good girl', 'boy & girl are good']

# Cleaning the texts
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])  # Remove non-alphabetic characters
    review = review.lower()  # Convert to lowercase
    review = review.split()  # Tokenize
    # Use lemmatization and remove stopwords
    review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)  # Join back to a single string
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=500, ngram_range=(1, 3))
X = cv.fit_transform(corpus).toarray()

# Output vocabulary
print(cv.vocabulary_)