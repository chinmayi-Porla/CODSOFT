def chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case insensitivity

    # Define predefined rules and responses
    responses = {
        "hello": "Hi there! How can I assist you?",
        "how are you": "I'm just a bot, but thanks for asking!",
        "what is your name": "I'm a chatbot created by OpenAI.",
        "bye": "Goodbye! Have a great day!",
    }

    # Check user input against predefined rules and provide appropriate responses
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I didn't understand that."

# Main loop to interact with the chatbot
print("Welcome! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print(chatbot(user_input))
        break
    else:
        print("Bot:", chatbot(user_input))