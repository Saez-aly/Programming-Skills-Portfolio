# -*- coding: utf-8 -*-
"""
Exercise 4: Primitive Quiz
Direction: In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.
"""
# First step is to setup Dictionary containing 10 European countries and their capitals.
primitive_quiz = {
    "Greece": "Athens",
    "Finland": "Helsinki",
    "Hungary": "Budapest",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Ireland": "Dublin",
    "Slovakia": "Bratislava",
    "Croatia": "Zagreb",
    "Switzerland": "Bern",
    "Iceland": "Reykjavik"
}

"""There are a lot of ways to code this quiz, a lot of functions to use, but I want to apply what I've learn in class and in sololearn website. Which are for loop and concantenation, else if"""

# count for correct answers
correct_answers = 0

# Step 2: Use Loop through each country and ask for the capital
for country, capital in primitive_quiz.items():                # Loop to ensure all 10 countries will appear in the quiz.
    answer = input("What is the capital of " + country + "? ") # Concatenation for the question
    if answer.lower() == capital.lower():                      # This method call makes sure that the quiz is not case-sensitive.
        print("Correct!")                                      # Feedback for right answer.
        correct_answers += 1                                   # Increment the correct answers counter.
    else:
        print("Wrong! The correct answer is " + capital + ".")  # Feedback for wrong answer.

# Step 3: Provide feedback after the quiz is done
total_questions = len(primitive_quiz)                          # Total number of questions
print("\nQuiz completed! You got " + str(correct_answers) + " out of " + str(total_questions) + " correct.")

"""The quiz felt discouraging. so i added a final touch where the user can see their scores"""
