from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from textEditors import Ui_Dialog
import sys
import time



def buttonClick():
    ui.lineEdit.setText("hello\naaa")
    print(ui.lineEdit.text())
def buttonClick2():
    ui.textEdit.setText("aaa\nbbb")
    print(ui.textEdit.toPlainText())
        
app = QApplication(sys.argv)
t=QTranslator()
t.load('tra_chinese.qm')
app.installTranslator(t)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

ui.pushButton.clicked.connect(buttonClick)
ui.pushButton_2.clicked.connect(buttonClick2)

widget.show()
sys.exit(app.exec_())    
    
