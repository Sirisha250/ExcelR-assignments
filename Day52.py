from transformers import BertTokenizer

# Load the pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Define a sample sentence
sentence = "Hugging Face makes NLP easy and accessible!"

# Tokenize the sentence
tokens = tokenizer.tokenize(sentence)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

# Print the results
print("Original Sentence:", sentence)
print("Tokenized Output:", tokens)
print("Token IDs:", token_ids)
