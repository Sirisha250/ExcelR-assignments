def chatbot():
    responses = {
        "hello": "Hi! How can I help you?",
        "how are you?": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a nice day!"
    }

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in responses:
            print(f"Chatbot: {responses[user_input]}")
            if user_input == "bye":
                break  # Exit the loop
        else:
            print("Chatbot: I'm sorry, I don't understand.")

# Run the chatbot
chatbot()
