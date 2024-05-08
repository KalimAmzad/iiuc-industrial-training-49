# Python Math and Datetime Modules: In-Depth Guide

# ......................................................................
# Assignment done by : C201032- Sorowar Mahabub
# ......................................................................




"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides an in-depth guide to the math and datetime modules in Python.
We will explore:
1. Common mathematical functions and constants in the math module.
2. Handling dates and times using the datetime module.
3. Practical examples and real-world applications of both modules.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Math Module
# ----------------------
# The math module provides access to mathematical functions and constants.

import math

# # Example 1: Using math functions
# print("The square root of 16 is:", math.sqrt(16))
# print("Pi is:", math.pi)
# print("Euler's number is:", math.e)
# print("Cosine of pi is:", math.cos(math.pi))

# # Example 2: Using math to solve real-world problems
# # Calculate the area of a circle with a given radius
# radius = 5
# area = math.pi * math.pow(radius, 2)
# print(f"The area of the circle is: {area:.2f}")

# Section 2: Datetime Module
# --------------------------
# The datetime module allows you to manipulate dates and times.

import datetime
import datetime
import time
import time

# # Example 3: Working with datetime
# now = datetime.datetime.now()
# print("Current date and time:", now)
# print("Year:", now.year)
# print("Month:", now.month)
# print("Day:", now.day)


# # Example 4: Calculating differences in time
# new_year = datetime.datetime(2024, 1, 1)
# time_left_for_new_year = new_year - now
# print("Days until new year:", time_left_for_new_year.days)

# # Example 5: Formatting dates and times
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted date and time:", formatted_date)

# # Section 3: Practical Applications
# # ---------------------------------
# # Combining math and datetime for advanced calculations and data handling.

# # Example 6: Calculating age in years
# def calculate_age(birthdate):
#     today = datetime.date.today()
#     age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#     return age

# birthdate = datetime.date(1990, 6, 15)
# age = calculate_age(birthdate)
# print(f"Age is: {age} years")

# Assignments
# -----------
# Assignment 1: Write a function that calculates compound interest using the formula A = P(1 + r/n)^(nt).
def calculate_compound_interest(principal, rate, time, compound_frequency):
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    return amount

principal = 1000
rate = 0.05
time = 5
compound_frequency = 2
compound_interest = calculate_compound_interest(principal, rate, time, compound_frequency)
print("Compound interest:", compound_interest)


# Assignment 2: Create a script that prints the current time and updates every second.
import datetime
import time

while True:
     # Get current time
     current_time = datetime.datetime.now()
        
    # Print current time
    print("Current time:", current_time.strftime("%H:%M:%S"), end="\r")
        
    # Wait for one second
    time.sleep(1)