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

def create_admin_table(connection):
    try:
        cursor = connection.cursor()
        create_table_query = ("CREATE TABLE IF NOT EXISTS admin_id (ID INT AUTO_INCREMENT PRIMARY KEY, First_Name VARCHAR(255) NOT NULL, Last_Name VARCHAR(255) NOT NULL, MES_ID VARCHAR(255) NOT NULL UNIQUE, DOB DATE NOT NULL, Phone_Number VARCHAR(15) NOT NULL, Password VARCHAR(255) NOT NULL)")
        cursor.execute(create_table_query)
        print("Admin table 'admin_id' created successfully.")
    except mysql.connector.Error as e:
        print("Error creating admin table:", e)

def register_admin(connection, first_name, last_name, mes_id, dob, phone_number, password):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO admin_id (First_Name, Last_Name, MES_ID, DOB, Phone_Number, Password) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (first_name, last_name, mes_id, dob, phone_number, password)
        cursor.execute(insert_query, data)
        connection.commit()
        print("Admin registration successful!")
    except mysql.connector.Error as e:
        print("Error inserting data into MySQL:", e)

def main():
    connection = create_connection()
    if connection is None:
        return

    create_admin_table(connection)  # Create the admin table if it doesn't exist

    print("Welcome to the Admin Registration Page")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    mes_id = input("Enter MES ID: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    phone_number = input("Enter Phone Number: ")
    password = input("Enter Password: ")

    register_admin(connection, first_name, last_name, mes_id, dob, phone_number, password)

    connection.close()
    print("MySQL connection is closed.")

if __name__ == "__main__":
    main()
