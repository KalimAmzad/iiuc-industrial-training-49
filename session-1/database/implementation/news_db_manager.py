import os
import mysql.connector
from mysql.connector import Error
from db_connection import create_db_connection

def execute_query(connection, query):
    """
    Execute a given SQL query on the provided database connection.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    query : str
        The SQL query to execute.

    Returns
    -------
    None
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    """
    Execute a read query and return the results.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    query : str
        The SQL query to execute.

    Returns
    -------
    list
        A list of tuples containing the rows returned by the query.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return []

def create_tables(connection):
    """
    Create tables in the database based on the predefined schema.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.

    Returns
    -------
    None
    """
    create_categories_table = """
    CREATE TABLE IF NOT EXISTS categories (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT
    );
    """
    create_authors_table = """
    CREATE TABLE IF NOT EXISTS authors (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL
    );
    """
    create_editors_table = """
    CREATE TABLE IF NOT EXISTS editors (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL
    );
    """
    create_news_table = """
    CREATE TABLE IF NOT EXISTS news (
        id INT AUTO_INCREMENT PRIMARY KEY,
        category_id INT,
        author_id INT,
        editor_id INT,
        datetime DATETIME,
        title VARCHAR(255) NOT NULL,
        body TEXT,
        link VARCHAR(255),
        FOREIGN KEY (category_id) REFERENCES categories (id),
        FOREIGN KEY (author_id) REFERENCES authors (id),
        FOREIGN KEY (editor_id) REFERENCES editors (id)
    );
    """
    create_images_table = """
    CREATE TABLE IF NOT EXISTS images (
        id INT AUTO_INCREMENT PRIMARY KEY,
        news_id INT,
        image_url VARCHAR(255),
        FOREIGN KEY (news_id) REFERENCES news (id)
    );
    """
    create_summaries_table = """
    CREATE TABLE IF NOT EXISTS summaries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        news_id INT,
        summary_text TEXT,
        FOREIGN KEY (news_id) REFERENCES news (id)
    );
    """
    execute_query(connection, create_categories_table)
    execute_query(connection, create_authors_table)
    execute_query(connection, create_editors_table)
    execute_query(connection, create_news_table)
    execute_query(connection, create_images_table)
    execute_query(connection, create_summaries_table)


# Example usage
if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:
        # create_tables(conn)
        # read_categories_query = "SELECT * FROM categories;"
        # news_categories = execute_read_query(conn, read_categories_query)
        # print(news_categories)

        read_authors_query = "SELECT * FROM authors;"
        news_authors = execute_read_query(conn, read_authors_query)
        print(news_authors)

