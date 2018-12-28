# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProgressBarDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProgressBarDialog(object):
    def setupUi(self, ProgressBarDialog):
        ProgressBarDialog.setObjectName("ProgressBarDialog")
        ProgressBarDialog.setEnabled(True)
        ProgressBarDialog.resize(434, 64)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProgressBarDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(ProgressBarDialog)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(ProgressBarDialog)
        QtCore.QMetaObject.connectSlotsByName(ProgressBarDialog)

    def retranslateUi(self, ProgressBarDialog):
        _translate = QtCore.QCoreApplication.translate
        ProgressBarDialog.setWindowTitle(_translate("ProgressBarDialog", "Making Collages..."))

