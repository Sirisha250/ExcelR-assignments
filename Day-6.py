import nltk
from nltk.corpus import stopwords
import spacy

# Download NLTK stopwords
nltk.download('stopwords')

# Initialize NLTK stopwords
nltk_stopwords = set(stopwords.words('english'))

# Initialize spaCy model
nlp = spacy.load('en_core_web_sm')

# Function to process text
def process_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Use spaCy to tokenize text
    doc = nlp(text)
    # Remove stopwords using NLTK
    filtered_words = [token.text for token in doc if token.text not in nltk_stopwords]
    return filtered_words

# Input text
text = input("Enter a text: ")

# Process the text
result = process_text(text)

# Display the results
print("\nProcessed Text (without stopwords):")
print(" ".join(result))
