import mysql.connector
from config import db_config

def get_connection(): #to connect to database throughout
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        if connection and connection.is_connected():
            print("Connected to database")
            return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")

