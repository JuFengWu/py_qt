from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui_connection()
        
    def ui_connection(self):
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(65)
        self.ui.horizontalSlider.setMaximum(120)
        self.ui.horizontalSlider.valueChanged.connect(self.value_change)
        self.ui.horizontalSlider.sliderReleased.connect(self.show_release)
        
    def value_change(self):
        self.ui.progressBar.setValue(self.ui.horizontalSlider.value())
    def show_release(self):
        message_box = QMessageBox()
        message_box.setWindowTitle ("final slidbar value")
        message_box.setInformativeText(str(self.ui.horizontalSlider.value()))
        message_box.exec_()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
