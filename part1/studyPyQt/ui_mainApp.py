# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\source\miniprojects\part1\studyPyQt\mainApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(281, 162)
        Form.setMinimumSize(QtCore.QSize(281, 162))
        Form.setMaximumSize(QtCore.QSize(281, 162))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.lblMessage = QtWidgets.QLabel(Form)
        self.lblMessage.setGeometry(QtCore.QRect(10, 10, 250, 30))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setBold(False)
        font.setWeight(50)
        self.lblMessage.setFont(font)
        self.lblMessage.setObjectName("lblMessage")
        self.btnOK = QtWidgets.QPushButton(Form)
        self.btnOK.setGeometry(QtCore.QRect(200, 135, 75, 23))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setBold(False)
        font.setWeight(50)
        self.btnOK.setFont(font)
        self.btnOK.setObjectName("btnOK")
        self.btnPOP = QtWidgets.QPushButton(Form)
        self.btnPOP.setGeometry(QtCore.QRect(10, 135, 75, 23))
        font = QtGui.QFont()
        font.setFamily("NanumGothic")
        font.setBold(False)
        font.setWeight(50)
        self.btnPOP.setFont(font)
        self.btnPOP.setObjectName("btnPOP")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ":):"))
        self.lblMessage.setText(_translate("Form", "메시지:"))
        self.btnOK.setText(_translate("Form", "OK"))
        self.btnPOP.setText(_translate("Form", "popUP"))
