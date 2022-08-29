from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog


def value_change():
    ui.progressBar.setValue(ui.horizontalSlider.value())
def show_release():
    message_box = QMessageBox()
    message_box.setWindowTitle ("final slidbar value")
    message_box.setInformativeText(str(ui.horizontalSlider.value()))
    message_box.exec_()
    
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)
ui.progressBar.setMinimum(0)
ui.progressBar.setMaximum(100)
ui.progressBar.setValue(65)
ui.horizontalSlider.setMaximum(120)
ui.horizontalSlider.valueChanged.connect(value_change)
ui.horizontalSlider.sliderReleased.connect(show_release)
widget.show()
sys.exit(app.exec_())    
