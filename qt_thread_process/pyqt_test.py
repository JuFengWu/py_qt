
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog
from time import sleep

class RunningThread(QThread):
    def __init__(self, parent, finalSignal, processSignal):
        super(RunningThread, self).__init__(parent=parent)
        self.finalSignal = finalSignal
        self.processSignal = processSignal
    def run(self):
        i = 0
        while(i<5):
            self.processSignal.emit(i)
            sleep(1)
            i = i + 1
        self.processSignal.emit(i)
        self.finalSignal.emit("finish")

class MainWindow(QMainWindow): 
    finalSignal = pyqtSignal(str)
    processSignal = pyqtSignal(int)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui_connection()
        
        self.finalSignal.connect(self.finish_running)
        self.processSignal.connect(self.process_show)
        self.runningThread = RunningThread(self,self.finalSignal,self.processSignal)
    def ui_connection(self):
        self.ui.pushButton.clicked.connect(self.click_button)
    def click_button(self):
        self.runningThread.start()
        self.ui.label_2.setText("start running")
    @pyqtSlot(str)
    def finish_running(self,msg):
        self.ui.label_2.setText(msg)
    @pyqtSlot(int)
    def process_show(self,currentNumber):
        self.ui.progressBar.setValue(currentNumber*20)
        
def main(args= None):
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
