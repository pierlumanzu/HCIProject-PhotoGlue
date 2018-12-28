# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChosenBackgroundGradient.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChosenBackgroundGradient(object):
    def setupUi(self, ChosenBackgroundGradient):
        ChosenBackgroundGradient.setObjectName("ChosenBackgroundGradient")
        ChosenBackgroundGradient.resize(366, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChosenBackgroundGradient)
        self.verticalLayout.setObjectName("verticalLayout")
        self.firstColorArea = QtWidgets.QWidget(ChosenBackgroundGradient)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstColorArea.sizePolicy().hasHeightForWidth())
        self.firstColorArea.setSizePolicy(sizePolicy)
        self.firstColorArea.setObjectName("firstColorArea")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.firstColorArea)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.firstDialogButton = QtWidgets.QPushButton(self.firstColorArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstDialogButton.sizePolicy().hasHeightForWidth())
        self.firstDialogButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.firstDialogButton.setFont(font)
        self.firstDialogButton.setObjectName("firstDialogButton")
        self.horizontalLayout.addWidget(self.firstDialogButton)
        self.firstColorPreview = QtWidgets.QFrame(self.firstColorArea)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.firstColorPreview.setFont(font)
        self.firstColorPreview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.firstColorPreview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.firstColorPreview.setObjectName("firstColorPreview")
        self.horizontalLayout.addWidget(self.firstColorPreview)
        self.verticalLayout.addWidget(self.firstColorArea)
        self.secondColorArea = QtWidgets.QWidget(ChosenBackgroundGradient)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondColorArea.sizePolicy().hasHeightForWidth())
        self.secondColorArea.setSizePolicy(sizePolicy)
        self.secondColorArea.setObjectName("secondColorArea")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.secondColorArea)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.secondDialogButton = QtWidgets.QPushButton(self.secondColorArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondDialogButton.sizePolicy().hasHeightForWidth())
        self.secondDialogButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.secondDialogButton.setFont(font)
        self.secondDialogButton.setObjectName("secondDialogButton")
        self.horizontalLayout_2.addWidget(self.secondDialogButton)
        self.secondColorPreview = QtWidgets.QFrame(self.secondColorArea)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.secondColorPreview.setFont(font)
        self.secondColorPreview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.secondColorPreview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.secondColorPreview.setObjectName("secondColorPreview")
        self.horizontalLayout_2.addWidget(self.secondColorPreview)
        self.verticalLayout.addWidget(self.secondColorArea)

        self.retranslateUi(ChosenBackgroundGradient)
        QtCore.QMetaObject.connectSlotsByName(ChosenBackgroundGradient)

    def retranslateUi(self, ChosenBackgroundGradient):
        _translate = QtCore.QCoreApplication.translate
        ChosenBackgroundGradient.setWindowTitle(_translate("ChosenBackgroundGradient", "ChosenBackgroundGradient"))
        self.firstDialogButton.setText(_translate("ChosenBackgroundGradient", "Choose first color"))
        self.secondDialogButton.setText(_translate("ChosenBackgroundGradient", "Choose second color"))

