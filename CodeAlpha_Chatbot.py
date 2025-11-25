def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! 👋"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm doing great, thanks for asking! 😊"
    elif user_input in ["what is your name?", "name", "who are you"]:
        return "I'm a simple Python chatbot 🤖"
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day! 👋"
    else:
        return "Sorry, I didn't understand that. 🤔"


print("🤖 Simple Chatbot Program")
print("Type 'bye' to end the chat.\n")

while True:
    user_text = input("You: ")

    reply = chatbot_response(user_text)
    print("Bot:", reply)

    if reply.startswith("Goodbye"):
        break
