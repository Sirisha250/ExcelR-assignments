import spacy

def perform_ner(text):
    # Load the SpaCy English model
    nlp = spacy.load("en_core_web_sm")
    
    # Process the text
    doc = nlp(text)
    
    # Print named entities and their types
    for ent in doc.ents:
        print(f"{ent.text}: {ent.label_}")

# Example usage
text = "Barack Obama was the 44th President of the United States and was born in Hawaii."
perform_ner(text)
