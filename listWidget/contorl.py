from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from listwidget import Ui_Dialog
import time

def click_button():
    value = ui.listWidget.currentRow()
 
       
    print("Current Selected Row : " + str(value))
        
app = QApplication(sys.argv)
t=QTranslator()
t.load('tra_chinese.qm')
app.installTranslator(t)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

ui.listWidget.addItems(['A','B','C','D'])
ui.listWidget.addItem('X')
item = ui.listWidget.takeItem(1)       # 取得第二個項目，也就是 B
ui.listWidget.removeItemWidget(item)   # 移除第二個項目

ui.pushButton.clicked.connect(click_button)

widget.show()
sys.exit(app.exec_())    
