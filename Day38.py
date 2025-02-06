from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample text data (messages)
text_data = [
    "Spam messages are annoying",
    "I won a lottery",
    "This is a normal message",
    "Claim your prize now",
    "Hurry up, limited time offer",
    "Hello, how are you doing today?",
    "Free tickets available",
    "Congratulations, you've won!"
]

# Labels (0 = Not Spam, 1 = Spam)
labels = [1, 0, 0, 1, 1, 0, 1, 0]  # Corresponding labels for the above messages

# Convert text data into numerical format using TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(text_data)

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Initialize the Decision Tree Classifier
classifier = DecisionTreeClassifier()

# Train the model using the training data
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Calculate and print accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")

# Example of making predictions on new, unseen text data
new_text = ["Win a new car today", "Hello, let's meet up soon"]
new_data = vectorizer.transform(new_text)
predictions = classifier.predict(new_data)

print("\nPredictions for new text:")
for text, prediction in zip(new_text, predictions):
    print(f"{text} -> {'Spam' if prediction == 1 else 'Not Spam'}")
