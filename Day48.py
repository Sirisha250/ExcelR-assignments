from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
    return summary[0]['summary_text']

# Example paragraph
paragraph = """
Artificial Intelligence (AI) is rapidly transforming various industries, from healthcare to finance.
It enables automation, enhances decision-making, and provides deep insights into large datasets.
With advancements in machine learning and deep learning, AI-powered solutions are becoming more sophisticated,
helping businesses optimize their operations and improve customer experiences.
"""

# Generate summary
summary = summarize_text(paragraph)
print("Summary:", summary)
