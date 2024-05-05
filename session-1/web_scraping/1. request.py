"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com
Version: 1.0

This module demonstrates the usage of the `requests` library in Python for making HTTP requests.
It covers various real-world examples including GET and POST requests, handling response data,
and working with headers and parameters. This script is designed as an educational tool for
understanding web scraping and API interaction using Python.
"""

import requests

def get_example():
    """
    Demonstrates a simple GET request using the `requests` library.
    Fetches data from a public API and prints the JSON response.
    """
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("GET request successful!")
        # Print response content
        print(response.json())
    else:
        print("Failed to retrieve data")

def post_example():
    """
    Demonstrates a simple POST request using the `requests` library.
    Sends JSON data to a public API and prints the response.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    response = requests.post(url, json=data)
    
    # Check if the request was successful
    if response.status_code == 201:
        print("POST request successful!")
        # Print response content
        print(response.json())
    else:
        print("Failed to post data")

def main():
    """
    Main function to execute the examples.
    """
    print("Executing GET example...")
    get_example()
    print("\nExecuting POST example...")
    post_example()

if __name__ == "__main__":
    main()



# Assignments
# 1. Modify the GET Example: Change the get_example function to fetch a list of posts instead of just one. Analyze the JSON structure and print out the titles of all posts.

# 2. Error Handling: Add error handling to both functions to manage exceptions like connection errors or timeouts.

# 3. Headers and Authentication: Modify the post_example function to include custom headers.



# Advanced requests
"""
This module discuss advanced features like custom headers, user agents, and error handling.


Custom Headers and User Agents: These are used to provide additional information to the server about the request being made. For example, the 
`User-Agent` header can be used to simulate requests from different browsers.

Error Handling: The `try-except` blocks are used to catch and handle different types of exceptions that might occur during the request, such as network problems or invalid responses.
"""

import requests

def get_with_headers():
    """
    Demonstrates a GET request with custom headers and a user agent.
    Fetches data from a public API and prints the JSON response.
    """
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        print("GET request with custom headers successful!")
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

def post_with_authentication():
    """
    Demonstrates a POST request using basic authentication.
    Sends JSON data to a public API and prints the response.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    auth = ('user', 'pass')  # Replace with actual username and password
    
    try:
        response = requests.post(url, json=data, headers=headers, auth=auth)
        response.raise_for_status()
        print("POST request with authentication successful!")
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

def main():
    """
    Main function to execute advanced examples.
    """
    print("Executing GET example...")
    get_example()
    print("\nExecuting POST example...")
    post_example()

    # Advanced usages
    print("Executing GET request with custom headers...")
    get_with_headers()
    print("\nExecuting POST request with authentication...")
    post_with_authentication()

if __name__ == "__main__":
    main()


