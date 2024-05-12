"""
Author: Kalim Amzad
Version: 1.0

This module demonstrates the usage of the `requests-html` library in Python for web scraping.
It covers various real-world examples including rendering JavaScript, extracting data, and
working with HTML elements. This script is designed as an educational tool for understanding
web scraping using Python.

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
        title_tag = response.html.find('h1')
        print(len(title_tag), "title tags found:")
        print("Title: ", title_tag[0].text)

        datetime_element = response.html.find('time', first=True)
        datetime = datetime_element.attrs['datetime']
        print("Datetime attribute: ", datetime)

        # advanced usages of extraction
        temp = response.html.xpath('div.time-social-share-wrapper > div > time', first=True)
        print(temp)
        datetime = temp.attrs['datetime']
        print(datetime)



        # Example: Extracting all links
        # links = response.html.find('a')
        # print(len(links), "links found:")

        # for link in links:
        #     print("Link Text: ", link.text, "Link href: ", link.attrs['href'])
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def main():
    """
    Main function to execute the web scraping examples.
    """
    # print("Rendering JavaScript on a web page...")
    # render_javascript('https://example.com')

    print("\nExtracting information from a web page...")
    extract_information('https://www.prothomalo.com/world/usa/xnjy4uqwpv')

if __name__ == "__main__":
    main()
