from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog
import time


def buttonClick():
    #time.sleep(5) #假設動作很久，睡5秒
    IDlineEditText = ui.IDlineEdit.text()
    if(not IDlineEditText.isnumeric()):
        message_box = QMessageBox()
        message_box.setWindowTitle ("error")
        message_box.setInformativeText("please enter a interger number")
        message_box.exec_()
    else:
        ui.IDlabel.setText(IDlineEditText)
def buttonClick2():
    print("xxx")
    
        
app = QApplication(sys.argv)
t=QTranslator()
t.load('tra_chinese.qm')
app.installTranslator(t)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)
setIDButton = ui.setIDButton
setIDButton.clicked.connect(buttonClick)
setIDButton.clicked.connect(buttonClick2)
widget.show()
sys.exit(app.exec_())    
    
