import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import SnowballStemmer
from nltk.corpus import wordnet
from nltk import download
from nltk.stem import WordNetLemmatizer
import string

# Download NLTK data
download('wordnet')
download('omw-1.4')

# Initialize stemmer and lemmatizer
stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()

# Function to preprocess text
def preprocess_text(text):
    # Tokenize and remove punctuation
    tokens = simple_preprocess(text)
    # Remove stopwords
    tokens = [token for token in tokens if token not in STOPWORDS]
    # Apply stemming
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    # Apply lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(token, wordnet.VERB) for token in stemmed_tokens]
    return lemmatized_tokens

# Read sample text file
file_path = "sample_text.txt"  # Replace with your file path
with open(file_path, 'r') as file:
    text = file.read()

# Preprocess the text
processed_tokens = preprocess_text(text)

# Display results
print("Original Text:")
print(text)
print("\nProcessed Tokens:")
print(processed_tokens)
