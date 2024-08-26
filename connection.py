import mysql.connector

def create_connection():
    host = "localhost"
    username = "root"
    password = "kl!nEfeltEr38"
    database_name = "db9"

    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database_name
        )
        if connection.is_connected():
            return connection
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None