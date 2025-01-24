import spacy

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Input sentence
sentence = "NLP is amazing and fun to learn."

# Process the sentence with spaCy
doc = nlp(sentence)

# Perform POS tagging and display the results
print("Word\tPOS\tTag Description")
print("-" * 30)
for token in doc:
    print(f"{token.text}\t{token.pos_}\t{spacy.explain(token.pos_)}")
