from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from file_folder import Ui_Dialog
import time


def buttonClick():
    outputFolderName = QtWidgets.QFileDialog.getExistingDirectory()
    print(outputFolderName)
    ui.lineEdit.setText(outputFolderName)

def buttonClick2():
    #filename , _ = QtWidgets.QFileDialog.getOpenFileNames(filter='py (*.py)')
    filename , _ = QtWidgets.QFileDialog.getOpenFileNames()
    ui.lineEdit_2.setText(filename[0])
    
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)


ui.pushButton.clicked.connect(buttonClick)
ui.pushButton_2.clicked.connect(buttonClick2)


widget.show()
sys.exit(app.exec_())     
