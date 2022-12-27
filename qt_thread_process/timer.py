from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog
from time import sleep
import threading

number = 0

def count_sheep():
    global number
    number += 1
    process_show(number)
    if(number):
        timer.stop()
        number = 0
 
def process_show(currentNumber):
    ui.progressBar.setValue(currentNumber*20) 

def click_button():
    timer.start(500)
    ui.label_2.setText("start running")        
        
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)
ui.pushButton.clicked.connect(click_button)


timer = QTimer()
timer.timeout.connect(count_sheep)

widget.show()
sys.exit(app.exec_())    