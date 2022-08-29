
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog
from time import sleep
import threading

          
def run():
    i = 0
    while(i<5):
        ui.progressBar.setValue(i*20)
        sleep(1)
        i = i + 1
    ui.progressBar.setValue(i*20)
    ui.label_2.setText("finish")      
        
def click_button(self):
    runningThread = threading.Thread(target = run)   
    runningThread.start()
    ui.label_2.setText("start running")        
        
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)
ui.pushButton.clicked.connect(click_button)

widget.show()
sys.exit(app.exec_())    
