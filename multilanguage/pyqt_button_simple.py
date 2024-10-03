from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog
import time


def buttonClick():
    #time.sleep(5) #假設動作很久，睡5秒
    IDlineEditText = ui.IDlineEdit.text()
    if(not IDlineEditText.isnumeric()):
        message_box = QMessageBox()
        
        message_box.setWindowTitle(trans["error"])
        message_box.setInformativeText("please enter a interger number")
        message_box.exec_()
    else:
        ui.IDlabel.setText(IDlineEditText)
def buttonClick2():
    print("xxx")

import csv

# 初始化兩個字典
eng_to_chi = {}
eng_to_deu = {}
eng = {}

# 讀取 CSV 檔案
with open('language_table.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        print(row)
        english = row['eng']
        chinese = row['chi']
        german = row['deu']
        eng_to_chi[english] = chinese
        eng_to_deu[english] = german
        eng[english] = english

with open('current_language.txt', mode='r', encoding='utf-8') as file:
    txt = file.readline()
    print(txt)
    if txt == "chi":
        trans = eng_to_chi
    elif txt == "deu":
        trans = eng_to_deu
    else:
        trans = eng

app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

ui.IDlabel.setText(trans["Set ID"])

setIDButton = ui.setIDButton
setIDButton.clicked.connect(buttonClick)
setIDButton.clicked.connect(buttonClick2)
widget.show()
sys.exit(app.exec_())    
    
