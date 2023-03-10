import sys

import pyperclip
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        width = 315
        height = 130
        Form.setFixedSize(width, height)
        Form.setObjectName("Form")
        Form.resize(312, 121)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.input = QtWidgets.QLineEdit(Form)
        self.input.setGeometry(QtCore.QRect(10, 10, 291, 22))
        self.input.setStyleSheet("color: rgb(255, 255, 255);")
        self.input.setAlignment(QtCore.Qt.AlignCenter)
        self.input.setObjectName("input")
        self.output = QtWidgets.QLabel(Form)
        self.output.setGeometry(QtCore.QRect(10, 80, 291, 31))
        self.output.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output.setText("")
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 295, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textCode = QtWidgets.QPushButton(self.layoutWidget)
        self.textCode.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textCode.setObjectName("textCode")
        self.horizontalLayout.addWidget(self.textCode)
        self.copy = QtWidgets.QPushButton(self.layoutWidget)
        self.copy.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.copy.setObjectName("copy")
        self.horizontalLayout.addWidget(self.copy)
        self.codeText = QtWidgets.QPushButton(self.layoutWidget)
        self.codeText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.codeText.setObjectName("codeText")
        self.horizontalLayout.addWidget(self.codeText)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.input.setPlaceholderText(_translate("Form", "Enter the text or code"))
        self.textCode.setText(_translate("Form", "Text to Code"))
        self.copy.setText(_translate("Form", "Copy"))
        self.codeText.setText(_translate("Form", "Code to Text"))
        self.copy.clicked.connect(lambda: self.copy_out())
        self.textCode.clicked.connect(lambda: self.text_to_code())
        self.codeText.clicked.connect(lambda: self.code_to_text())

    def text_to_code(self):
        txt = self.input.text()

        encrypt = {'A': '.-', 'B': '-...', 'C': '-.-.',
                   'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....', 'I': '..',
                   'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.',
                   'S': '...', 'T': '-', 'U': '..-',
                   'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', ' ': '.....'}
        message =  ' '.join(encrypt[i] for i in txt.upper())
        print(message)
        self.output.setText(message)

    def code_to_text(self):
        txt = self.input.text()
        encrypt = {'A': '.-', 'B': '-...', 'C': '-.-.',
                   'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....', 'I': '..',
                   'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.',
                   'S': '...', 'T': '-', 'U': '..-',
                   'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', ' ': '.....'}
        decrypt = {v: k for k, v in encrypt.items()}

        if '-' in txt:
            message =  ''.join(decrypt[i] for i in txt.split())
            self.output.setText(message)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Morse Converter")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Wrong")
            msg.exec_()

    def copy_out(self):
        text = self.output.text()
        pyperclip.copy(text)
        msg = QMessageBox()
        msg.setWindowTitle("MorseConverter")
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Copied on clipboard.")
        msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
