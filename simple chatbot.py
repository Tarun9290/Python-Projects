import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "I'm fine, how are you?", "I'm doing well, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"]
}

def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            bot_response = random.choice(responses[user_input])
            print("Bot: " + bot_response)
        else:
            print("Bot: I'm sorry, I don't understand what you're saying.")

chatbot()