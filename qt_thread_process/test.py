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
global isRun
isRun = True
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
    global isRun
    timer.start(1000)
    ui.label_2.setText("start running")
    isRun = True
    
def click_button2():
    global isRun
    print("click_button2")
    if(isRun):
        print("is Run")
        isRun = False
        timer.stop()
    else:
        print("is Run is false")
        isRun = True
        timer.start(1000)
        
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
