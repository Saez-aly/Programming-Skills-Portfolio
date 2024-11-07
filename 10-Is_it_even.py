# -*- coding: utf-8 -*-
"""
Exercise 10: Is it even?
Directiions: Write a program that tests if a value is even or odd. Follow the instructions outlined below: The program should ask the user for a number from within the main function.
The entered number should be passed to a function that determines if the value is even or odd.
The function should return a message indicating whether the number is even or odd.
The message returned by the function should be printed from within the main function.

"""

#First step is to know if the number is odd or even.
#We would know a number if even if its divisible by 2 otherwise its odd so we will be using modulus operator..

def is_it_even (number):
    # This function checks if the number is even or odd
    if number % 2 == 0:  # Checks if the number can be divided by 2
    
#Second step is to return a message saying whether the number is odd or even.
        return "The number is even."  # displays if the number is even
    else:
        return "The number is odd."  # displays if the number is odd

#Third step  is to make sure that the message was returned from within the main function.
def main():
    # This is the main function where the program starts
    user_input = input("Please enter a number: ")  # Ask the user for a number
    user_input = int(user_input)  # Convert the input from a string to an integer
    result = is_it_even (user_input)  # Call the function with the user's number
    print(result)  # Print the result message to the console

# And lastly, this line checks if the script is run directly.
if __name__ == "__main__":
    main()  # Call the main function to start the program 

"""What i have learned: Is it even? In this final activity, I learned how to create a program that checks whether the number is even or odd. I have already learned it in class so I just applied it here. So, I used modulus to determine if the number is even, which of course if its divisible by two. 
By getting user input, passing it to a function, and returning a feedback so the user get their answer. Lastly, is to make sure everything works."""
