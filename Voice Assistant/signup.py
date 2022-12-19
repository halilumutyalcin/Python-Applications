# --! Libraries

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from google.cloud import storage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# --! Setup of Firebase

firebaseConfig = {
    "apiKey": "AIzaSyCe1oRfbsRzPU-_XpG7rNtKcPZ3eJ10tmY",
    "authDomain": "loginform-4acac.firebaseapp.com",
    "projectId": "loginform-4acac",
    "databaseURL": "https://loginform-4acac.appspot.com",
    "storageBucket": "loginform-4acac.appspot.com",
    "messagingSenderId": "1059346041006",
    "appId": "1:1059346041006:web:39f39d37d2c0b78b15053f",
    "measurementId": "G-ESLYGKDXW9"
}
firebase = firebase.initialize_app(firebaseConfig)
auth = firebase.auth()


class Sign(object):

    # --! Connect to Firebase Data

    def signup(self):
        email = self.email.text()
        password = self.password.text()
        confirmpassword = self.confirmpassword.text()

        try:
            if self.password.text() == self.confirmpassword.text():
                password = self.password.text()
                user = auth.create_user_with_email_and_password(email, password)
                print("Sucsessfully signed up.")

            else:
                self.invalid.setVisible(True)
                print("şifre hatalı")
        except:
            print("sunucudan kaynaklı hata")
            self.invalid.setVisible(True)
        return

    # --! SignUp Page

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 550)

        # --! Settings of Window

        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(100, 20, 611, 451))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(290, 40, 251, 381))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
                                 "border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(-1, 25, 311, 421))
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(114, 83, 104, 255), stop:0.55 rgba(241, 238, 219, 255), stop:1 rgba(193, 145, 133, 255));\n"
            "border-radius: 20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(330, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgba(0,0,0,200);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.email = QtWidgets.QLineEdit(self.widget)
        self.email.setGeometry(QtCore.QRect(330, 140, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                 "border: 2px solid rgba(0,0,0,0);\n"
                                 "border-bottom-color: rgba(46,82,101,200);\n"
                                 "color: rgb(0,0,0);\n"
                                 "padding-bottom: 7px;")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(330, 200, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                    "border: 2px solid rgba(0,0,0,0);\n"
                                    "border-bottom-color: rgba(46,82,101,200);\n"
                                    "color: rgb(0,0,0);\n"
                                    "padding-bottom: 7px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(60, 50, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgba(0,0,0,200);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(58, 100, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgba(0,0,0,200);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(140, 350, 151, 71))
        self.label_7.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_7.setObjectName("label_7")
        self.signupbutton = QtWidgets.QPushButton(self.widget)
        self.signupbutton.setGeometry(QtCore.QRect(330, 360, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.signupbutton.setFont(font)
        self.signupbutton.setStyleSheet("QPushButton#signupbutton{\n"
                                        "    background-color: rgb(193, 145, 133);\n"
                                        "    color: rgba(255,255,255,200);\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton#signupbutton:pressed{\n"
                                        "    padding-left: 5px;\n"
                                        "    padding-top: 5px;\n"
                                        "    background-color: rgb(114, 83, 104);\n"
                                        "    background-position: calc(100% - 10px)center;\n"
                                        "}\n"
                                        "QPushButton#signupbutton:hover{\n"
                                        "    background-color: rgb(114, 83, 104);\n"
                                        "}")
        self.signupbutton.setObjectName("signupbutton")
        self.btn_minimize = QtWidgets.QPushButton(self.widget)
        self.btn_minimize.setGeometry(QtCore.QRect(480, 50, 16, 17))
        self.btn_minimize.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize.setMaximumSize(QtCore.QSize(17, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minimize.setFont(font)
        self.btn_minimize.setStyleSheet("QPushButton{\n"
                                        "    border: none;\n"
                                        "    border-radius: 8px;\n"
                                        "    background-color: rgb(63, 154, 165);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(3, 88, 93);\n"
                                        "}")
        self.btn_minimize.setObjectName("btn_minimize")
        self.btn_exit = QtWidgets.QPushButton(self.widget)
        self.btn_exit.setGeometry(QtCore.QRect(510, 50, 16, 17))
        self.btn_exit.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_exit.setMaximumSize(QtCore.QSize(17, 17))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("QPushButton{\n"
                                    "    border: none;\n"
                                    "    border-radius: 8px;\n"
                                    "    background-color: rgb(217, 62, 58);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color: rgb(141, 33, 31);\n"
                                    "}")
        self.btn_exit.setObjectName("btn_exit")
        self.confirmpassword = QtWidgets.QLineEdit(self.widget)
        self.confirmpassword.setGeometry(QtCore.QRect(330, 260, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.confirmpassword.setFont(font)
        self.confirmpassword.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                           "border: 2px solid rgba(0,0,0,0);\n"
                                           "border-bottom-color: rgba(46,82,101,200);\n"
                                           "color: rgb(0,0,0);\n"
                                           "padding-bottom: 7px;")
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setObjectName("confirmpassword")
        self.invalid = QtWidgets.QLabel(self.widget)
        self.invalid.setGeometry(QtCore.QRect(350, 310, 151, 20))
        self.invalid.setStyleSheet("color: rgba(0,0,0,200);")
        self.invalid.setObjectName("invalid")

        # --! Invisible Label

        self.invalid.setVisible(False)

        # --! Opacity Settings of button.

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.signupbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.btn_minimize.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.btn_exit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

        self.btn_minimize.clicked.connect(lambda: Form.showMinimized())
        self.btn_exit.clicked.connect(lambda: Form.close())
        self.signupbutton.clicked.connect(lambda: ux.signup())


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Sign Up"))
        self.email.setPlaceholderText(_translate("Form", "E-Mail"))
        self.password.setPlaceholderText(_translate("Form", "Password"))
        self.label_5.setText(_translate("Form", "Jarvis Assistant"))
        self.label_6.setText(_translate("Form", "Hi, \n"
                                                "I\'m Jarvis. \n"
                                                "I am your voice assistant. \n"
                                                "Please log in so I can help."))
        self.label_7.setText(_translate("Form", "Made by Halil Umut Yalcin,\n"
                                                "                      Betul Esen.\n"
                                                "\n"
                                                "All rights reserved. | 2021"))
        self.signupbutton.setText(_translate("Form", "S ı g n   U p "))
        self.btn_minimize.setText(_translate("Form", "-"))
        self.btn_exit.setText(_translate("Form", "X"))
        self.confirmpassword.setPlaceholderText(_translate("Form", "Confirm Password"))
        self.invalid.setText(_translate("Form", "Invalid email or passwords!"))

# --! Run Func.

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ux = Sign()
    ux.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
