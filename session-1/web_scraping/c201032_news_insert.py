import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_db_connection():
    """
    Create a database connection to the MySQL database specified by the db_name.

    Returns
    -------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        print("MySQL Database connection successful by - C201032, Sorowar Mahabub!!")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def execute_query(connection, query, data=None):
    """
    Execute a given SQL query on the provided database connection.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    query : str
        The SQL query to execute.
    data : tuple, optional
        The data tuple to pass to the query, for parameterized queries.

    Returns
    -------
    Id of last inserted row : int
    """
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query successful!")
        return cursor.lastrowid
    except Error as e:
        print(f"The error '{e}' occurred")
 
    
def insert_category(connection, name, description):
    """
    Inserts a new category into the categories table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the category.
    description : str
        The description of the category.

    Returns
    -------
    Category ID : int
    """
    query = """
    INSERT INTO categories (name, description)
    VALUES (%s, %s)
    """
    data = (name, description)
    
    # cursor =  connection.cursor()  # Create a new cursor object    
    # cursor.execute(query, data)  # Use the cursor to execute the query
    # connection.commit()  # Commit the transaction
    
    # return cursor.lastrowid  # Return the ID of the last inserted row
    cursor = execute_query(connection, query, data)
    return cursor  # Return the ID of the inserted category

def insert_reporter(connection, name, email):
    """
    Inserts a new reporter into the reporters table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the reporter.
    email : str
        The email of the reporter.

    Returns
    -------
    Reorter ID : int
    """
    query = """
    INSERT INTO repoters (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    
    # cursor = connection.cursor()  # Create a new cursor object
    # cursor.execute(query, data)  # Use the cursor to execute the query
    # connection.commit()  # Commit the transaction
    
    # return cursor.lastrowid  # Return the ID of the last inserted row
    cursor = execute_query(connection, query, data)
    if cursor is None:
        print("Failed to execute query!!")
        return None
    return cursor # Return the ID of the inserted reporter

def insert_publisher(connection, name, email, phone_number, head_office_address, website, facebook, twitter, linkedin, instagram):
    """
    Inserts a new publisher into the publishers table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the publisher.
    email : str
        The email of the publisher.

    Returns
    -------
    Publisher ID : int
    """
    query = """
    INSERT INTO publishers (name, email, phone_number, head_office_address, website, facebook, twitter, linkedin, instagram)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (name, email, phone_number, head_office_address, website, facebook, twitter, linkedin, instagram)
    
    # cursor = connection.cursor()  # Create a new cursor object
    # cursor.execute(query, data)  # Use the cursor to execute the query
    # connection.commit()  # Commit the transaction
    
    # return cursor.lastrowid  # Return the ID of the last inserted row
    cursor = execute_query(connection, query, data)
    if cursor is None:
        print("Failed to execute query!!")
        return None
    return cursor # Return the ID of the inserted publisher

def insert_news(connection, category_id, reporter_id, publisher_id, datetime, title, body, link):
    """
    Inserts a new news article into the news table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    category_id : int
        The ID of the category.
    reporter_id : int
        The ID of the reporter.
    publisher_id : int
        The ID of the publisher.
    datetime : datetime
        The publication date and time of the news article.
    title : str
        The title of the news article.
    body : str
        The body text of the news article.
    link : str
        The URL link to the full news article.

    Returns
    -------
    News ID : int
    """
    query = """
    INSERT INTO news (category_id, reporter_id, publisher_id, datetime, title, body, link)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (category_id, reporter_id, publisher_id, datetime, title, body, link)
    
    # cursor = connection.cursor()  # Create a new cursor object
    # cursor.execute(query, data)  # Use the cursor to execute the query
    # connection.commit()  # Commit the transaction
    
    # return cursor.lastrowid  # Return the ID of the last inserted row
    cursor = execute_query(connection, query, data)
    if cursor is None:
        print("Failed to execute query!!")
        return None
    return cursor  # Return the ID of the last inserted row

def insert_image(connection, news_id, image_url):
    """
    Inserts a new image into the images table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    news_id : int
        The ID of the news article associated with the image.
    image_url : str
        The URL of the image.

    Returns
    -------
    Image ID : int
    """
    query = """
    INSERT INTO images (news_id, image_url)
    VALUES (%s, %s)
    """
    data = (news_id, image_url)
    
    # cursor = connection.cursor()  # Create a new cursor object
    # cursor.execute(query, data)  # Use the cursor to execute the query
    # connection.commit()  # Commit the transaction
    
    # return cursor.lastrowid  # Return the ID of the last inserted row
    cursor = execute_query(connection, query, data)
    if cursor is None:
        print("Failed to execute query")
        return None
    return cursor # Return the ID of the last inserted row

def insert_summary(connection, news_id, summary_text):
    """
    Inserts a new summary into the summaries table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    news_id : int
        The ID of the news article associated with the summary.
    summary_text : str
        The text of the summary.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO summaries (news_id, summary_text)
    VALUES (%s, %s)
    """
    data = (news_id, summary_text)
    execute_query(connection, query, data)

# Example usage
if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:
        # Insert categories
        insert_category(conn, "Politics", "All news related to politics")
        # insert_category(conn, "Sports", "All news related to sports")
        # insert_category(conn, "Entertainment", "All news related to entertainment")
        # insert_category(conn, "Technology", "All news related to technology")
        # insert_category(conn, "Business", "All news related to business")
        
        # Insert reporters
        insert_reporter(conn, "Sorowar", "sorowar@ugrad.iiuc.ac.bd")
        # insert_reporter(conn, "Munna", "munna@ugrad.iiuc.ac.bd")
        # insert_reporter(conn, "Rahim", "rahim@ugrad.iiuc.ac.bd")
        # insert_reporter(conn, "Karim", "karim@ugrad.iiuc.ac.bd")
        # insert_reporter(conn, "Dipto", "dipto@ugrad.iiuc.ac.bd")
        
        # Insert publishers
        insert_publisher(conn, "BBC", "bbc@ugrad.iiuc.ac.bd", 1234567890, "Dhaka, Bangladesh", "bbc.com", "facebook.com/bbc", "twitter.com/bbc", "linkedin.com/bbc","instagram.com/bbc")
        # insert_publisher(conn, "IIUC", "iiuc@ugrad.iiuc.ac.bd", 5678901234, "Dhaka, Bangladesh", "iiuc.ac.bd", "facebook.com/iiuc", "twitter.com/iiuc", "linkedin.com/iiuc", "instagram.com/iiuc")
        # insert_publisher(conn, "Prothom Alo", "p_alo@gmail.com", 1234567890, "Dhaka, Bangladesh", "prothomalo.com", "facebook.com/prothomalo", "twitter.com/prothomalo", "linkedin.com/prothomalo", "instagram.com/prothomalo")
        # insert_publisher(conn, "Daily Star", "d_star@gmail.com", 1234567890, "Dhaka, Bangladesh", "dailystar.com.bd", "facebook.com/dailystar", "twitter.com/dailystar", "linkedin.com/dailystar", "instagram.com/dailystar")
        # insert_publisher(conn, "CNN", "cnn@ugrad.iiuc.ac.bd", 1234567890, "Dhaka, Bangladesh", "cnn.com", "facebook.com/cnn", "twitter.com/cnn", "linkedin.com/cnn", "instagram.com/cnn")
        
        # Insert news articles
        insert_news(conn, 1, 1, 1, "2022-01-01 00:00:00", "Test News Article 1", "This is the body of the first news article.", "https://example.com/news-article-1")
        # insert_news(conn, 2, 2, 2, "2022-01-02 00:00:00", "Test News Article 2", "This is the body of the second news article.", "https://example.com/news-article-2")
        # insert_news(conn, 3, 3, 3, "2022-01-03 00:00:00", "Test News Article 3", "This is the body of the third news article.", "https://example.com/news-article-3")
        # insert_news(conn, 4, 4, 4, "2022-01-04 00:00:00", "Test News Article 4", "This is the body of the fourth news article.", "https://example.com/news-article-4")
        # insert_news(conn, 5, 5, 5, "2022-01-05 00:00:00", "Test News Article 5", "This is the body of the fifth news article.", "https://example.com/news-article-5")
        
        # Insert images
        insert_image(conn, 1, "https://upload.wikimedia.org/wikipedia/commons/0/09/INews.png")
        # insert_image(conn, 2, "https://upload.wikimedia.org/wikipedia/commons/0/09/INews.png")
        # insert_image(conn, 3, "https://upload.wikimedia.org/wikipedia/commons/0/09/INews.png")
        # insert_image(conn, 4, "https://upload.wikimedia.org/wikipedia/commons/0/09/INews.png")
        # insert_image(conn, 5, "https://upload.wikimedia.org/wikipedia/commons/0/09/INews.png")
        
        conn.commit()
        conn.close()
        print("Database created successfully by - Sorowar Mahabub, C201032!")