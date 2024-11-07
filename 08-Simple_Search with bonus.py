# -*- coding: utf-8 -*-
"""
Exercise 8: Simple Search 
Direction: Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".
Additonal: 1.) Allow the user to input the search term instead of using a predefined value. 2.) Implement the search functionality based on user input.
"""
# Step 1: Create a list of strings wih the boys names.
boys_list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # I created a variable named boys_list and listed down the strings, which are the boys.

# Step 2: Allow user to input a search term.
search = input("Enter a name to search: ")  # This allows the user to input or search for names instead of predefined value. 
#In order to increase its functionality and usability, we would want to add a message/feedback whether the name is on the list or not. 

# Step 3: Search for the name in the list
if search in boys_list:  # Check if the input name is in the list
    print(search + " is on the list.")  # If found, it displays a confirmation message
else:
    print(search + " is not on the list.")  # If not found, it displays an error message.
