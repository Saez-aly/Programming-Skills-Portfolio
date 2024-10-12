"""
Exercise 3: Biography
In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.
"""
# First step, getting the user's input and storing it in variable as name, hometown, and age.
name = input("Please enter your full name ? ")  # string input for name
hometown = input("Please enter your hometown ? ")  # string input for hometown
age = input("Please your age ? ")  # string input for age

#To ensure valid input for age,  we need to change the age from string to integer. Age is a number. 

# Second step: Validating age input
if age.isdigit():  # checks if the age input is a valid integer (digits only)
    age = int(age)  # convert the age input to an integer
else:
    age = None  # set age to None if input is not a valid integer
    print("Invalid. Please enter a numeric value for age.")

# Third step Storing the user information in a dictionary
user_info = {
    "name": name,
    "hometown": hometown,
    "age": age}

# Finally, the last step; displays the user information, and checks if age input is valid.
if user_info["age"] is not None:
    print("Name: " + user_info["name"] + "\nHometown: " + user_info["hometown"] + "\nAge: " + str(user_info["age"]))
else:
    print("Name: " + user_info["name"] + "\nHometown: " + user_info["hometown"] + "\nAge: Invalid")

