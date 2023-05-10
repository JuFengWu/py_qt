from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Form
import time


def buttonClick(event):
    lineEditText = ui.lineEdit.text()
    if(not lineEditText.isnumeric()):
        message_box = QMessageBox()
        message_box.setWindowTitle ("error")
        message_box.setInformativeText("please enter a interger number")
        message_box.exec_()
    else:
        ui.label.setText(lineEditText)
        print(str(event.x()) +"," + str(event.y()) + "," + str(event.button()))

app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Form()
ui.setupUi(widget)

ui.label_2.mouseReleaseEvent = buttonClick

widget.show()
sys.exit(app.exec_())    
    
