
import sys
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from test.admin_reg import *

######## Data Base Connection ########
import mysql.connector


########### welcome.ui #########

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("app\components\loginreg\welcome_screen.ui",self)
        self.addimage()
        self.Login.clicked.connect(self.radiobutton)
        self.Signup.clicked.connect(self.radiobutton)
    
    def addimage(self):
        qp = QPixmap("app\components\loginreg\download.jpg")
        self.label.setPixmap(qp)

    def login(self):
        # user = self.username.text()
        # pwd = self.password.text()
        # if len(user)==0 or len(pwd)==0:
        #     self.error.setText("Incorrect credentials")
        # else:
        #     try:
        #         # connecting to DB and validating the Uname and pwd
        #         mydb = mysql.connector.connect(
        #             host='127.0.0.1',
        #             user='root ',
        #             passwd='MySQL@9287',
        #             port='3306',
        #             database='register')
        #         cur=mydb.cursor()
        #         cur.execute('SELECT * from account_details where Username=%s and Password=%s'
        #                ,(user,pwd))
        #         if cur.fetchone():
        #             self.error.setText("successfull")
        obj2 = DashBoard()
        widget.addWidget(obj2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
            #     else:
            #         self.error.setText("Incorrect credentials or Pwd")
            # except Exception as es:
            #     print("Error")

    def loginfac(self):
        # user = self.username.text()
        # pwd = self.password.text()
        # if len(user)==0 or len(pwd)==0:
        #     self.error.setText("Incorrect credentials")
        # else:
        #     try:
        #         # connecting to DB and validating the Uname and pwd
        #         mydb = mysql.connector.connect(
        #             host='127.0.0.1',
        #             user='root ',
        #             passwd='MySQL@9287',
        #             port='3306',
        #             database='register')
        #         cur=mydb.cursor()
        #         cur.execute('SELECT * from account_details where Username=%s and Password=%s'
        #                ,(user,pwd))
        #         if cur.fetchone():
        #             self.error.setText("successfull")
        obj2 = FacDashBoard()
        widget.addWidget(obj2)
        widget.setCurrentIndex(widget.currentIndex() + 1)
            #     else:
            #         self.error.setText("Incorrect credentials or Pwd")
            # except Exception as es:
            #     print("Error")    

    def signup(self):
        obj = SignUp()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def signupfac(self):
        obj1 = SignUpFaculty()
        widget.addWidget(obj1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.Signup.clicked.connect(self.signup_clicked)

    def signup_clicked(self):
        register_admin()  
        
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

class DashBoard(QDialog):
    def __init__(self):
        super(DashBoard, self).__init__()
        loadUi("app\components\loginreg\Dashboard.ui",self)
        self.addimage()
        self.comboBox.activated.connect(self.combobox)

    def addimage(self):
        qp = QPixmap("app\components\loginreg\download.jpg")
        self.label.setPixmap(qp)

    def combobox(self):
        obj = WelcomeScreen()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex()+1)


########### Faculty_Dashboard.ui #########

class FacultyDashBoard(QDialog):
    def __init__(self):
        super(FacultyDashBoard, self).__init__()
        loadUi("app\components\loginreg\FacultyDashBoard.ui",self)
        self.addimage()
        self.comboBox.activated.connect(self.combobox)

    def addimage(self):
        qp = QPixmap("app\components\loginreg\download.jpg")
        self.label.setPixmap(qp)

    def combobox(self):
        obj = WelcomeScreen()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class FacDashBoard(QDialog):
    def __init__(self):
        super(FacDashBoard, self).__init__()
        loadUi("app\components\loginreg\FacDashBoard.ui",self)
        self.addimage()
        self.comboBox.activated.connect(self.combobox)
        self.conduct.clicked.connect(self.goto)

    def goto(self):
        obj2 = FacultyDashBoard()
        widget.addWidget(obj2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def addimage(self):
        qp = QPixmap("app\components\loginreg\download.jpg")
        self.label.setPixmap(qp)

    def combobox(self):
        obj = WelcomeScreen()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex() + 1)

########### signup.ui #########

class SignUp(QDialog):
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi("app\components\loginreg\Sign_Up.ui", self)
        self.addimage()
        self.Signup_2.clicked.connect(self.goback)
        self.Signup.clicked.connect(self.signup)
        # self.user_image_2.clicked.connect(self.clicker)

    def addimage(self):
        qp = QPixmap("app\components\loginreg\download.jpg")
        self.label.setPixmap(qp)

    def goback(self):
        obj=WelcomeScreen()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # def clicker(self):
        # fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);; PDF Files (*.pdf);;  JPG Files (*.jpg);; JPEG Files (*.jpeg);; PNG Files (*.png)")

    def signup(self):
        admission_number = self.admission_number_2.text()
        first_name = self.first_name_2.text()
        last_name = self.last_name_2.text()
        mes_id = self.mes_id_2.text()
        year = self.year_2.text()
        department = self.department_2.text()
        dob = self.dob_2.text()
        phone_number = self.phone_number_2.text()
        password = self.password_2.text()
        confirm_password = self.confirm_password_2.text()
        # user_image = self.user_image_2.text()
        # if (len(admission_number) and len(first_name) and len(last_name) and len(mes_id)
        #     and len(year) and len(department) and len(dob) and len(phone_number) and len(password) and len(confirm_password)) == 0:
        #     self.error.setText("Please fill all Credentials")
        # else:
        #     if password == confirm_password:
        #         try:
        #             db = mysql.connector.connect(
        #                 host='127.0.0.1',
        #                 user='root',
        #                 passwd='MySQL@9287',
        #                 port='3306',
        #                 database='register')
        #             cur = db.cursor()
        #             cur.execute("CREATE TABLE IF NOT EXISTS student_id (id INT AUTO_INCREMENT PRIMARY KEY, admission_number VARCHAR(10) NOT NULL UNIQUE, first_name VARCHAR(255) NOT NULL, last_name VARCHAR(255) NOT NULL, mes_id VARCHAR(255) NOT NULL, year VARCHAR(255) NOT NULL, department VARCHAR(255) NOT NULL, dob DATE NOT NULL, phone_number VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, confirm_password VARCHAR(255) NOT NULL)")
        #             R = cur.fetchone()
        #             if R != None and R[0] != None:
        #                 id = int(R[0]) + 1
        #             cur = db.cursor()
        #             sql ="insert into register(id, admission_number, first_name, last_name, mes_id, year, department, dob, phone_number, password, confirm_password) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        #             cur.execute(sql,(id,admission_number,first_name,last_name,mes_id,year,department,dob,phone_number,password,confirm_password))
        #             db.commit()
        #             if cur.fetchone():
        #                 self.error.setText("ERROR")
        #             else:
        #                  self.error.setText("Sign Up Successfull ")
        #                  self.error.setStyleSheet("color:green")
        #                  self.error.setFont(QFont('MS Shell Dlg 2', 14))

        #         except Exception as es:
        #             print("error")
        #             self.error.setText("ERROR ")
        #     else:
        #         self.error.setText("Passwords don't match")


        ########### SignUpFaculty.ui #########

class SignUpFaculty(QDialog):
    def __init__(self):
        super(SignUpFaculty, self).__init__()
        loadUi("app\components\loginreg\Sign_Up_faculty.ui", self)
        self.addimagefac()
        self.SignupFac_2.clicked.connect(self.gobackfac)
        self.SignupFac.clicked.connect(self.signupfac)

    def addimagefac(self):
        qp1 = QPixmap("app\components\loginreg\download.jpg")
        self.label.setPixmap(qp1)

    def gobackfac(self):
        obj2 = WelcomeScreen()
        widget.addWidget(obj2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signupfac(self):
        first_name = self.first_name_2.text()
        last_name = self.last_name_2.text()
        mes_id = self.mes_id_2.text()     
        dob = self.dob_2.text()
        phone_number = self.phone_number_2.text()
        password = self.password_2.text()
        # if (len(name) and len(Phnum) and len(pwd) and len(user)
        #     and len(confirmpwd)) == 0:
        #     self.error.setText("Please fill all Credentials")
        # else:
        #     if pwd == confirmpwd:
        #         try:
        #             mydb = mysql.connector.connect(
        #                 host='localhost',
        #                 user='root',
        #                 passwd='kumar',
        #                 port='3306',
        #                 database='test')
        #             cur = mydb.cursor()
        #             id_query="SELECT max(id) from test.account_details"
        #             cur.execute(id_query)
        #             R=cur.fetchone()
        #             if R!=None and R[0]!=None:
        #                 id=int(R[0])+1
        #             cur = mydb.cursor()
        #             sql="insert into test.account_details(id,Name,PhNum,Username,Password) values(%s, %s, %s, %s, %s)"
        #             cur.execute(sql,(id,name,Phnum,user,pwd))
        #             mydb.commit()
        #             if cur.fetchone():
        #                 self.error.setText("ERROR")
        #             else:
        #                  self.error.setText("Sign Up Successfull ")
        #                  self.error.setStyleSheet("color:green")
        #                  self.error.setFont(QFont('MS Shell Dlg 2', 14))

        #         except Exception as es:
        #             print("error")
        #             self.error.setText("ERROR ")
        #     else:
        #         self.error.setText("Passwords don't match")

########### MAIN CODE #########
#The code below are mandatory to launch the PyQt APP

app = QApplication(sys.argv)
connection = create_connection()
if connection is None:
    create_admin_table(connection)

welcome= WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(700)
widget.setFixedWidth(1125)
widget.show()
try:
    sys.exit((app.exec()))
    connection.close()
except:
    print("exiting")
    print("MySQL connection is closed.")
