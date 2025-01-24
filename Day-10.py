import re

# Function to extract email addresses
def extract_emails(text):
    # Regular expression pattern for email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    # Find all email addresses in the text
    emails = re.findall(email_pattern, text)
    return emails

# Test the function
input_text = 'Contact us at support@example.com and sales@example.org.'
email_addresses = extract_emails(input_text)

# Display the results
print("Original Text:")
print(input_text)

print("\nExtracted Email Addresses:")
print(email_addresses)
