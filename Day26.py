from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(text1, text2):
    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()
    
    # Transform the text data into TF-IDF vectors
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    
    # Compute the cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    
    return similarity[0][0]

# Example usage
text1 = "This is a sample text."
text2 = "This text is a simple example."
similarity_score = calculate_cosine_similarity(text1, text2)
print(f"Cosine Similarity: {similarity_score:.4f}")
