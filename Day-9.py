import re

# Function to clean text
def clean_text(text):
    # Remove special characters using regex
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Convert text to lowercase
    text = text.lower()
    return text

# Test the function
input_text = 'Hello, World! Welcome to NLP 101.'
cleaned_text = clean_text(input_text)

# Display the results
print("Original Text:")
print(input_text)

print("\nCleaned Text:")
print(cleaned_text)
