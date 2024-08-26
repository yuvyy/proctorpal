import sys
import mysql.connector
from capture import capture_and_save_image
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


class RegistrationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Registration Page")
        self.setGeometry(100, 100, 400, 400)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.admission_number_label = QLabel("Admission Number:")
        self.admission_number_input = QLineEdit()

        self.first_name_label = QLabel("First Name:")
        self.first_name_input = QLineEdit()

        self.last_name_label = QLabel("Last Name:")
        self.last_name_input = QLineEdit()

        self.mes_id_label = QLabel("MES ID:")
        self.mes_id_input = QLineEdit()

        self.year_label = QLabel("Year:")
        self.year_input = QLineEdit()

        self.department_label = QLabel("Department:")
        self.department_input = QLineEdit()

        self.dob_label = QLabel("Date of Birth (YYYY-MM-DD):")
        self.dob_input = QLineEdit()

        self.phone_number_label = QLabel("Phone Number:")
        self.phone_number_input = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register_student)

        layout.addWidget(self.admission_number_label)
        layout.addWidget(self.admission_number_input)
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_input)
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.mes_id_label)
        layout.addWidget(self.mes_id_input)
        layout.addWidget(self.year_label)
        layout.addWidget(self.year_input)
        layout.addWidget(self.department_label)
        layout.addWidget(self.department_input)
        layout.addWidget(self.dob_label)
        layout.addWidget(self.dob_input)
        layout.addWidget(self.phone_number_label)
        layout.addWidget(self.phone_number_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register_student(self):
        admission_number = self.admission_number_input.text()
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        mes_id = self.mes_id_input.text()
        year = self.year_input.text()
        department = self.department_input.text()
        dob = self.dob_input.text()
        phone_number = self.phone_number_input.text()
        password = self.password_input.text()
        user_image = capture_and_save_image(admission_number)

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='kl!nEfeltEr38',
                database='db9'
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
