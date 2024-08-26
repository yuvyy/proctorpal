import mysql.connector

def create_connection():
    # Replace these with your MySQL server credentials
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

def authenticate_user(connection, mes_id, password):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM student_id WHERE mes_id = %s AND password = %s"
        cursor.execute(query, (mes_id, password))
        user = cursor.fetchone()
        if user:
            return user
        else:
            return None
    except mysql.connector.Error as e:
        print("Error executing MySQL query:", e)
        return None

def main():
    connection = create_connection()
    if connection is None:
        return

    print("Welcome to the Student Login Page")
    mes_id = input("Enter your MES ID: ")
    password = input("Enter your password: ")

    user = authenticate_user(connection, mes_id, password)
    if user:
        print("Login successful!")
        print("Name:", user[2])  # Assuming the name is the second column in the Registration table
    else:
        print("Login failed. Invalid MES ID or password.")

    connection.close()
    print("MySQL connection is closed.")

if __name__ == "__main__":
    main()
