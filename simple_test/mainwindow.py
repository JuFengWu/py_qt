# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.setIDButton = QtWidgets.QPushButton(Dialog)
        self.setIDButton.setGeometry(QtCore.QRect(150, 210, 89, 25))
        self.setIDButton.setObjectName("setIDButton")
        self.showIDLabel = QtWidgets.QLabel(Dialog)
        self.showIDLabel.setGeometry(QtCore.QRect(110, 90, 81, 17))
        self.showIDLabel.setObjectName("showIDLabel")
        self.IDlabel = QtWidgets.QLabel(Dialog)
        self.IDlabel.setGeometry(QtCore.QRect(210, 90, 31, 17))
        self.IDlabel.setObjectName("IDlabel")
        self.IDlineEdit = QtWidgets.QLineEdit(Dialog)
        self.IDlineEdit.setGeometry(QtCore.QRect(180, 150, 113, 25))
        self.IDlineEdit.setObjectName("IDlineEdit")
        self.changeIDLabel = QtWidgets.QLabel(Dialog)
        self.changeIDLabel.setGeometry(QtCore.QRect(80, 150, 81, 17))
        self.changeIDLabel.setObjectName("changeIDLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.setIDButton.setText(_translate("Dialog", "Set ID"))
        self.showIDLabel.setText(_translate("Dialog", "Current ID :"))
        self.IDlabel.setText(_translate("Dialog", "90"))
        self.changeIDLabel.setText(_translate("Dialog", "Change ID :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
