import keyboard
import sys
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from admin_reg import *
from admin_login import *
from face_reg import perform_face_detection
from student_reg import register_student
from create_test import test_creation, url_to_alphanumeric_code
from student_homepage import *
import mysql.connector
from PyQt5.QtCore import QUrl, QTimer, QTime
from PyQt5.QtWebEngineWidgets import QWebEngineView
import datetime
from verification import verification
from datetime import datetime, time
import multiprocessing
from facenotfound import facenotfound


MES_ID = None

SESSION_TRACKER = {}

######## Data Base Connection ########
# import mysql.connector

########### welcome.ui #########

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("guicomponents\welcome_screen.ui",self)
        self.addimage()
        self.Login.clicked.connect(self.radiobutton)
        self.Signup.clicked.connect(self.radiobutton)
    
    def addimage(self):
        qp = QPixmap("guicomponents\download.jpg")
        self.label.setPixmap(qp)

    def login(self):
        mes_id = self.mes_id.text()
        password= self.password.text()
        if len(mes_id)==0 or len(password)==0:
            self.error.setText("Incorrect credentials")
        else:
            global MES_ID
            MES_ID = mes_id
            authenticate_user(connection, mes_id, password)
            obj2 = DashBoard()
            widget.addWidget(obj2)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def loginfac(self):
        mes_id = self.mes_id.text()
        password = self.password.text()
        if len(mes_id)==0 or len(password)==0:
            self.error.setText("Incorrect credentials")
        else:
            authenticate_user(connection, mes_id, password)
            obj2 = FacDashBoard()
            widget.addWidget(obj2)
            widget.setCurrentIndex(widget.currentIndex() + 1)
           
    def signup(self):
        obj = SignUp()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def signupfac(self):
        obj1 = SignUpFaculty()
        widget.addWidget(obj1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
    def radiobutton(self):
        if self.Student.isChecked():
            self.Signup.clicked.connect(self.signup)
        else:
            self.Signup.clicked.connect(self.signupfac)

        if self.Student.isChecked():
            self.Login.clicked.connect(self.login)
        else:
            self.Login.clicked.connect(self.loginfac)
        

########### Dashboard.ui #########

# class DashBoard(QDialog):
#     def __init__(self):
#         super(DashBoard, self).__init__()
#         loadUi("guicomponents\Dashboard.ui",self)
#         self.addimage()
#         self.comboBox.activated.connect(self.combobox)
#         self.submit.clicked.connect(self.start_exam)
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Embedded Web Browser")
#         self.setGeometry(100, 100, 800, 600)

#         # central_widget = QWidget(self)
#         # self.setCentralWidget(central_widget)

#         layout = QVBoxLayout()

#         self.test_code_input = QLineEdit(self)
#         layout.addWidget(self.test_code_input)

#         self.load_url_button = QPushButton("Go!", self)
#         layout.addWidget(self.load_url_button)

#         self.web_view = QWebEngineView(self)
#         layout.addWidget(self.web_view)

#         self.timer_label = QLabel(self)

#         central_widget.setLayout(layout)

#         self.load_url_button.clicked.connect(self.load_test_url)

#         self.web_view.loadFinished.connect(self.handle_webpage_loaded)

#         self.is_fullscreen = False  

#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.handle_timer_event)

#         self.start_time = None
#         self.timer_duration = 0

#     def load_test_url(self):
#         test_code = self.test_code_input.text()

#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="kl!nEfeltEr38",
#             database="db9"
#         )

#         cursor = connection.cursor()

#         query = "SELECT test_url,starts_at,ends_at FROM create_test WHERE Test_Code = %s"
#         cursor.execute(query, (test_code,))
#         result = cursor.fetchone()
#         print(result)
#         def to_min(time):
#             return (int(time[:2])*60)+(int(time[3:]))
#         startTime = to_min(result[1])
#         endTime = to_min(result[2])
#         current_datetime = datetime.datetime.now()
#         current_time = current_datetime.time()
#         # minutes1 = current_time.hour * 60 + current_time.minute
#         # minutes2 = delta2.total_seconds() / 60

#         timer_duration = int (endTime - startTime)  # Replace 10 with the desired number of minutes as an integer
#         # timer_duration = int (1)
#         if result:
#             url = result[0]
#             self.web_view.setUrl(QUrl(url))
#             self.test_code_input.hide()
#             self.load_url_button.hide()

#             keyboard.add_hotkey('alt+tab', lambda: None)  
#             keyboard.add_hotkey('ctrl+tab', lambda: None) 
#             keyboard.add_hotkey('ctrl+shift+esc', lambda: None)  

#             blocked_keys = {'alt', 'tab', 'ctrl', 'shift', 'esc', 'win'}
#             for key in blocked_keys:
#                 keyboard.block_key(key)

#             self.showMaximized()

#             self.start_time = QTime.currentTime()
#             self.timer_duration = timer_duration * 60  
#             self.timer.start(1000) 

#         else:
#             print("Test code not found. Please check the code and try again.")

#         cursor.close()
#         connection.close()

#     def handle_webpage_loaded(self):
#         self.is_fullscreen = not self.is_fullscreen
#         if self.is_fullscreen:
#             self.showFullScreen()
#         else:
#             self.showNormal()

#     def handle_timer_event(self):
        
#         current_time = QTime.currentTime()
#         elapsed_time = self.start_time.secsTo(current_time)
#         remaining_time = self.timer_duration - elapsed_time

#         if remaining_time <= 0:
#             self.timer.stop()
#             self.timer_label.setText("Timer expired! Window closing Soon")
#             QTimer.singleShot(5000, app.quit)
#             return

#         remaining_time_str = QTime(0, 0).addSecs(remaining_time).toString("hh:mm:ss")

#         self.timer_label.setText(remaining_time_str)
#     # def addimage(self):
#     #     qp = QPixmap("guicomponents\download.jpg")
#     #     self.label.setPixmap(qp)

#     def start_exam(self):
#         self.load_test_url(self)

#     # def combobox(self):
#     #     obj = WelcomeScreen()
#     #     widget.addWidget(obj)
#     #     widget.setCurrentIndex(widget.currentIndex()+1)


# ########### Faculty_Dashboard.ui #########

class FacultyDashBoard(QDialog):
    def __init__(self):
        super(FacultyDashBoard, self).__init__()
        loadUi("guicomponents\FacultyDashBoard.ui",self)
        self.addimage()
        self.comboBox.activated.connect(self.combobox)
        self.Start.clicked.connect(self.create_test)
        # self.code_label = QLabel()

    def addimage(self):
        qp = QPixmap("guicomponents\download.jpg")
        self.label.setPixmap(qp)
    
    def create_test(self):
        test_name = self.test_name.text()
        starts_at = self.starts_at.text()
        ends_at = self.ends_at.text()
        # send_alerts = self.send_alerts.text()
        test_url = self.test_url.text()
        test_code = url_to_alphanumeric_code(test_url)
        test_creation(connection,test_name, starts_at, ends_at, test_url, test_code)
        # test_code = self.test_code.setText({self.url.currentText()})
        self.label_2.setText(test_code)

    def combobox(self):
        obj = WelcomeScreen()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class DashBoard(QDialog):
    def __init__(self, parent=None):
        super(DashBoard, self).__init__()
        loadUi("guicomponents\Dashboard.ui",self)
        self.addimage()
        self.comboBox.activated.connect(self.combobox)
        self.submit.clicked.connect(self.start_exam)

        layout = QVBoxLayout(self)

        self.test_code_input = QLineEdit(self)
        layout.addWidget(self.test_code_input)

        self.load_url_button = QPushButton("Go!", self)
        layout.addWidget(self.load_url_button)

        self.web_view = QWebEngineView(self)
        layout.addWidget(self.web_view)

        self.timer_label = QLabel(self)
        layout.addWidget(self.timer_label)

        self.setLayout(layout)

        self.load_url_button.clicked.connect(self.load_test_url)

        self.web_view.loadFinished.connect(self.handle_webpage_loaded)

        self.is_fullscreen = False

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.handle_timer_event)

        self.start_time = None
        self.timer_duration = 0

    def startTest(self, url, timer_duration):
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

    def load_test_url(self):

        global MES_ID
        test_code = self.test_code_input.text()

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kl!nEfeltEr38",
            database="db9"
        )

        cursor = connection.cursor()

        print(MES_ID)
        query= "select user_image from student_id where MES_ID = %s"
        cursor.execute(query,(MES_ID,))
        result = cursor.fetchone()
        print(result[0])


        if verification(result[0]) == True:

            query = "SELECT test_url,starts_at,ends_at FROM create_test WHERE Test_Code = %s"
            cursor.execute(query, (test_code,))
            result = cursor.fetchone()
            print(result)

            def check_test_started(startTime, endTime):
                start_time_obj = time(int(startTime // 60), startTime % 60)
                end_time_obj = time(int(endTime // 60), endTime % 60)
                current_datetime = datetime.now()
                current_time = current_datetime.time()
                if start_time_obj <= current_time <= end_time_obj:
                    return True
                else:
                    print("The test hasn't started yet. Please try later.")
                    return False

                
                
            def to_min(time):
                return (int(time[:2])*60)+(int(time[3:]))
            
            startTime = to_min(result[1])
            endTime = to_min(result[2])
            current_datetime = datetime.now()
            current_time = current_datetime.time()
            

            timer_duration = int (endTime - startTime)

            if result:

                if check_test_started(startTime, endTime):
                    
                    timer_duration = int(endTime - startTime)
                    url = result[0]
                    # self.startTest(url, timer_duration)

                    test_process = multiprocessing.Process(target=self.startTest(url, timer_duration))
                    face_detection_process = multiprocessing.Process(target=facenotfound())

                    test_process.start()
                    face_detection_process.start()

                    test_process.join()
                    face_detection_process.join()
                
                else:
                    print("Test not started yet")
                    # add gui code to display that test not started yet

            else:
                print("Test code not found. Please check the code and try again.")
        
        else:
            print("User not verified")
        

        cursor.close()
        connection.close()

    def handle_webpage_loaded(self):
        self.is_fullscreen = not self.is_fullscreen
        if self.is_fullscreen:
            self.showFullScreen()
        else:
            self.showNormal()

    def handle_timer_event(self,stop_event):
        
        current_time = QTime.currentTime()
        elapsed_time = self.start_time.secsTo(current_time)
        remaining_time = self.timer_duration - elapsed_time

        if remaining_time <= 0:
            self.timer.stop()
            self.timer_label.setText("Timer expired! Window closing Soon")
            QTimer.singleShot(5000, self.close)
            stop_event.set()
            return

        remaining_time_str = QTime(0, 0).addSecs(remaining_time).toString("hh:mm:ss")
        
        self.timer_label.setText(remaining_time_str)


    def addimage(self):
        qp = QPixmap("guicomponents\download.jpg")
        self.label.setPixmap(qp)

    def start_exam(self):
        self.load_test_url(self)

    def combobox(self):
        obj = WelcomeScreen()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex()+1)


class FacDashBoard(QDialog):
    def __init__(self):
        super(FacDashBoard, self).__init__()
        loadUi("guicomponents\FacDashBoard.ui",self)
        self.addimage()
        self.comboBox.activated.connect(self.combobox)
        self.conduct.clicked.connect(self.goto)

    def addimage(self):
        qp = QPixmap("guicomponents\download.jpg")
        self.label.setPixmap(qp)
    
    def goto(self):
        obj2 = FacultyDashBoard()
        widget.addWidget(obj2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def combobox(self):
        obj = WelcomeScreen()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex() + 1)

########### signup.ui #########

class SignUp(QDialog):
    
    user_image = None
    ad_no = None
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi("guicomponents\Sign_Up.ui", self)
        self.addimage()
        self.Signup_2.clicked.connect(self.goback)
        self.Signup.clicked.connect(self.signup)
        self.user_image.clicked.connect(self.clicker)

    def addimage(self):
        qp = QPixmap("guicomponents\download.jpg")
        self.label.setPixmap(qp)

    def goback(self):
        obj=WelcomeScreen()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def clicker(self):
        SignUp.ad_no = self.admission_number_2.text()
        SignUp.user_image = perform_face_detection(SignUp.ad_no)
  
    def signup(self):
        SignUp.ad_no = self.admission_number_2.text()
        admission_number = self.admission_number_2.text()
        first_name = self.first_name_2.text()
        last_name = self.last_name_2.text()
        mes_id = self.mes_id_2.text()
        year = self.year_2.text()
        department = self.department_2.text()
        old_date = self.dob_2.text()
        dob = old_date[6:]+'-'+old_date[3:5]+'-'+old_date[:2]
        phone_number = self.phone_number_2.text()
        password = self.password_2.text()
        confirm_password = self.confirm_password_2.text()
        user_image = SignUp.user_image
        if (len(admission_number) and len(first_name) and len(last_name) and len(mes_id)
            and len(year) and len(department) and len(dob) and len(phone_number) and len(password) and len(confirm_password) and len(user_image)) == 0:
            self.error.setText("Please fill all Credentials")
        else:
            if password == confirm_password:
                register_student(connection, admission_number, first_name, last_name, mes_id, year, department, dob, phone_number, confirm_password, user_image)
                self.goback()
            else:
                self.error.setText("Passwords don't match")


        ########### SignUpFaculty.ui #########

class SignUpFaculty(QDialog):
    def __init__(self):
        super(SignUpFaculty, self).__init__()
        loadUi("guicomponents\Sign_Up_faculty.ui", self)
        self.addimagefac()
        self.SignupFac_2.clicked.connect(self.gobackfac)
        self.SignupFac.clicked.connect(self.signupfac)

    def addimagefac(self):
        qp1 = QPixmap("guicomponents\download.jpg")
        self.label.setPixmap(qp1)

    def gobackfac(self):
        obj2 = WelcomeScreen()
        widget.addWidget(obj2)
        widget.setCurrentIndex(widget.currentIndex()+1)

#yyyy-mm-dd
#dd-mm-yyyy
    def signupfac(self):
        first_name = self.first_name_2.text()
        last_name = self.last_name_2.text()
        mes_id = self.mes_id_2.text()     
        old_date = self.dob_2.text()
        dob = old_date[6:]+'-'+old_date[3:5]+'-'+old_date[:2]
        phone_number = self.phone_number_2.text()
        password = self.password_2.text()
        if (len(first_name) and len(last_name) and len(mes_id) and len(dob)
            and len(phone_number) and len(password)) == 0:
            self.error.setText("Please fill all Credentials")
        else:       
            register_admin(connection, first_name, last_name, mes_id, dob, phone_number, password)
            self.gobackfac()

########### MAIN CODE #########
#The code below are mandatory to launch the PyQt APP

app = QApplication(sys.argv)
connection = create_connection()
create_admin_table(connection)

welcome= WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(700)
widget.setFixedWidth(1125)
widget.show()
try:
    # connection.close()
    sys.exit((app.exec()))
except:
    print("exiting")
    print("MySQL connection is closed.")
