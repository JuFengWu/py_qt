from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog
from time import sleep
import threading

number = 0
global timer
def count_sheep():
    print("do timer")
    global number
    number += 1
    process_show(number)
    if(number==5):
        timer.stop()
        number = 0
 
def process_show(currentNumber):
    ui.progressBar.setValue(currentNumber*20) 

def click_button():
    timer.start(1000)
    ui.label_2.setText("start running")
    
def click_button2():
    message_box = QMessageBox()
    message_box.setWindowTitle ("error")
    message_box.setInformativeText("hello")
    message_box.exec_()
        
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)
ui.pushButton.clicked.connect(click_button)
ui.pushButton_2.clicked.connect(click_button2)

timer = QTimer()
timer.timeout.connect(count_sheep)

widget.show()
sys.exit(app.exec_())    
