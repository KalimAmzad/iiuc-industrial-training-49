import time
import datetime
from requests_html import HTMLSession
from mysql.connector import Error
from db_connection import create_db_connection
from news_insert_modified import (execute_query,
                                insert_reporter, 
                                insert_category, 
                                insert_news,
                                insert_publisher,
                                insert_image)


def process_and_insert_news_data(connection, publisher_website, publisher, title, reporter, news_datetime, category, images, url):
    """
    Processes and inserts news scraping data into the database.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    publisher_website : str
        The website of the publisher.
    publisher : str
        The name of the publisher.
    title : str
        The title of the news article.
    reporter : str
        The name of the reporter.
    datetime : datetime
        The publication date and time of the news article.
    category : str
        The category of the news article.
    images : list of str
        A list of image URLs associated with the news article.

    Returns
    -------
    None
    """
    try:
        # Insert category if not exists
        category_id = insert_category(connection, category, f"{category} af description")
        
        # Insert reporter if not exists
        reporter_id = insert_reporter(connection, reporter, f"{reporter}@hfg.com")
        
        # Insert publisher as a placeholder (assuming publisher is not provided)
        publisher_id = insert_publisher(connection, publisher, f"{publisher}@ghjey.com")
        
        # Insert news article
        news_id = insert_news(connection, category_id, reporter_id, publisher_id, news_datetime, title, news_body, url)
        
        # Insert images
        for image_url in images:
            image_id = insert_image(connection, news_id, image_url)
    
    except Error as e:
        print(f"Error while processing news data - {e}")


def single_news_scraper(url):
    session = HTMLSession()
    try:
        response = session.get(url)
        response.html.render()  # This will download Chromium if not found
        # time.sleep(3)

        # print(response.html.html)
        publisher_website = url.split('/')[2]       
        publisher = publisher_website.split('.')[-2]  

        title = response.html.find('h1', first=True).text
        reporter = response.html.find('.contributor-name', first=True).text
        # reporter_location = response.html.find('.author-location', first=True).text
        datetime_element = response.html.find('time', first=True)
        news_datetime = datetime_element.attrs['datetime']
        category = response.html.find('.print-entity-section-wrapper', first=True).text

        news_body = '\n'.join([p.text for p in response.html.find('p')])
        # news_body = []
        # all_p = response.html.find('p')
        # for p in all_p:
        #     # print(p.text)
        #     news_body.append(p.text)
        # news_body = '\n'.join(news_body)

        img_tags = response.html.find('img')
        images = [img.attrs['src'] for img in img_tags if 'src' in img.attrs]
        # images = []
        # for img_tag in img_tags:
        #     if img_tag:
        #         img_url = img_tag.attrs['src']
        #         images.append(img_url)
        #         # print(f"Image URL: {img_url}")
        #     else:
        #         print("No image tag found.")
        
        print(publisher_website, publisher, title, reporter, news_datetime, category, images)
        # process_and_insert_news_data(conn, publisher_website, publisher, title, reporter, reporter_location, datetime, category, images)
        return publisher_website, publisher, title, reporter, news_datetime, category, news_body, images
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

# url = "https://www.prothomalo.com/bangladesh/k4fpzemipc"
# publisher_website, publisher, title, reporter, news_datetime, category, news_body, images = single_news_scraper(url)
# print(publisher, title, reporter, news_datetime, category, images)

# Example usage
if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:
        main_link = "https://www.prothomalo.com/bangladesh/capital"
        # collect all news link and process the link
        session = HTMLSession()
        main_response = session.get(main_link)
        all_news_links = main_response.html.find('a')
        for news_link in all_news_links:
            
            # url = "https://www.prothomalo.com/bangladesh/district/l9iivxgmt0"
            publisher_website, publisher, title, reporter, news_datetime, category, news_body, images = single_news_scraper(news_link)
            print(publisher, title, reporter, news_datetime, category, images)
            process_and_insert_news_data(conn, publisher_website, publisher, title, reporter, news_datetime, category, images, news_link)
