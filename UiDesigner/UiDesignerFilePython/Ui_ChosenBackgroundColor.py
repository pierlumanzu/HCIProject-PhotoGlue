# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChosenBackgroundColor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChosenBackgroundColor(object):
    def setupUi(self, ChosenBackgroundColor):
        ChosenBackgroundColor.setObjectName("ChosenBackgroundColor")
        ChosenBackgroundColor.resize(366, 125)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ChosenBackgroundColor)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dialogButton = QtWidgets.QPushButton(ChosenBackgroundColor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialogButton.sizePolicy().hasHeightForWidth())
        self.dialogButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.dialogButton.setFont(font)
        self.dialogButton.setObjectName("dialogButton")
        self.horizontalLayout.addWidget(self.dialogButton)
        self.colorPreview = QtWidgets.QFrame(ChosenBackgroundColor)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.colorPreview.setFont(font)
        self.colorPreview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.colorPreview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.colorPreview.setObjectName("colorPreview")
        self.horizontalLayout.addWidget(self.colorPreview)

        self.retranslateUi(ChosenBackgroundColor)
        QtCore.QMetaObject.connectSlotsByName(ChosenBackgroundColor)

    def retranslateUi(self, ChosenBackgroundColor):
        _translate = QtCore.QCoreApplication.translate
        ChosenBackgroundColor.setWindowTitle(_translate("ChosenBackgroundColor", "ChosenBackgroundColor"))
        self.dialogButton.setText(_translate("ChosenBackgroundColor", "Choose color"))

