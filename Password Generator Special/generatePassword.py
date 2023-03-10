import random
import sys

import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import string


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(261, 281)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(14, 10, 241, 20))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 221, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(20, 200, 221, 20))
        self.output.setText("")
        self.output.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.output.setObjectName("output")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 240, 242, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.generate = QtWidgets.QPushButton(self.widget)
        self.generate.setObjectName("generate")
        self.horizontalLayout.addWidget(self.generate)
        self.copy = QtWidgets.QPushButton(self.widget)
        self.copy.setObjectName("copy")
        self.horizontalLayout.addWidget(self.copy)
        self.value = QtWidgets.QSpinBox(self.widget)
        self.value.setAccelerated(True)
        self.value.setMinimum(4)
        self.value.setMaximum(32)
        self.value.setProperty("value", 16)
        self.value.setObjectName("value")
        self.horizontalLayout.addWidget(self.value)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(60, 80, 139, 103))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.numbers = QtWidgets.QCheckBox(self.widget1)
        self.numbers.setObjectName("numbers")
        self.verticalLayout.addWidget(self.numbers)
        self.cLetters = QtWidgets.QCheckBox(self.widget1)
        self.cLetters.setObjectName("cLetters")
        self.verticalLayout.addWidget(self.cLetters)
        self.lLetters = QtWidgets.QCheckBox(self.widget1)
        self.lLetters.setObjectName("lLetters")
        self.verticalLayout.addWidget(self.lLetters)
        self.characters = QtWidgets.QCheckBox(self.widget1)
        self.characters.setObjectName("characters")
        self.verticalLayout.addWidget(self.characters)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "--> Password Generator <--"))
        self.label_2.setText(_translate("MainWindow", "Please enter password lentgh."))
        self.generate.setText(_translate("MainWindow", "Generate"))
        self.copy.setText(_translate("MainWindow", "Copy"))
        self.numbers.setText(_translate("MainWindow", "Numbers"))
        self.cLetters.setText(_translate("MainWindow", "Capital Letters"))
        self.lLetters.setText(_translate("MainWindow", "Lower Case Letters"))
        self.characters.setText(_translate("MainWindow", "Characters"))


        self.generate.clicked.connect(lambda: X.generate(self))
        self.copy.clicked.connect(lambda: X.copy_password(self))
        MainWindow.setWindowTitle("PswGn")
        MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))
        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)



class X(Ui_MainWindow):


    def generate(self):
        password_length = self.value.value()
        lowerLetters = string.ascii_letters[:26]
        cLetters = string.ascii_letters[26:]
        numbers = string.digits
        punctation = string.punctuation
        a =""
        b =""
        c =""
        d =""
        if self.numbers.isChecked():
            a = numbers
        if self.lLetters.isChecked():
            b = lowerLetters
        if self.cLetters.isChecked():
            c = cLetters
        if self.characters.isChecked():
            d = punctation
        printable = a+b+c+d
        password = list(printable)
        password = random.sample(printable,k=password_length)
        output = ''.join(password)
        self.output.setText(output)


    def copy_password(self):
        text = self.output.text()
        if text == "":
            msg = QMessageBox()
            msg.setWindowTitle("PswGn")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('icon.ico'))
            msg.setText("Output is null.")
            msg.exec_()
        else:
            pyperclip.copy(text)
            msg = QMessageBox()
            msg.setWindowTitle("PswGn")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QtGui.QIcon('icon.ico'))
            msg.setText("Generated password copied on clipboard.")
            msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())