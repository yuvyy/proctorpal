import mysql.connector
import hashlib
import string
import random
import re
from datetime import datetime
# Replace with your MySQL server credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "kl!nEfeltEr38",
    "database": "TESTDB"
}

# Function to generate a 6-character alphanumeric code from the URL
def url_to_alphanumeric_code(url):
    md5_hash = hashlib.md5(url.encode()).hexdigest()
    code = md5_hash[:6]
    alphanumeric_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    return alphanumeric_code
    
def is_valid_time(time_str):
    try:
        datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

def is_valid_test_name(test_name):
    return bool(re.match(r"^[a-zA-Z0-9_]+$", test_name))

def test_creation(connection,test_name,starts_at,ends_at,test_url, test_code):
    # test_name = input("Enter the test name: ")
    # starts_at = input("Enter the start time: ")
    # ends_at = input("Enter the end time: ")
    # send_alerts = input("Show alerts? (yes/no): ")
    # test_url = input("Enter the test URL: ")
    # test_code = url_to_alphanumeric_code(test_url)
    # print(test_code)

    if not is_valid_time(starts_at) or not is_valid_time(ends_at):
        print("Invalid time format. Please use 24-hour format HH:MM.")
        return

    if starts_at >= ends_at:
        print("Start time must be before end time.")
        return

    if not is_valid_test_name(test_name):
        print("Invalid test name. Use alphanumeric characters and underscores only.")
        return
    # Create a connection to the MySQL database
    # connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS create_test (Test_Name VARCHAR(255) NOT NULL UNIQUE, Starts_At VARCHAR(50) NOT NULL, Ends_At VARCHAR(50) NOT NULL, Test_Url VARCHAR(255) NOT NULL, Test_Code VARCHAR(6) NOT NULL )")

    # Insert the data into the MySQL database
    cursor.execute("INSERT INTO create_test (test_name, starts_at, ends_at, test_url, test_code) VALUES (%s, %s, %s, %s, %s)",
                   (test_name, starts_at, ends_at, test_url, test_code))
    connection.commit()

    # url_to_alphanumeric_code(test_url)
    print("Test data saved successfully!")

    # Close the cursor and connection
    cursor.close()
    # connection.close()

def main():
    test_creation()

if __name__ == "__main__":
    main()






