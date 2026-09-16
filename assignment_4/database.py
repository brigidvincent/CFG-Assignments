import mysql.connector
from db_utils import get_connection

#this file is for the set up of my database, tables, and values within

def create_entertainment_database():
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS entertainment_db")
        connection.commit()
        print("Database created")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
    finally:
        if cursor:
            cursor.close()
            print("cursor closed")
        if connection and connection.is_connected():
            connection.close()
            print("Database closed")

#keeping these functions seperate so that tables can be altered in future
#made a tables dictionary so in future can add more tables to be created 

def create_tables():
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        tables = {
            "films" : """
                CREATE TABLE IF NOT EXISTS films (
                film_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) UNIQUE NOT NULL,
                release_year INT,
                genre VARCHAR(100),
                director VARCHAR(255),
                IMDB_rating DECIMAL(2,1),
                runtime INT,
                age_rating VARCHAR(5)
                )""" #age rating can be PG or 12A so have left this as VARCHAR instead of INT
        }
        cursor.execute("""USE entertainment_db""")
        for table_name, query in tables.items():
            cursor.execute(query)
            print(f"Table {table_name} created successfully")
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        if cursor:
            cursor.close()
            print("cursor closed")
        if connection and connection.is_connected():
            connection.close()
            print("connection closed")

#used chatgpt to give me details of a few films + tv shows for values in my database
def insert_films():
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""USE entertainment_db""")
        query ="""INSERT INTO films (title, release_year, genre, director, IMDB_rating, runtime, age_rating) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        film_values = [
    (
        "The Grand Budapest Hotel",
        2014,
        "Comedy",
        "Wes Anderson",
        8.1,
        99,
        15
    ),
    (
        "The Gentlemen",
        2019,
        "Comedy/Crime",
        "Guy Ritchie",
        7.8,
        113,
        18
    ),
    (
        "Knives Out",
        2019,
        "Mystery/Comedy",
        "Rian Johnson",
        7.9,
        130,
        12
    ),
    (
        "The Dark Knight",
        2008,
        "Action/Crime",
        "Christopher Nolan",
        9.0,
        152,
        12
    ),
    (
        "Hot Fuzz",
        2007,
        "Action/Comedy",
        "Edgar Wright",
        7.8,
        121,
        15
    ),
    (
        "The Nice Guys",
        2016,
        "Action/Comedy",
        "Shane Black",
        7.4,
        116,
        15
    ),
    (
        "10 Things I Hate About You",
        1999,
        "Romance/Comedy",
        "Gil Junger",
        7.4,
        97,
        12
    ),
    (
        "Crazy Rich Asians",
        2018,
        "Romance/Comedy",
        "Jon M. Chu",
        6.9,
        120,
        12
    ),
    (
        "The Shawshank Redemption",
        1994,
        "Drama",
        "Frank Darabont",
        9.3,
        142,
        15
    ),
    (
        "Interstellar",
        2014,
        "Sci-Fi/Drama",
        "Christopher Nolan",
        8.7,
        169,
        12
    ),
    (
        "The Martian",
        2015,
        "Sci-Fi/Comedy",
        "Ridley Scott",
        8.0,
        144,
        12
    ),
    (
        "Ocean's Eleven",
        2001,
        "Crime/Comedy",
        "Steven Soderbergh",
        7.7,
        116,
        12
    ),
    (
        "The Notebook",
        2004,
        "Romance/Drama",
        "Nick Cassavetes",
        7.8,
        123,
        12
    ),
    (
        "Get Out",
        2017,
        "Horror/Thriller",
        "Jordan Peele",
        7.8,
        104,
        15
    ),
    (
        "The Hangover",
        2009,
        "Comedy",
        "Todd Phillips",
        7.7,
        100,
        15
    )]
        cursor.executemany(query,film_values)
        connection.commit()
        print("records inserted into films")
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        if cursor:
            cursor.close()
            print("cursor closed")
        if connection and connection.is_connected():
            connection.close()
            print("connection closed")

#a function for initial database set up - only need to run this file once at the start
def setup_database():
    create_entertainment_database()
    create_tables()
    insert_films()

if __name__ == "__main__":
    setup_database()
 #after running, update env file for database name (uncomment it)