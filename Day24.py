import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Download necessary NLTK resources
nltk.download('punkt')

def get_most_common_words(file_path, num_words=10):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Convert to lowercase and filter out non-alphabetic tokens
    words = [word.lower() for word in tokens if word.isalpha()]
    
    # Calculate word frequency
    freq_dist = FreqDist(words)
    
    # Get the most common words
    common_words = freq_dist.most_common(num_words)
    
    # Display results
    for word, freq in common_words:
        print(f"{word}: {freq}")

# Example usage (replace 'sample.txt' with your text file path)
file_path = 'sample.txt'
get_most_common_words(file_path)
