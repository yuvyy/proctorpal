from connection import create_connection
from logreg import *
from student_reg import create_student_table

def main():
    connection = create_connection()
    create_admin_table(connection)
    create_student_table(connection)
    welcome= WelcomeScreen()
    widget = QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(700)
    widget.setFixedWidth(1125)
    widget.show()
    try:
        sys.exit((app.exec()))
    except:
        print("exiting")
        # print("MySQL connection is closed.")

    # connection.close()
if __name__ == "__main__":
    main()