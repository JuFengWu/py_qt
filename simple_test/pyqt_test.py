from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Form
import time
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.buttonClick)
        
    def buttonClick(self):
        #time.sleep(5) #假設動作很久，睡5秒
        lineEditText = self.ui.lineEdit.text()
        if(not lineEditText.isnumeric()):
            message_box = QMessageBox()
            message_box.setWindowTitle ("error")
            message_box.setInformativeText("please enter a interger number")
            message_box.exec_()
        else:
            self.ui.label.setText(lineEditText)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
