from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog
import time
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui_connection()
        
    def ui_connection(self):
        self.setIDButton = self.ui.setIDButton
        self.setIDButton.clicked.connect(self.buttonClick)
        
    def buttonClick(self):
        #time.sleep(5) #假設動作很久，睡5秒
        IDlineEditText = self.ui.IDlineEdit.text()
        if(not IDlineEditText.isnumeric()):
            message_box = QMessageBox()
            message_box.setWindowTitle (self.tr("error"))
            message_box.setInformativeText(self.tr("please enter a interger number"))
            message_box.exec_()
        else:
            self.ui.IDlabel.setText(IDlineEditText)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
