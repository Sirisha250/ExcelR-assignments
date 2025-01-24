import requests
from bs4 import BeautifulSoup

# Function to fetch and print the title of a webpage
def fetch_webpage_title(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract and return the title
            title = soup.title.string if soup.title else "No title found"
            return title
        else:
            return f"Failed to fetch webpage. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"

# Test the function
url = 'https://example.com'
title = fetch_webpage_title(url)

# Display the results
print(f"URL: {url}")
print(f"Title: {title}")
