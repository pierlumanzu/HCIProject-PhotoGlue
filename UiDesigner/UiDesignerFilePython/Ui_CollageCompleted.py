# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CollageCompleted.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CollageCompleted(object):
    def setupUi(self, CollageCompleted):
        CollageCompleted.setObjectName("CollageCompleted")
        CollageCompleted.resize(484, 204)
        self.successfulLabel = QtWidgets.QLabel(CollageCompleted)
        self.successfulLabel.setGeometry(QtCore.QRect(50, 40, 381, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        self.successfulLabel.setFont(font)
        self.successfulLabel.setObjectName("successfulLabel")
        self.okButton = QtWidgets.QPushButton(CollageCompleted)
        self.okButton.setGeometry(QtCore.QRect(340, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.folderButton = QtWidgets.QPushButton(CollageCompleted)
        self.folderButton.setGeometry(QtCore.QRect(190, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.folderButton.setFont(font)
        self.folderButton.setObjectName("folderButton")

        self.retranslateUi(CollageCompleted)
        QtCore.QMetaObject.connectSlotsByName(CollageCompleted)

    def retranslateUi(self, CollageCompleted):
        _translate = QtCore.QCoreApplication.translate
        CollageCompleted.setWindowTitle(_translate("CollageCompleted", "Collage Completed"))
        self.successfulLabel.setText(_translate("CollageCompleted", "Collages created successfully."))
        self.okButton.setText(_translate("CollageCompleted", "OK"))
        self.folderButton.setText(_translate("CollageCompleted", "Go to the Folder"))

