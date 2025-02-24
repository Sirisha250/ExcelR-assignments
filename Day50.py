import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define dimensions
d_model = 4  # Feature size
num_vectors = 3  # Number of query/key/value vectors

# Generate random query, key, and value vectors
query = np.random.rand(num_vectors, d_model)
key = np.random.rand(num_vectors, d_model)
value = np.random.rand(num_vectors, d_model)

# Compute dot-product attention scores (QK^T)
attention_scores = np.dot(query, key.T)

# Scale by sqrt(d_model) for stability
attention_scores /= np.sqrt(d_model)

# Apply softmax to get attention weights
attention_weights = np.exp(attention_scores) / np.sum(np.exp(attention_scores), axis=1, keepdims=True)

# Compute the final attention output (Weighted sum of value vectors)
attention_output = np.dot(attention_weights, value)

# Print results
print("Query Vectors:\n", query)
print("Key Vectors:\n", key)
print("Value Vectors:\n", value)
print("Attention Scores:\n", attention_scores)
print("Attention Weights (Softmax Applied):\n", attention_weights)
print("Final Attention Output:\n", attention_output)
