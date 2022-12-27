
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog
from time import sleep
import threading

number = 0

class RunningThread(QThread):
    def __init__(self, parent):
        super(RunningThread, self).__init__(parent=parent)
    def run(self):
        i = 0
        while(i<5):
            process_show(i)
            sleep(1)
            i = i + 1
        process_show(i)
 
def process_show(currentNumber):
    ui.progressBar.setValue(currentNumber*20) 

def click_button():
    thread.start()
    ui.label_2.setText("start running")        
        
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)
ui.pushButton.clicked.connect(click_button)


thread = RunningThread(widget)


widget.show()
sys.exit(app.exec_())    
