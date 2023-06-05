from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from ui1 import Ui_FirstUI
from ui2 import Ui_ui2
import time


def buttonClick():
    widget2.show()
    #widget.close()

def clickHello():
    print("clickHello")

def clickHello2():
    print("clickHello2")

app = QApplication(sys.argv)

widget2 = QWidget() # or whatever your top-level class is
ui2 = Ui_ui2()
ui2.setupUi(widget2)
ui2.pushButton.clicked.connect(clickHello2)

widget = QWidget()
ui1 = Ui_FirstUI()
ui1.setupUi(widget)
ui1.pushButton.clicked.connect(buttonClick)
ui1.helloButton.clicked.connect(clickHello)
widget.show()
sys.exit(app.exec_())   