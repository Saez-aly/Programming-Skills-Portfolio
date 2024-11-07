"""Exercise 7: Some Counting
Define- Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console in each case."""

# This program demonstrates counting in different ways using a for loop.

# Counting up from 0 to 50 (by 1)
print("Counting up from 0 to 50:")
for i in range(0, 51, 1):  # The range starts at 0, ends at 50 (inclusive), and increases by 1
    print(i)  # This prints each number as it counts up from 0 to 50

# Counting down from 50 to 0 (by -1)
print("\nCounting down from 50 to 0:")
for i in range(50, -1, -1):  # The range starts at 50, ends at 0 (inclusive), and decreases by 1 each time
    print(i)  # This prints each number as it counts down from 50 to 0

# Counting up from 30 to 50 (by 1)
print("\nCounting up from 30 to 50:")
for i in range(30, 51, 1):  # The range starts at 30, ends at 50 (inclusive), and increases by 1
    print(i)  # This prints each number as it counts up from 30 to 50

# Counting down from 50 to 10 (by -2)
print("\nCounting down from 50 to 10 in steps of 2:")
for i in range(50, 9, -2):  # The range starts at 50, ends at 10, and decreases by 2 each time
    print(i)  # This prints each number as it counts down by 2 from 50 to 10

# Counting up from 100 to 200 (by 5)
print("\nCounting up from 100 to 200 in steps of 5:")
for i in range(100, 201, 5):  # The range starts at 100, ends at 200 (inclusive), and increases by 5 each time
    print(i)  # This prints each number as it counts up by 5 from 100 to 200

""" What I have learned: In this exercise I learn how to use loops in
various ways such as applying range function to define the starting and
ending points, along with increments whether its one or two. Practicing
both upwards and downwards, as well as specific slicing, stops or
interval; different types of counting as we call it—in a single code
really stretched my mind and my grasp about looping and number
manipulation"""
