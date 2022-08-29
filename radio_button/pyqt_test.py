from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog

        
def click_checkbox():
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
            
def click_combo_button():
    ui.label_6.setText(ui.comboBox.currentText())
    
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

checkBox = ui.checkBox
checkBox.clicked.connect(click_checkbox)

buttonGroup = QButtonGroup(widget)
buttonGroup.addButton(ui.radioButton, 1)
buttonGroup.addButton(ui.radioButton_2, 2)
ui.radioButton.clicked.connect(click_radio_button)
ui.radioButton_2.clicked.connect(click_radio_button)

ui.comboBox.addItems(['cat','dog','bird'])
ui.pushButton.clicked.connect(click_combo_button)
widget.show()
sys.exit(app.exec_())   
