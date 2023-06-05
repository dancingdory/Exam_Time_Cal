import sys
import math
import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QLabel, QMessageBox
from PyQt5.QtWidgets import QPushButton, QDialog, QDialogButtonBox
from PyQt5.QtCore import QSize
from PyQt5 import uic
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from decimal import Decimal, ROUND_HALF_UP


class FirstForm(QMainWindow):

    def __init__(self):
        super(FirstForm, self).__init__()
        uic.loadUi('exam_main_win.ui', self)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.openOtherForm)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close)       

    def openOtherForm(self):
        st_time = self.lineEdit.text().split(":")
        #print ("hr:", st_time[0])
        #print ("min:", st_time[1])

        dur_time = self.lineEdit_2.text().split(":")
        t1 = datetime.datetime(2018,1,1,int(st_time[0]),int(st_time[1]),0)
        t2 = datetime.timedelta(hours=int(dur_time[0]), minutes=int(dur_time[1]))
        # calculate end time
        t3 = t1 + t2
        #print("End time:", t3.strftime('%H:%M:%S'))

        #calculate extra time
        extra_dur = 0.25 * (int(dur_time[0]) * 60 + int(dur_time[1]))
        #rdup_extra_dur = Decimal(extra_dur).quantize(0, ROUND_HALF_UP) #mathematical round up
        rdup_extra_dur = math.ceil(extra_dur) #rounding up extra time
        print ("25% extra time ", extra_dur)
        #print("Round up 25% extra time ", rdup_extra_dur)
        
        t_extra_dur = 1.25 * (int(dur_time[0]) * 60 + int(dur_time[1]))
        #rdup_t_extra_dur = Decimal(t_extra_dur).quantize(0, ROUND_HALF_UP)
        rdup_t_extra_dur = math.ceil(t_extra_dur)
        t4 = datetime.timedelta(minutes=int(rdup_t_extra_dur)) #rounding up extra time to minutes to put into timedelta
        #t4 = datetime.timedelta(minutes=t_extra_dur)

        t5 = t1 + t4
        #print("End time with 25% extra time of", rdup_extra_dur, " min: ", t5.strftime('%H:%M:%S'))

        self.hide()
        otherview = SecondForm(self)
        otherview.displayStartTime(self.lineEdit.text())
        otherview.displayDuration(self.lineEdit_2.text())
        otherview.displayEndTime(t3.strftime('%H:%M:%S'))
        otherview.displayExtraTime(str(rdup_extra_dur))
        otherview.displayFinalTime (t5.strftime('%H:%M:%S'))
        otherview.show()

class SecondForm(QDialog):
    st_time = ""
    def __init__(self, parent=None):
        super(SecondForm, self).__init__(parent)
        uic.loadUi('output.ui', self)
        self.button2.clicked.connect(self.goBackToOtherForm)

    def goBackToOtherForm(self):
        self.parent().show()
        self.close()

    def displayStartTime(self, st_time):        
        self.lineEdit.setText(st_time)
        self.lineEdit.displayText()

    def displayDuration (self, dur_time):
        self.lineEdit_2.setText(dur_time)
        self.lineEdit_2.displayText()

    def displayEndTime (self, end_time):
        self.lineEdit_3.setText(end_time)
        self.lineEdit_3.displayText()

    def displayExtraTime (self, extra_time):
        self.lineEdit_5.setText(extra_time)
        self.lineEdit_5.displayText()

    def displayFinalTime (self, final_time):
        self.lineEdit_4.setText(final_time)
        self.lineEdit_4.displayText()

#app = QApplication(sys.argv)
if __name__ == '__main__':
    appc = ApplicationContext()
    main = FirstForm()
    main.show()
    sys.exit(appc.app.exec_())
            
