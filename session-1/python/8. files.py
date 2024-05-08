# Python File I/O and JSON Handling: Comprehensive Guide

# ......................................................................
# Assignment done by : C201032- Sorowar Mahabub
# ......................................................................




"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to file input/output operations and JSON handling.
We will explore:
1. Reading and writing to plain text files.
2. Working with CSV files using the csv module.
3. Handling JSON data with the json module.
4. Practical examples and real-world applications.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Plain Text Files
# ---------------------------
# Reading and writing plain text files is often the first step in file manipulation.

# # Example 1: Writing to a Text File
# with open('example.txt', 'w') as file:
#     file.write("Hello, Python learners!\n")
#     file.write("Welcome to file I/O operations.")

# # Example 2: Reading from a Text File
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# Section 2: CSV Files
# --------------------
# CSV (Comma-Separated Values) files are commonly used for storing tabular data.

import csv

# Example 3: Writing to a CSV File
# with open('example.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age", "City"])
#     writer.writerow(["Alice", 28, "New York"])
#     writer.writerow(["Bob", 22, "Los Angeles"])
#     writer.writerow(["Carol", 24, "Chicago"])

# # Example 4: Reading from a CSV File
# with open('example.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# # Section 3: JSON Data
# # --------------------
# # JSON (JavaScript Object Notation) is a lightweight data-interchange format.

# import json

# # Example 5: Writing JSON to a File
# data = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# with open('data.json', 'w') as file:
#     json.dump(data, file)


# # Example 6: Reading JSON from a File
# with open('data.json', 'r') as file:
#     data = json.load(file)
#     print(data)

# # Section 4: Practical Applications
# # ---------------------------------
# # Combining file I/O with real-world data processing.

# # Example 7: Processing JSON Data from a File
# # Suppose we have a JSON file containing multiple user records.
# users = [
#     {"name": "Alice", "age": 25, "email": "alice@example.com"},
#     {"name": "Bob", "age": 30, "email": "bob@example.com"}
# ]
# with open('users.json', 'w') as file:
#     json.dump(users, file)

# with open('users.json', 'r') as file:
#     users = json.load(file)
#     for user in users:
#         print(f"{user['name']} ({user['age']}): {user['email']}")

# Assignments
# -----------
# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.
import csv
import json

def csv_to_json(csv_file, json_file):
    products = []

    # Read CSV file and convert each row to a dictionary
    with open(csv_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            products.append(row)

    # Write products list to a JSON file
    with open(json_file, 'w') as jsonfile:
        json.dump(products, jsonfile, indent=4)


csv_file = 'H:\Field Work - IM - DS\Industrial_Training_Assignment\session-1\python\products.csv'
json_file = 'H:\Field Work - IM - DS\Industrial_Training_Assignment\session-1\python\products.json'
csv_to_json(csv_file, json_file)

        
# Assignment 2: Create a log file writer that appends log messages to a file with timestamps.
import logging
from logging.handlers import RotatingFileHandler
import os

# Ensure the log directory exists
log_dir = 'H:\\Field Work - IM - DS\\Industrial_Training_Assignment\\session-1\\python\\logs'
os.makedirs(log_dir, exist_ok=True)

# Set up logging to file
log_file = os.path.join(log_dir, 'app.log')
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

# Create a file handler which logs even debug messages
fh = RotatingFileHandler(log_file, maxBytes=10485760, backupCount=5)
fh.setLevel(logging.INFO)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)

def log_message(message):
    logger.info(message)

# Congratulations on completing the comprehensive section on Python file I/O and JSON handling!
# Review the assignments, try to solve them, and check your understanding of file operations and data formats.
