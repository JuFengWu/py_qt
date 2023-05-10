from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow_1 import Ui_Dialog_1
from mainwindow_2 import Ui_Dialog_2
import time


def buttonClick():
    widget2.show()

app = QApplication(sys.argv)

widget2 = QWidget() # or whatever your top-level class is
ui2 = Ui_Dialog_2()
ui2.setupUi(widget2)

widget = QWidget()
ui = Ui_Dialog_1()
ui.setupUi(widget)
setIDButton = ui.setIDButton
setIDButton.clicked.connect(buttonClick)
widget.show()
sys.exit(app.exec_())   