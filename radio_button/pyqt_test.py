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
        self.checkBox = self.ui.checkBox
        self.checkBox.clicked.connect(self.click_checkbox)
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.addButton(self.ui.radioButton, 1)
        self.buttonGroup.addButton(self.ui.radioButton_2, 2)
        self.ui.radioButton.clicked.connect(self.click_radio_button)
        self.ui.radioButton_2.clicked.connect(self.click_radio_button)
        self.setup_combo_box()
        
    def click_checkbox(self):
        if(self.checkBox.isChecked()):
            self.ui.label_4.setText("check")
        else:
            self.ui.label_4.setText("not check")
            
    def click_radio_button(self):
        if(self.buttonGroup.checkedId() == 1):
            self.ui.label_2.setText("click 1")
        elif(self.buttonGroup.checkedId() == 2):
            self.ui.label_2.setText("click 2")
        else:
            print("error occurt")
            
    def setup_combo_box(self):
        self.ui.comboBox.addItems(['cat','dog','bird'])
        self.ui.pushButton.clicked.connect(self.click_combo_button)
    def click_combo_button(self):
        self.ui.label_6.setText(self.ui.comboBox.currentText())
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
