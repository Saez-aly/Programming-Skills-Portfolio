# -*- coding: utf-8 -*-
"""
Exercise 5: Days of the Month
Direction: Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.
"""
# First is to create a dictionary that maps month numbers (1-12) to the number of days in each month.
days_in_month = {
    1: 31,  # January has 31 days
    2: 28,  # February normally has 28 days (we'll adjust for leap years)
    3: 31,  # March has 31 days
    4: 30,  # April has 30 days
    5: 31,  # May has 31 days
    6: 30,  # June has 30 days
    7: 31,  # July has 31 days
    8: 31,  # August has 31 days
    9: 30,  # September has 30 days
    10: 31, # October has 31 days
    11: 30, # November has 30 days
    12: 31  # December has 31 days
}

# Second; Ask the user for the month number. 
# We need to convert the input from string to integer because input() returns text.
month = int(input("Enter the month number (1-12): "))

# Third: Check if the month is valid (between 1 and 12)
if month in days_in_month:
    # Step 4: Special case for February (month 2), we need to ask if it's a leap year
    if month == 2:
        leap_year = input("Is it a leap year? (yes/no): ")
        
        # Step 5: Check if the user entered "yes" (ignoring case, so 'Yes' or 'YES' work too)
        if leap_year.lower() == "yes":
            # If it's a leap year, February has 29 days
            print("Month " + str(month) + " has 29 days (leap year).")
        else:
            # If it's not a leap year, February has 28 days
            print("Month " + str(month) + " has " + str(days_in_month[month]) + " days.")
    else:
        # For all other months, simply print the number of days using string concatenation
        print("Month " + str(month) + " has " + str(days_in_month[month]) + " days.")
        
        """there are shorter way to do this, but im using concantenation since im applying what i've learned in class and sololearn"""
else:
    # If the input is not valid (not between 1 and 12), print an error message
    print("Invalid month number. Please enter a number between 1 and 12.")


