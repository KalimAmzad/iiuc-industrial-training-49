# Python Functions: Comprehensive Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to functions in Python.
We will explore:
1. Basic function definitions and calls.
2. Parameters, arguments, and return values.
3. Variable scope and lifetime within functions.
4. Advanced function concepts like decorators, lambda functions, and error handling.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Basic Functions
# --------------------------
# Functions are defined using the `def` keyword. They allow you to encapsulate code for reuse.

# Example 1: Simple Function
def greet(name):
    """Greets a person with their name."""
    print(f"Hello, {name}!")

greet("Alice")

# Section 2: Parameters and Return Values
# ---------------------------------------
# Functions can accept parameters and return values to the caller.

# Example 2: Function with Parameters and Return Value
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add_numbers(5, 3)
# print(f"The sum is {result}.")


# Functions can return multiple values using tuples.
# Example 3: Function with Multiple Return Values
def get_user_data():
    """Returns multiple pieces of user data."""
    name = "Alice"
    age = 30
    membership = True
    return name, age, membership

user_name, user_age, is_member = get_user_data()
# print(f"Name: {user_name}, Age: {user_age}, Membership: {is_member}")


# Functions can have default parameters and accept variable numbers of arguments.
# Example 4: Default Arguments and *args, **kwargs
def create_profile(name, email, *interests, **details):
    """Creates a user profile dictionary with given details."""
    profile = {
        "name": name,
        "email": email,
        "interests": interests,
        "details": details
    }
    # process profile

    return profile

profile = create_profile("Bob", "bob@example.com", "nasheed", "art", age=25, location="New York")
# print(profile)
profile = create_profile("Bob", "bob@example.com", "nasheed", "art", "calliography", age=35, location="Boston")
# print(profile)
profile = create_profile("Bob", "bob@example.com", "swimming", "art", "calliography", "listening_quran", age=27, location="Chicago")
# print(profile)


# Section 3: Variable Scope
# -------------------------
# Variables defined inside a function are local to that function. Variables defined outside are global.

# Example 3: Local vs. Global Variables
x = "global"

def test_scope():
    y = "local"
    print("Inside function:", y)

test_scope()
print("Outside function:", x)

# Section 4: Advanced Function Concepts
# -------------------------------------

# Decorators enhance the behavior of functions, and lambda functions allow for concise function definitions.

# Example 3: Using Decorators for Logging
def log_function_data(func):
    """Decorator to log function usage."""
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} was called with args: {args} and kwargs: {kwargs}")
        # save into database with args & kwargs
        return func(*args, **kwargs)
    return wrapper

@log_function_data
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add(10, 5))


# Example 5: Lambda Functions
# Lambda functions are useful for short, simple functions.
# Lambda functions are small anonymous functions defined with the `lambda` keyword.
square = lambda x: x * x
print(f"Square of 5 is {square(5)}.")


# Proper error handling in functions is crucial for robust applications.
# Example 6: Error Handling in Functions
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Only numbers are allowed.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"The result is {result}")
    finally:
        print("Executing finally clause.")

divide(10, 2)
divide(10, "0")

# Assignments
# -----------
# Assignment 1: Write a function that calculates the factorial of a number and handles any potential errors.
def factorial(n):
    if not isinstance(n, int) or n < 0:
        print("Error: The number must be a non-negative integer.")
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Congratulations on completing the advanced section on Python functions!
# Review the assignments, try to solve them, and check your understanding of function concepts.
