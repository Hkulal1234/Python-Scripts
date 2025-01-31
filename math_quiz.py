# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 06:06:21 2025

@author: harsh
"""

import random

def generate_question():
    """Generates a random math question with two numbers and an operator."""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "/", "*"])
    
    if operator == '/':
        num1 = num2 * random.randint(1, 10)
    
    question = f"{num1} {operator} {num2}"
    answer = eval(question) # Calculate the correct answer
    return question, round(answer, 2)  # Round for division

def math_quiz():
    """Runs the math quiz game."""
    print("Welcome to the math quiz game")
    score = 0
    total_question = 5
    
    for i in range(total_question):
        question,correct_answer = generate_question()
        try:
            user_answer = float(input(f"Question {i+1}: {question} = "))
            if user_answer == correct_answer:
                print("correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}")
        except ValueError:
            print("Invalid input! Please enter a number")
    print(f"\nQuiz Over! You scored {score} out of {total_question}.")
    
if __name__ == "__main__":
    math_quiz()
            