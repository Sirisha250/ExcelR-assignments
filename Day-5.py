from collections import Counter

# Function to calculate word frequency
def word_frequency(text):
    # Convert text to lowercase and split into words
    words = text.lower().split()
    # Use Counter to count word occurrences
    word_counts = Counter(words)
    return word_counts

# Input text
text = input("Enter a text: ")

# Calculate and display word frequency
word_counts = word_frequency(text)
print("\nWord Frequency:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
