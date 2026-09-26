from db_utils import get_connection
import mysql.connector

#returns all films in films table
def get_all_films():
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True) #returns as dictionary for easier jsonify in app.py
        cursor.execute("SELECT * FROM films")
        films = cursor.fetchall()
        return films
    except mysql.connector.Error as err:
        print((f"Error: {err}"))
        return None #so that app.py treats it as an error
    finally:
        if cursor:
            cursor.close()
            print("Cursor closed")
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed")

#for identifying film with entered id
def get_film_by_id(film_id):
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True) 
        cursor.execute("SELECT * FROM films WHERE film_id = %s",(film_id,))
        film = cursor.fetchone()
        return film
    except mysql.connector.Error as err:
        print((f"Error: {err}"))
        return None 
    finally:
        if cursor:
            cursor.close()
            print("Cursor closed")
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed")

#for adding a film into the films table
def insert_film(title, release_year, genre, director, IMDB_rating, runtime, age_rating):
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        query ="""INSERT INTO films (title, release_year, genre, director, IMDB_rating, runtime, age_rating) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,(title, release_year, genre, director, IMDB_rating, runtime, age_rating))
        connection.commit()
        return (True, cursor.lastrowid) #returns true if insert worked, with last row id for user
    except mysql.connector.Error as err:
        print((f"Error: {err}"))
        return False 
    finally:
        if cursor:
            cursor.close()
            print("Cursor closed")
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed")

#picks a random film for user, can choose a genre if they wish
def surprise_me(genre=None): 
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        if genre is None: #if user has no preference, then a film w any genre is returned
            query = f"""SELECT * FROM films
                        ORDER BY RAND()
                        LIMIT 1"""
            cursor.execute(query)
        else: #otherwise genre is specified in result
            query = f"""SELECT * FROM films
                        WHERE genre LIKE %s
                        ORDER BY RAND()
                        LIMIT 1"""
            cursor.execute(query, (f"%{genre}%",))
        choice = cursor.fetchone()
        return choice
    except mysql.connector.Error as err:
        print((f"Error: {err}"))
        return None 
    finally:
        if cursor:
            cursor.close()
            print("Cursor closed")
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed")