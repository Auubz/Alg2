# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(549, 436)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.userinput = QtWidgets.QLineEdit(Dialog)
        self.userinput.setGeometry(QtCore.QRect(20, 60, 181, 31))
        self.userinput.setObjectName("userinput")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.Result = QtWidgets.QLabel(Dialog)
        self.Result.setGeometry(QtCore.QRect(80, 250, 111, 61))
        self.Result.setObjectName("Result")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.button_pressed)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter your Name:"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.Result.setText(_translate("Dialog", ""))

    def button_pressed(self):
        self.Result.setText("Hello " + self.userinput.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)


    Dialog.show()
    sys.exit(app.exec_())

