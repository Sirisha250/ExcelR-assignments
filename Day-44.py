def simple_chatbot():
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "hello":
            print("Chatbot: Hi! How can I help you?")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break  # Exit the loop
        else:
            print("Chatbot: I'm sorry, I don't understand.")

# Run the chatbot
simple_chatbot()
