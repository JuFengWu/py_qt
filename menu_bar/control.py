from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from menu_bar import Ui_MainWindow


def setting():
    ui.label.setText("click setting")
    
def save():
    ui.label.setText("click save")

def save_all():
    ui.label.setText("click save_all")

def load():
    ui.label.setText("click load")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui.actionsetting.triggered.connect(setting)
ui.actionsave.triggered.connect(save)
ui.actionsave_all.triggered.connect(save_all)
ui.actionload.triggered.connect(load)

MainWindow.show()
sys.exit(app.exec_())
    
