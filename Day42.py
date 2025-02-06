import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

# Prompt for text completion
prompt = "Artificial Intelligence is..."

# Generate completion using the GPT model (text-davinci-003)
response = openai.Completion.create(
    model="text-davinci-003",  # Model name
    prompt=prompt,             # Input text
    max_tokens=50,             # Maximum number of tokens to generate
    n=1,                       # Number of completions to generate
    stop=None,                 # Define any stopping conditions
    temperature=0.7            # Adjust creativity of output (0 to 1)
)

# Extract the generated text from the response
generated_text = response.choices[0].text.strip()

# Output the generated text
print("Generated text: ", generated_text)
