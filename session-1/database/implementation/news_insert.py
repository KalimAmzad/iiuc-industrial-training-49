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
        print("MySQL Database connection successful")
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
    None
    """
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query successful")
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
    None
    """
    query = """
    INSERT INTO categories (name, description)
    VALUES (%s, %s)
    """
    data = (name, description)
    execute_query(connection, query, data)

def insert_author(connection, name, email):
    """
    Inserts a new author into the authors table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the author.
    email : str
        The email of the author.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO authors (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    execute_query(connection, query, data)

def insert_editor(connection, name, email):
    """
    Inserts a new editor into the editors table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the editor.
    email : str
        The email of the editor.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO editors (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    execute_query(connection, query, data)

def insert_news(connection, category_id, author_id, editor_id, datetime, title, body, link):
    """
    Inserts a new news article into the news table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    category_id : int
        The ID of the category.
    author_id : int
        The ID of the author.
    editor_id : int
        The ID of the editor.
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
    None
    """
    query = """
    INSERT INTO news (category_id, author_id, editor_id, datetime, title, body, link)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (category_id, author_id, editor_id, datetime, title, body, link)
    execute_query(connection, query, data)

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
    None
    """
    query = """
    INSERT INTO images (news_id, image_url)
    VALUES (%s, %s)
    """
    data = (news_id, image_url)
    execute_query(connection, query, data)

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
        insert_category(conn, "Politics", "All news related to politics")
        insert_author(conn, "John Doe", "test@example.com")
        # Add more insert calls for other tables
