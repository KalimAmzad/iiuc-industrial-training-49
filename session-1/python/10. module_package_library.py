# Python Modules, Packages, Libraries, and Pip: In-Depth Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides an in-depth guide to understanding modules, packages, libraries, and the use of pip in Python.
We will explore:
1. What are modules, packages, and libraries?
2. How to create and use them.
3. Introduction to pip and how to use it to manage Python packages.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Modules
# ------------------
# A module in Python is a file containing Python definitions and statements. The file name is the module name with the suffix '.py'.

# Example 1: Creating and using a module
# Suppose we have a module named `mymodule.py` with a function `greet()` defined in it.
# mymodule.py content:
# def greet(name):
#     print(f"Hello, {name}!")

# To use this module, we would import it in another Python script:
# import mymodule
# mymodule.greet("Alice")

print("Module example: See comments for usage.")

# Section 2: Packages
# -------------------
# A package is a collection of Python modules under a common namespace. In most cases, a package is a directory containing a special `__init__.py` file.

# Example 2: Creating and using a package
# Suppose we have a package directory `mypackage` with an `__init__.py` file and another module `submodule.py`.
# mypackage/
#     __init__.py
#     submodule.py
# submodule.py content:
# def hello():
#     print("Hello from submodule!")

# To use this package, you would import the submodule:
# from mypackage import submodule
# submodule.hello()

print("Package example: See comments for usage.")

# Section 3: Libraries
# --------------------
# A library in Python is a collection of modules and packages aimed at solving particular problems or carrying out specific tasks.

# Example 3: Using a library
# One of the most popular libraries in Python is `requests` for making HTTP requests.
# import requests
# response = requests.get('https://api.github.com')
# print(response.status_code)

print("Library example: See comments for usage.")

# Section 4: Pip and Package Management
# -------------------------------------
# `pip` is the package installer for Python. You can use it to install packages from the Python Package Index (PyPI) and other indexes.

# Example 4: Using pip to install a package
# To install the `requests` library, you would typically run the following command in your terminal:
# pip install requests

# Example 5: Listing installed packages
# To see what packages are installed in your environment, you can use:
# pip list

# Example 6: Uninstalling a package
# To uninstall a package, use:
# pip uninstall requests

print("Pip examples: See comments for usage.")

# Assignments
# -----------
# Assignment 1: Create a simple package with at least two modules, each containing one function.
# Assignment 2: Use pip to install any library that is new to you and write a small script to explore its functionality.

# Congratulations on completing the comprehensive section on Python's modules, packages, libraries, and pip!
# Review the assignments, try to solve them, and check your understanding of these essential Python features.
