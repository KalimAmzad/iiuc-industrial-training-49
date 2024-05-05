# Python Loops: Comprehensive Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to using loops in Python.
We will explore:
1. Basic usage of for and while loops.
2. Loop control statements like break and continue.
3. Advanced applications integrating loops with conditional logic.
4. Complex data filtering and processing.
5. Automation of repetitive tasks.
6. Integration of loops with lists, strings, and dictionaries.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Basic Loop Usage
# ---------------------------
# For loops are ideal for iterating over sequences such as lists, tuples, or strings.

# Example 1: Simple for loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loops are used when you want to repeat something an unknown number of times, as long as a condition is true.
# Example 2: Simple while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# Section 2: Loop Control Statements
# -----------------------------------
# 'break' exits the loop entirely, and 'continue' skips to the next iteration of the loop.

# Example 3: Using break in a for loop
for num in range(1, 10):
    if num == 6:
        break
    print(num)

# Example 4: Using continue in a for loop
for num in range(1, 10):
    if num % 2 == 0:
        continue
    print(num)

# Section 3: Advanced Loop Usage
# ------------------------------
# Nested loops and loops with conditional logic can handle more complex scenarios.

# Example 5: Nested for loops with dictionaries
students = {
    "Alice": {"math": 90, "science": 85},
    "Bob": {"math": 75, "science": 92}
}
for student, grades in students.items():
    print(f"{student}'s grades:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")

# Example 6: Real-world application - Inventory Management
inventory = {
    "apples": 50,
    "bananas": 20,
    "oranges": 75
}
min_threshold = 30
discount_threshold = 60
discount_rate = 0.1

for item, quantity in inventory.items():
    if quantity < min_threshold:
        print(f"Reorder {item}.")
    elif quantity > discount_threshold:
        print(f"Apply a {discount_rate*100}% discount on {item}.")

# Assignments
# -----------
# Assignment 1: Write a script that processes a list of temperature readings. If any temperature is above a certain threshold, print a warning.
temperatures = [22, 35, 28, 31, 40]
threshold = 30
for temp in temperatures:
    if temp > threshold:
        print(f"Warning: Temperature {temp} exceeds threshold of {threshold} degrees.")

# Assignment 2: Given a list of users with their subscription status, write a loop that sends an email to all subscribed users.
users = [{"email": "user1@example.com", "subscribed": True},
         {"email": "user2@example.com", "subscribed": False},
         {"email": "user3@example.com", "subscribed": True}]
for user in users:
    if user["subscribed"]:
        print(f"Sending email to {user['email']}.")



# Example 7: User Activity Log Analysis
# This example processes a list of user activity logs to identify users who performed specific actions.

activity_logs = [
    {"user": "Alice", "action": "login"},
    {"user": "Bob", "action": "logout"},
    {"user": "Alice", "action": "upload"},
    {"user": "Charlie", "action": "login"},
    {"user": "Alice", "action": "logout"}
]

actions_count = {}
for log in activity_logs:
    user = log["user"]
    action = log["action"]
    if user not in actions_count:
        actions_count[user] = {}
    if action in actions_count[user]:
        actions_count[user][action] += 1
    else:
        actions_count[user][action] = 1

print("User actions count:", actions_count)

# Example 8: Data Pagination Display
# Simulate data pagination logic where data is displayed in chunks/pages.

data = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7", "Item8", "Item9", "Item10"]
items_per_page = 3
total_pages = (len(data) + items_per_page - 1) // items_per_page

current_page = 1
while current_page <= total_pages:
    start = (current_page - 1) * items_per_page
    end = start + items_per_page
    print(f"Page {current_page}: {data[start:end]}")
    current_page += 1

# Example 9: Monitoring System Status
# Check a list of servers and perform actions based on their status.

servers = [
    {"name": "Server1", "status": "active"},
    {"name": "Server2", "status": "inactive"},
    {"name": "Server3", "status": "active"},
    {"name": "Server4", "status": "inactive"}
]

for server in servers:
    if server["status"] == "inactive":
        print(f"{server['name']} is inactive. Attempting to restart.")
        # Simulate restart logic
        server["status"] = "active"
        print(f"{server['name']} has been restarted.")

# Example 10: Complex Condition with Nested Loops
# Process a matrix and apply conditions based on the values.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for num in row:
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")

# Assignments
# -----------
# Assignment 1: Create a script that processes a dictionary of products, checking stock levels and generating restock alerts if necessary.
products = {
    "laptop": {"stock": 4, "min_required": 10},
    "smartphone": {"stock": 15, "min_required": 5}
}

for product, details in products.items():
    if details["stock"] < details["min_required"]:
        print(f"Alert: {product} stock is low. Please restock.")
    else:
        print(f"{product} stock is sufficient.")


# Congratulations on completing the advanced section on Python loops!
# Review the assignments, try to solve them, and check your understanding of loops in Python.
