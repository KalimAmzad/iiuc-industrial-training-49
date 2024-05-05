from requests_html import HTMLSession

def single_news(url):
    session = HTMLSession()
    try:
        response = session.get(url)
        # response.html.render()  # This will download Chromium if not found

        # print(response.html.html)
        title = response.html.find('h1', first=True).text
        print(title)
        # Example: Extracting all links
        links = response.html.find('a')
        for link in links:
            print(link)
            # print(link.text, link.attrs['href'])
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()


single_news("https://www.prothomalo.com/bangladesh/capital/p8r7ejhfel")
