import mysql.connector
#from capture import capture_and_save_image
import re
import datetime
# from face_detector import get_face_detector
from face_reg import perform_face_detection
# from face_landmarks import get_landmark_model

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

def validate_admission_number(admission_number):
    pattern = r"^\d{4}PE\d{4}$"
    return re.match(pattern, admission_number) is not None

def validate_mes_id(mes_id):
    pattern = r"^\w+@student\.mes\.ac\.in$"
    return re.match(pattern, mes_id) is not None

def validate_year(year):
    return year in ["FE", "SE", "TE", "BE"]

def validate_department(department):
    return department in ["IT", "CS", "ECS", "EXTC", "MECH", "AUTO"]

def validate_dob(dob):
    try:
        # Parse the date string and validate the format
        datetime.datetime.strptime(dob, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_phone_number(phone_number):
    return re.match(r"^\d{10}$", phone_number) is not None

def create_student_table(connection):
    try:
        cursor = connection.cursor()
        create_table_query = ("CREATE TABLE IF NOT EXISTS student_id (ID INT AUTO_INCREMENT PRIMARY KEY, Admission_Number VARCHAR(10) NOT NULL UNIQUE, First_Name VARCHAR(255) NOT NULL, Last_Name VARCHAR(255) NOT NULL, MES_ID VARCHAR(255) NOT NULL UNIQUE, Year VARCHAR(255) NOT NULL, Department VARCHAR(255) NOT NULL, DOB DATE NOT NULL, Phone_Number VARCHAR(15) NOT NULL, Password VARCHAR(255) NOT NULL, user_image VARCHAR(255) NOT NULL)")
        cursor.execute(create_table_query)
        #print("Student table 'student_id' created successfully.")
    except mysql.connector.Error as e:
        print("Error creating student table:", e)

def register_student(connection, admission_number, first_name, last_name, mes_id, year, department, dob, phone_number, password, user_image):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO student_id (Admission_Number, First_Name, Last_Name, MES_ID, Year, Department, DOB, Phone_Number, Password, user_image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (admission_number, first_name, last_name, mes_id, year, department, dob, phone_number, password, user_image)
        cursor.execute(insert_query, data)
        connection.commit()
        print("Student registration successful!")
    except mysql.connector.Error as e:
        print("Error inserting data into MySQL:", e)

def main():
    connection = create_connection()
    if connection is None:
        return

    create_student_table(connection)  # Create the admin table if it doesn't exist

    print("Welcome to the Student Registration Page")

    # Load the face detection model
    # face_model = get_face_detector()

    # Load the facial landmark model
    # landmark_model = get_landmark_model()

    while True:
        admission_number = input("Enter Admission Number (e.g., 2020PE0001): ")
        if validate_admission_number(admission_number):
            break
        else:
            print("Invalid admission number format. Please try again.")
    
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")

    while True:
        mes_id = input("Enter MES ID (e.g., xyz@student.mes.ac.in): ")
        if validate_mes_id(mes_id):
            break
        else:
            print("Invalid MES ID format. Please try again.")

    while True:
        year = input("Enter Year (FE, SE, TE, BE): ")
        if validate_year(year):
            break
        else:
            print("Invalid year. Please enter FE, SE, TE, or BE.")

    while True:
        department = input("Enter Department (IT, CS, ECS, EXTC, MECH, AUTO): ")
        if validate_department(department):
            break
        else:
            print("Invalid department. Please enter a valid department.")

    while True:
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        if validate_dob(dob):
            break
        else:
            print("Invalid date of birth format. Please try again.")

    while True:
        phone_number = input("Enter Phone Number (10 digits only): ")
        if validate_phone_number(phone_number):
            break
        else:
            print("Invalid phone number format. Please try again.")
    password = input("Enter Password: ")

    input("Press Enter to capture your profile picture")

    user_image = perform_face_detection(admission_number)
    print(admission_number)
    print(user_image)

    register_student(connection, admission_number, first_name, last_name, mes_id, year, department, dob, phone_number, password, user_image)

    

    connection.close()
    print("MySQL connection is closed.")


if __name__ == "__main__":
    main()