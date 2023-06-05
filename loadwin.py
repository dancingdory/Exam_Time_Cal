import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QLabel, QMessageBox
from PyQt5.QtWidgets import QPushButton, QDialog
from PyQt5.QtCore import QSize
from PyQt5 import uic

class FirstForm(QMainWindow):

    def __init__(self):
        super(FirstForm, self).__init__()
        uic.loadUi('firstform.ui', self)
        self.button1.clicked.connect(self.openOtherForm)

    def openOtherForm(self):
        self.hide()
        otherview = SecondForm(self)
        otherview.show()

class SecondForm(QDialog):

    def __init__(self, parent=None):
        super(SecondForm, self).__init__(parent)
        uic.loadUi('secondform.ui', self)
        self.button2.clicked.connect(self.goBackToOtherForm)

    def goBackToOtherForm(self):
        self.parent().show()
        self.close()

app = QApplication(sys.argv)
main = FirstForm()
main.show()
sys.exit(app.exec_())
