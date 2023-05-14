#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import cv2
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QImage, QPixmap
from mainwindow import Ui_Dialog
    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget =  QWidget()
    ui = Ui_Dialog()
    ui.setupUi(widget)

    imageFile = "./Lenna.jpg"
    image = cv2.imread(imageFile)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    qImage = QImage(image, image.shape[1],image.shape[0],image.strides[0], QImage.Format_RGB888)
    ui.imageLabel.setPixmap(QPixmap.fromImage(qImage))
    ui.imageLabel.setFixedSize(image.shape[1],image.shape[0])

    widget.show()
    sys.exit(app.exec_())
