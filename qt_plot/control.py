from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from qt_plot import Ui_Dialog
import time
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


def buttonClick():
    dr = MyFigureCanvas()
    dr.test()
    graphicscene = QtWidgets.QGraphicsScene()
    graphicscene.addWidget(dr)
    ui.graphicsView.setScene(graphicscene) 
    ui.graphicsView.show()
def buttonClick2():
    dr = MyFigureCanvas()
    x = [1,2,3,4,5,6,7,8,9]
    y = [12,4,17,19,45,21,11,2,3]
    dr.test2(x,y)
    graphicscene = QtWidgets.QGraphicsScene()
    graphicscene.addWidget(dr)
    ui.graphicsView.setScene(graphicscene) 
    ui.graphicsView.show()
    
class MyFigureCanvas(FigureCanvas):  

    def __init__(self, parent=None, width=11, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)  
        FigureCanvas.__init__(self, fig) 
        self.setParent(parent)
        self.axes = fig.add_subplot(111)
    def test(self):
        x = [1,2,3,4,5,6,7,8,9]
        y = [23,21,32,13,3,13,13,3,1]
        self.axes.plot(x, y)
    def test2(self,x,y):
        self.axes.plot(x, y)
    

app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

ui.pushButton.clicked.connect(buttonClick)
ui.pushButton_2.clicked.connect(buttonClick2)

widget.show()
sys.exit(app.exec_())    
    
