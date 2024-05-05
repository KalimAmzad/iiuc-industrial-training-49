# Advanced Python: Strings

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to provide a comprehensive understanding of Python strings.
We will explore:
1. String basics - Creation, accessing, and updating.
2. All string methods and their uses.
3. Practical applications of strings in data manipulation.

Each section includes detailed explanations, examples, and challenging assignments.
"""

# Section 1: String Basics
# ------------------------
# Strings in Python are sequences of characters.

# Example 1: Creating and Using Strings
simple_string = "Hello, Python learners!"
# print(simple_string[0])  # Accessing the first character

# Strings are immutable
# Trying to change a character directly will raise a TypeError
# simple_string[0] = "h"  # Uncommenting this line will cause an error

# String Methods
# Finding substrings
print(simple_string.find('Python'))  # Returns the start index of 'Python'

# Replacing substrings
modified_string = simple_string.replace('learners', 'developers')
# print("Modified String:", modified_string)

# Splitting strings
# print(simple_string)

marks = "80: 83: 70: 48: 47"
marks_list = marks.split(': ')  # Splits the string into a list of marks
# print("Array of marks:", marks_list)

words = simple_string.split(',')  # Splits the string into a list of words
print("Array of words:", words)

# Joining strings
joined_string = ' '.join(words)  # Joins the list back into a single string
print("Joined string:", joined_string)

# Case conversion
# print(simple_string.upper())  # Converts to uppercase
# print(simple_string.lower())  # Converts to lowercase

# Stripping whitespace
user_input = "   some user input   "
print(user_input.strip())  # Removes leading and trailing whitespace
print(user_input.rstrip())  # Removes trailing whitespace
print(user_input.lstrip())  # Removes leading whitespace

# Assignment 1: Create a string that contains a simple bio data like name, age, and country. Extract each piece of information and print them separately.
# Write your code below:


# Section 2: Advanced String Operations
# -------------------------------------
# Strings can be used in more complex operations like formatting.

# Example 2: String Formatting
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# Old-style formatting
old_greeting = "Hello, my name is %s and I am %d years old." % (name, age)
print(old_greeting)


# Assignment 2: Create a formatted string that includes data from a list or dictionary. For example, use a dictionary to store a person's information and format a string to include it.
# Write your code below:


# Section 3: Advanced Slicing and Multiline Strings
# -------------------------------------
# Python strings are immutable, which means that every string operation creates a new string.

# Example 1: Advanced Slicing
complex_string = "Hello, Python enthusiasts!"
reverse_string = complex_string[::-1]  # Reverses the string using slicing
print(reverse_string)

# Multiline strings
multiline_string = """This is a string that spans
multiple lines within triple quotes."""
print(multiline_string)

# Raw strings
path = r"C:\new_folder\test.txt"  # Raw string ignores escape characters
print(path)

# String Methods
# Counting substrings
print("The count of 'n' is:", complex_string.count('n'))

# Formatting strings with str.format() and f-strings
pi = 3.14159
formatted_string = "The value of pi is {:.2f}".format(pi)  # Formatting to two decimal places
print(formatted_string)

# Assignment 3: Write a function that takes a string and returns a dictionary with the counts of each character in the string.
# Write your code below:


# Section 4: Regular Expressions
# ------------------------------
# Regular expressions are used for pattern matching in strings.


import re

# Basic Regex: Matching Literal Strings
pattern = 'world'
text = 'Hello, world!'
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found.")


# Character Classes
pattern = r'\d+'  # Matches one or more digits
text = 'There are 123 apples, 45 oranges, and 78 bananas.'
matches = re.findall(pattern, text)
print("Numbers found:", matches)

# Alternation and Grouping
pattern = r'apple|banana'  # Matches 'apple' or 'banana'
text = 'I like apples, oranges and bananas.'
matches = re.findall(pattern, text)
print("Fruits found:", matches)


# Positive Lookahead
pattern = r'\d{2}(?=px)'  # Matches a number only if it's followed by 'px'
text = 'The image is 106px by 209px.'
matches = re.findall(pattern, text)
print("Numbers followed by 'px':", matches)

# Non-capturing Group
pattern = r'(?:\d{3}-)?\d{3}-\d{4}'  # Matches phone numbers with optional area code
text = 'Call 415-555-1234 or 555-4321'
matches = re.findall(pattern, text)
print("Phone numbers found:", matches)


# Example: Email Validation
# A more detailed regex for validating an email address.
email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email = "example@domain.com"
# email = "example@domain"
if re.match(email_regex, email):
    print("Valid email!")
else:
    print("Invalid email!")


# Example: Extracting Phone Numbers
# Regex to match US phone number formats
phone_regex = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
text = "Call me at 415-555-1011 tomorrow, or at 415.555.9999 for office line."
phones = re.findall(phone_regex, text)
print("Phone numbers found:", phones)

# Example: Replacing Text
# Replacing all occurrences of digits with a placeholder
replaced_text = re.sub(r'\d', 'X', 'My number: 12345, office: 98765')
print("Censored text:", replaced_text)

# Assignment: Write a regex to find all the hashtags in a string.
text_with_hashtags = "This is a #great day to learn #regex in #Python!"
hashtags = re.findall(r"#(\w+)", text_with_hashtags)
print("Hashtags:", hashtags)

# Congratulations on completing the advanced section on Python strings!
# Review the assignments, try to solve them, and check your understanding of string manipulation techniques.
