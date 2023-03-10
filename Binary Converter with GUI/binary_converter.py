
import sys
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 163)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_text = QtWidgets.QLineEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(10, 40, 781, 22))
        self.input_text.setMaxLength(3250)
        self.input_text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.input_text.setReadOnly(False)
        self.input_text.setObjectName("input_text")
        self.display_label = QtWidgets.QLabel(self.centralwidget)
        self.display_label.setGeometry(QtCore.QRect(10, 10, 781, 20))
        self.display_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.display_label.setObjectName("display_label")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(10, 80, 781, 20))
        self.output.setText("")
        self.output.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.output.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.output.setObjectName("output")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 110, 771, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text_to_binary_bttn = QtWidgets.QPushButton(self.widget)
        self.text_to_binary_bttn.setObjectName("text_to_binary_bttn")
        self.horizontalLayout.addWidget(self.text_to_binary_bttn)
        self.copy_bttn = QtWidgets.QPushButton(self.widget)
        self.copy_bttn.setObjectName("copy_bttn")
        self.horizontalLayout.addWidget(self.copy_bttn)
        self.binary_to_code_bttn = QtWidgets.QPushButton(self.widget)
        self.binary_to_code_bttn.setObjectName("binary_to_code_bttn")
        self.horizontalLayout.addWidget(self.binary_to_code_bttn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.display_label.setText(_translate("MainWindow", "Enter text below"))
        self.text_to_binary_bttn.setText(_translate("MainWindow", "Text to Binary Code"))
        self.copy_bttn.setText(_translate("MainWindow", "Copy Output"))
        self.binary_to_code_bttn.setText(_translate("MainWindow", "Binary Code to Text"))

        self.copy_bttn.clicked.connect(lambda: Func.copy_text(self))
        self.text_to_binary_bttn.clicked.connect(lambda: Func.encrypt(self))
        self.binary_to_code_bttn.clicked.connect(lambda: Func.decrypt(self))

        MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))
        MainWindow.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)


class Func(Ui_MainWindow):

    def encrypt(self):
        text = self.input_text.text()
        res = " ".join(format(ord(i), "08b") for i in text)
        self.output.setText(res)

    def decrypt(self):
        try:
            text = self.input_text.text()
            binary_values = text.split()
            ascii_string = ""
            for binary_value in binary_values:
                an_integer = int(binary_value, 2)
                ascii_character = chr(an_integer)
                ascii_string += ascii_character

            self.output.setText(ascii_string)
            return ascii_string

        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('icon.ico'))
            msg.setText("Please enter binary code")
            msg.setWindowTitle("Binary Converter - Error")
            msg.exec_()



    def copy_text(self):
        text = self.output.text()
        if text == "":
            msg = QMessageBox()
            msg.setWindowTitle("Binary Converter")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowIcon(QtGui.QIcon('icon.ico'))
            msg.setText("Output is null.")
            msg.exec_()
        else:
            pyperclip.copy(text)
            msg = QMessageBox()
            msg.setWindowTitle("Binary Converter")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QtGui.QIcon('icon.ico'))
            msg.setText("Binary code copied on clipboard.")
            msg.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())