"""
requests_html_tutorial.py
~~~~~~~~~~~~~~~~~~~~~~~~~

This module demonstrates the usage of the `requests-html` library in Python for web scraping.
It covers various real-world examples including rendering JavaScript, extracting data, and
working with HTML elements. This script is designed as an educational tool for understanding
web scraping using Python.

Author: [Your Name]
Version: 1.0
"""

from requests_html import HTMLSession

def render_javascript(url):
    """
    Demonstrates how to render JavaScript using the `requests-html` library.
    This function fetches the page content after JavaScript has been executed.

    Parameters:
    url : str
        The URL of the website to scrape.

    Returns:
    None
    """
    session = HTMLSession()
    try:
        response = session.get(url)
        response.html.render()  # This will download Chromium if not found
        print("Rendered web page:", response.html.html)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def extract_information(url):
    """
    Extracts and prints specific information from a webpage using CSS selectors.

    Parameters:
    url : str
        The URL of the website to scrape.

    Returns:
    None
    """
    session = HTMLSession()
    try:
        response = session.get(url)
        # Example: Extracting all links
        links = response.html.find('a')
        for link in links:
            print(link.text, link.attrs['href'])
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def main():
    """
    Main function to execute the web scraping examples.
    """
    print("Rendering JavaScript on a web page...")
    render_javascript('https://example.com')

    print("\nExtracting information from a web page...")
    extract_information('https://example.com')

if __name__ == "__main__":
    main()
