
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
        print("MySQL Database connection successful! Done by- Sorowar Mahabub, C201032!")
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

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
        print(f"The error '{e}' occurred!")
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
    create_repoters_table = """
    CREATE TABLE IF NOT EXISTS repoters (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL
    );
    """
    create_publishers_table = """
    CREATE TABLE IF NOT EXISTS publishers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        phone_number VARCHAR(255) NOT NULL,
        head_office_address VARCHAR(255) NOT NULL,
        website VARCHAR(255) NOT NULL,
        facebook VARCHAR(255) NOT NULL,
        twitter VARCHAR(255)NOT NULL,
        linkedin VARCHAR(255)NOT NULL,
        instagram VARCHAR(255) NOT NULL
    );
    """
    
    create_news_table = """
    CREATE TABLE IF NOT EXISTS news (
        id INT AUTO_INCREMENT PRIMARY KEY,
        category_id INT,
        reporter_id INT,
        publisher_id INT,
        datetime DATETIME,
        title VARCHAR(255) NOT NULL,
        body TEXT,
        link VARCHAR(255),
        FOREIGN KEY (category_id) REFERENCES categories (id),
        FOREIGN KEY (reporter_id) REFERENCES repoters (id),
        FOREIGN KEY (publisher_id) REFERENCES publishers (id)
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
    execute_query(connection, create_repoters_table)
    execute_query(connection, create_publishers_table)
    execute_query(connection, create_news_table)
    execute_query(connection, create_images_table)
    execute_query(connection, create_summaries_table)


# Example usage
if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:
        create_tables(conn)
        
        read_categories_query = "SELECT * FROM categories"
        news_categories = execute_read_query(conn, read_categories_query)
        print(news_categories)

        read_repoters_query = "SELECT * FROM repoters"
        news_repoters = execute_read_query(conn, read_repoters_query)
        print(news_repoters)
        
        read_publishers_query = "SELECT * FROM publishers"
        news_publishers = execute_read_query(conn, read_publishers_query)
        print(news_publishers)
        
        read_news_query = "SELECT * FROM news"
        news = execute_read_query(conn, read_news_query)
        print(news)
        
        read_images_query = "SELECT * FROM images"
        news_images = execute_read_query(conn, read_images_query)
        print(news_images)

