import sys
import keyboard
from PyQt5.QtCore import QUrl, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel
import mysql.connector
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineView
import datetime
    
class WebBrowserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Embedded Web Browser")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.test_code_input = QLineEdit(self)
        layout.addWidget(self.test_code_input)

        self.load_url_button = QPushButton("Go!", self)
        layout.addWidget(self.load_url_button)

        self.web_view = QWebEngineView(self)
        layout.addWidget(self.web_view)

        self.timer_label = QLabel(self)

        central_widget.setLayout(layout)

        self.load_url_button.clicked.connect(self.load_test_url)

        self.web_view.loadFinished.connect(self.handle_webpage_loaded)

        self.is_fullscreen = False  

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.handle_timer_event)

        self.start_time = None
        self.timer_duration = 0

    def load_test_url(self):
        test_code = self.test_code_input.text()

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kl!nEfeltEr38",
            database="db9"
        )

        cursor = connection.cursor()

        query = "SELECT test_url,starts_at,ends_at FROM create_test WHERE Test_Code = %s"
        cursor.execute(query, (test_code,))
        result = cursor.fetchone()
        print(result)
        def to_min(time):
            return (int(time[:2])*60)+(int(time[3:]))
        startTime = to_min(result[1])
        endTime = to_min(result[2])
        current_datetime = datetime.datetime.now()
        current_time = current_datetime.time()
        # minutes1 = current_time.hour * 60 + current_time.minute
        # minutes2 = delta2.total_seconds() / 60

        timer_duration = int (endTime - startTime)  # Replace 10 with the desired number of minutes as an integer
        # timer_duration = int (1)
        if result:
            url = result[0]
            self.web_view.setUrl(QUrl(url))
            self.test_code_input.hide()
            self.load_url_button.hide()

            keyboard.add_hotkey('alt+tab', lambda: None)  
            keyboard.add_hotkey('ctrl+tab', lambda: None) 
            keyboard.add_hotkey('ctrl+shift+esc', lambda: None)  

            blocked_keys = {'alt', 'tab', 'ctrl', 'shift', 'esc', 'win'}
            for key in blocked_keys:
                keyboard.block_key(key)

            self.showMaximized()

            self.start_time = QTime.currentTime()
            self.timer_duration = timer_duration * 60  
            self.timer.start(1000) 

        else:
            print("Test code not found. Please check the code and try again.")

        cursor.close()
        connection.close()

    def handle_webpage_loaded(self):
        self.is_fullscreen = not self.is_fullscreen
        if self.is_fullscreen:
            self.showFullScreen()
        else:
            self.showNormal()

    def handle_timer_event(self):
        
        current_time = QTime.currentTime()
        elapsed_time = self.start_time.secsTo(current_time)
        remaining_time = self.timer_duration - elapsed_time

        if remaining_time <= 0:
            self.timer.stop()
            self.timer_label.setText("Timer expired! Window closing Soon")
            QTimer.singleShot(5000, close_application)
            return

        remaining_time_str = QTime(0, 0).addSecs(remaining_time).toString("hh:mm:ss")

        self.timer_label.setText(remaining_time_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser_app = WebBrowserApp()
    browser_app.show()
    sys.exit(app.exec_())

def close_application():
    app.quit()

# keyboard.hook(close_application)




# #this is for students' homepage where they enter a test code
# import sys
# import keyboard
# from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget
# import mysql.connector
# from PyQt5.QtWebEngineWidgets import QWebEnginePage
# from PyQt5.QtWebEngineWidgets import QWebEngineView

# class WebBrowserApp(QMainWindow):
#     def _init_(self):
#         super()._init_()
#         self.setWindowTitle("Embedded Web Browser")
#         self.setGeometry(100, 100, 800, 600)

#         # Create a central widget
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         layout = QVBoxLayout()

#         # Input field for test code
#         self.test_code_input = QLineEdit(self)
#         layout.addWidget(self.test_code_input)

#         # Button to load the URL
#         self.load_url_button = QPushButton("Go!", self)
#         layout.addWidget(self.load_url_button)

#         # Web view for displaying the web page
#         self.web_view = QWebEngineView(self)
#         layout.addWidget(self.web_view)

#         central_widget.setLayout(layout)

#         # Connect the button click event to load the URL
#        # self.load_url_button.clicked.connect(self.load_test_url)    
#         # Connect the button click event to load the URL
#         self.load_url_button.clicked.connect(self.load_test_url)

#         # Connect the webpage loaded signal
#         self.web_view.loadFinished.connect(self.handle_webpage_loaded)

#         self.is_fullscreen = False  # Track fullscreen state


#     def load_test_url(self):
#         test_code = self.test_code_input.text()

#         # Connect to the MySQL database
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="kl!nEfeltEr38",
#             database="TESTDB"
#         )

#         cursor = connection.cursor()

#         # Query the database to retrieve the URL for the given test code
#         query = "SELECT test_url,starts_at,ends_at FROM TestTable WHERE test_code = %s"
#         cursor.execute(query, (test_code,))
#         result = cursor.fetchone()

#         if result:
#             url = result[0]
#             self.web_view.setUrl(QUrl(url))
#             self.test_code_input.hide()
#             self.load_url_button.hide()

#             keyboard.add_hotkey('alt+tab', lambda: None)  # Block Alt+Tab
#             keyboard.add_hotkey('ctrl+tab', lambda: None)  # Block Ctrl+Tab
#             keyboard.add_hotkey('ctrl+shift+esc', lambda: None)  # Block Ctrl+Shift+Esc

#             blocked_keys = {'alt', 'tab', 'ctrl', 'shift', 'esc', 'win'}
#             for key in blocked_keys:
#                 keyboard.block_key(key)

#             self.showMaximized()

#         else:
#             print("Test code not found. Please check the code and try again.")

#         cursor.close()
#         connection.close()

#     def handle_webpage_loaded(self):
#         # When the webpage is loaded, toggle fullscreen
#         self.is_fullscreen = not self.is_fullscreen
#         if self.is_fullscreen:
#             self.showFullScreen()
#         else:
#             self.showNormal()

# if _name_ == '_main_':
#     app = QApplication(sys.argv)
#     browser_app = WebBrowserApp()
#     browser_app.show()
#     sys.exit(app.exec_())

#         # Define a function to close the application
#     def close_application():
#         app.quit()
# # Add a keyboard event to close the application if the user switches out
# keyboard.hook(close_application)