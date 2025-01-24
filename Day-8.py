import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK data
nltk.download('punkt')

# Sample paragraph
paragraph = """Natural Language Processing (NLP) is a field of artificial intelligence. It focuses on the interaction between computers and humans using natural language. Tokenization is one of the basic steps in NLP."""

# Tokenize into sentences
sentences = sent_tokenize(paragraph)

# Tokenize into words
words = word_tokenize(paragraph)

# Display results
print("Original Paragraph:")
print(paragraph)

print("\nTokenized Sentences:")
for i, sentence in enumerate(sentences, start=1):
    print(f"{i}. {sentence}")

print("\nTokenized Words:")
print(words)
