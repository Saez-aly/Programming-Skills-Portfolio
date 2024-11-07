# -*- coding: utf-8 -*-
"""
Exercise 6: Brute Force Attack 
Directions: Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.
Addional: Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted."""

# Define the correct password
correct_password = "12345"

# Start with 0 attempts
attempts = 0

# Set up a while loop for the password attempts
while True:
    password_input = input("Enter your password: ")  # Get user input for password
    attempts += 1  # Increment the attempt count
    
    if password_input == correct_password:  # Check if the input matches the correct password
        print("Access granted!")
        break  # Exit the loop if the password is correct
    elif attempts == 1:  # First wrong attempt
        print("Wrong password. Try again.")
    elif attempts >= 2 and attempts <= 3:  # Between 2 and 3 wrong attempts
        print("Warning! You have only", 5 - attempts, "attempts left.")
    elif attempts >= 4 and attempts <= 5:  # Between 4 and 5 wrong attempts
        print("Final warning! Only", 5 - attempts, "attempt left.")
    else:  # More than 5 attempts
        print("Your access has been denied. We are calling the Dubai Police")
        break  # Exit the loop after too many wrong attempts

""" What I have learned: Brute force attack with Additional requirement
We did one in class similar to this, it’s parking fine. So, for this activity
I got practice using if-else statements because I used it to handle the
situation where its giving warning after a certain number of attempts. I
think I have gotten better at using conditions because this code can;
grant access is the input is correct, has only 5 attemps, and calls the
authority for 5th wrong attempt."""
