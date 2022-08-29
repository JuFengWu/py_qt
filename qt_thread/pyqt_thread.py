
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog
from time import sleep
import threading
    
    

def run():
   sleep(1)
   ui.label_2.setText("end run")  
def click_button():
    runningThread = threading.Thread(target = run)   
    runningThread.start()
    ui.label_2.setText("start run")
   
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)
ui.pushButton.clicked.connect(click_button)

widget.show()
sys.exit(app.exec_())    
