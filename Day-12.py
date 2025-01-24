from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Input text
text = 'data science machine learning artificial intelligence'

# Generate the WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off the axis
plt.title("WordCloud of Input Text", fontsize=16)
plt.show()

# Save the WordCloud as an image
wordcloud.to_file("wordcloud.png")
print("WordCloud image saved as 'wordcloud.png'")
