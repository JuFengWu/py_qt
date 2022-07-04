#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import cv2
import os
from PyQt5.QtWidgets import QApplication, QMainWindow , QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from mainwindow import Ui_Dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.imageFile = "./Lenna.jpg"
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui_connection()
        
    def ui_connection(self):
        image = cv2.imread(self.imageFile)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        qImage = QImage(image, image.shape[1],image.shape[0],image.strides[0], QImage.Format_RGB888)
        self.ui.imageLabel.setPixmap(QPixmap.fromImage(qImage))
        self.ui.imageLabel.setFixedSize(image.shape[1],image.shape[0])
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
