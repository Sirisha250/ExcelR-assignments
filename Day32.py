import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Download necessary NLTK resources
nltk.download('punkt')

def calculate_tf(file_path, top_n=5):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Convert tokens to lowercase and filter non-alphabetic words
    words = [word.lower() for word in tokens if word.isalpha()]
    
    # Calculate term frequency
    word_counts = Counter(words)
    
    # Get the top N most frequent words
    most_common_words = word_counts.most_common(top_n)
    
    # Display results
    print("Top", top_n, "most frequent tokens:")
    for word, count in most_common_words:
        print(f"{word}: {count}")

# Example usage (replace 'sample.txt' with your actual file path)
file_path = 'sample.txt'
calculate_tf(file_path)
