# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 06:58:41 2025

@author: harsh
"""

import random

word_list = ['Yellow','Baby', 'Table', 'Phone', 'Hands']
word = random.choice(word_list)

hidden_word = list(word)
blank_index = random.randint(0, len(word) - 1)

hidden_word[blank_index] = "_" 
    
hidden_word_display = " ".join(hidden_word)
attempts = 5

print("🎯 Welcome to Fill in the Blanks Game! 🎯")
print(f"🔹 Guess the missing letters in: {hidden_word_display}")

while attempts > 0:
    
    guess = input("\nEnter a missing letter: ").lower()
    
    if len(guess) !=1 or not guess.isalpha():
        print("❌ Invalid input! Enter a single letter.")
        continue
    
    if guess == word[blank_index].lower():
        hidden_word[blank_index] = guess
        print(f"\n🎉 Correct! The word is: {''.join(hidden_word).upper()}")
        break
        
    else:
        print("❌ Wrong guess!")
        attempts -= 1
        print(f"Remaining attempts: {attempts}")

    print(f"\nCurrent word: {' '.join(hidden_word)}")
    print(f"Remaining attempts: {attempts}")

# Game Over conditions
if attempts == 0:
    print("\n💀 Game Over! The correct word was:", word.upper())

