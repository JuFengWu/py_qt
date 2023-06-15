from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from listwidget import Ui_Dialog
import time
import threading

def my_job():
    print("thread start")
    time.sleep(1)
    ui.listWidget.addItem('Y')
    print("finish thread sleep 1")
    time.sleep(1)
    ui.listWidget.addItem('Z')

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

firstThread = threading.Thread(target = my_job) #threading.Thread是class
firstThread.start()

ui.listWidget.addItems(['A','B','C','D'])
ui.listWidget.addItem('X')
item = ui.listWidget.takeItem(1)       # 取得第二個項目，也就是 B
ui.listWidget.removeItemWidget(item)   # 移除第二個項目

ui.pushButton.clicked.connect(click_button)

widget.show()
sys.exit(app.exec_())    
