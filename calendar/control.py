from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
from calendar import Ui_Dialog
import time

def showDate(date):
    print(date)
    selectDay = ui.calendarWidget.selectedDate()

    print("pyQT day",selectDay)
    print("normal day", selectDay.toString(Qt.ISODate))
    cell_format = QTextCharFormat()
    if backGroundColor:
        cell_format.setBackground(QColor("red"))
    else:
        cell_format.setBackground(QColor("white"))
    ui.calendarWidget.setDateTextFormat(selectDay, cell_format)

def change_back_ground():
    global backGroundColor
    backGroundColor = not backGroundColor
    #if backGroundColor:
    #    backGroundColor = False
    #else:
    #    backGroundColor = True
    
backGroundColor = True
        
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

ui.calendarWidget.setGridVisible(True)
ui.calendarWidget.clicked.connect(showDate)

ui.pushButton.clicked.connect(change_back_ground)

widget.show()
sys.exit(app.exec_())    
