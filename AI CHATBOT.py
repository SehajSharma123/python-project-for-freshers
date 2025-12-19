print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Chatbot: Goodbye!")
        break
    elif "hello" in user:
        print("Chatbot: Hi! How can I help you?")
    elif "name" in user:
        print("Chatbot: I am a Python Chatbot.")
    elif "how are you" in user:
        print("Chatbot: I am fine 😊")
    else:
        print("Chatbot: Sorry, I don't understand.")
