# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ui2(object):
    def setupUi(self, ui2):
        ui2.setObjectName("ui2")
        ui2.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(ui2)
        self.pushButton.setGeometry(QtCore.QRect(120, 160, 121, 51))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ui2)
        QtCore.QMetaObject.connectSlotsByName(ui2)

    def retranslateUi(self, ui2):
        _translate = QtCore.QCoreApplication.translate
        ui2.setWindowTitle(_translate("ui2", "Dialog"))
        self.pushButton.setText(_translate("ui2", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui2 = QtWidgets.QDialog()
    ui = Ui_ui2()
    ui.setupUi(ui2)
    ui2.show()
    sys.exit(app.exec_())