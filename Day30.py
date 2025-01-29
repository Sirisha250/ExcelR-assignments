from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the polarity of the text
    polarity = blob.sentiment.polarity
    
    # Determine sentiment category
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    print(f"Sentiment: {sentiment} (Polarity: {polarity:.2f})")

# Example usage
text = "I love this beautiful day!"
analyze_sentiment(text)
