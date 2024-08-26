import sys
import mysql.connector
from capture import capture_and_save_image
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPalette, QColor

class RegistrationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Registration Page")
        self.setGeometry(100, 100, 400, 400)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Define custom colors
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))  # Background color
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))   # Text color
        palette.setColor(QPalette.Button, QColor(200, 200, 200))  # Button background color
        palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))   # Button text color

        self.setPalette(palette)

        # Create labels, input fields, and buttons
        self.admission_number_label = QLabel("Admission Number:")
        self.admission_number_input = QLineEdit()

        # ... (Other labels and input fields)

        self.register_button = QPushButton("Register")
        self.register_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.register_button.clicked.connect(self.validate_and_register)

        # Add widgets to the layout
        layout.addWidget(self.admission_number_label)
        layout.addWidget(self.admission_number_input)
        # ... (Add other widgets)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def validate_and_register(self):
        # Retrieve input values
        admission_number = self.admission_number_input.text()
        # ... (Retrieve values for other fields)

        # Check if any field is empty
        if not admission_number or not first_name or not last_name or not mes_id or not year or not department or not dob or not phone_number or not password:
            QMessageBox.critical(self, "Error", "Please fill in all fields.")
            return  # Don't proceed with registration if any field is empty

        # If all fields are filled, proceed with registration
        user_image = capture_and_save_image(admission_number)

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='your_username',
                password='your_password',
                database='your_database'
            )

            cursor = connection.cursor()
            insert_query = "INSERT INTO student_id (Admission_Number, First_Name, Last_Name, MES_ID, Year, Department, DOB, Phone_Number, Password, user_image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (admission_number, first_name, last_name, mes_id, year, department, dob, phone_number, password, user_image)
            cursor.execute(insert_query, data)
            connection.commit()

            QMessageBox.information(self, "Registration Successful", "Student registration successful!")
            connection.close()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"Error registering student: {e}")

def main():
    app = QApplication(sys.argv)
    window = RegistrationPage()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
