
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainwindow import Ui_Dialog
from time import sleep

class RunningThread(QThread):
    def __init__(self, parent, signal):
        super(RunningThread, self).__init__(parent=parent)
        self.signal = signal
    def run(self):
        sleep(5)
        self.signal.emit("end running")

class MainWindow(QMainWindow): 
    signal = pyqtSignal(str)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui_connection()
        
        self.signal.connect(self.finish_running)
        self.runningThread = RunningThread(self,self.signal)
    def ui_connection(self):
        self.ui.pushButton.clicked.connect(self.click_button)
    def click_button(self):
        self.runningThread.start()
        self.ui.label_2.setText("start running")
    @pyqtSlot(str)
    def finish_running(self,msg):
        self.ui.label_2.setText(msg)
    
        
def main(args= None):
    
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
