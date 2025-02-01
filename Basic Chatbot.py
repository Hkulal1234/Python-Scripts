# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:18:59 2025

@author: harsh
"""

import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you ?", ["I'm doing great, thanks for asking!", "I'm just a bot, but I'm good!"]),
    (r"what is your name ?", ["I'm a chatbot!", "I don't have a name, but I'm here to help!"]),
    (r"bye", ["Goodbye! Have a nice day!", "See you later!"]),
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Chatbot : Goodbye! ")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response if response else "I'm sorry, I don't understand that.")

start_chat()