# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BackgroundImageConf.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BackgroundImageConf(object):
    def setupUi(self, BackgroundImageConf):
        BackgroundImageConf.setObjectName("BackgroundImageConf")
        BackgroundImageConf.resize(760, 438)
        self.verticalLayout = QtWidgets.QVBoxLayout(BackgroundImageConf)
        self.verticalLayout.setObjectName("verticalLayout")
        self.backgroundImageSettingsArea = QtWidgets.QWidget(BackgroundImageConf)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backgroundImageSettingsArea.sizePolicy().hasHeightForWidth())
        self.backgroundImageSettingsArea.setSizePolicy(sizePolicy)
        self.backgroundImageSettingsArea.setObjectName("backgroundImageSettingsArea")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.backgroundImageSettingsArea)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backgroundImageLabel = QtWidgets.QLabel(self.backgroundImageSettingsArea)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.backgroundImageLabel.setFont(font)
        self.backgroundImageLabel.setObjectName("backgroundImageLabel")
        self.horizontalLayout.addWidget(self.backgroundImageLabel)
        self.backgroundImagePath = QtWidgets.QLineEdit(self.backgroundImageSettingsArea)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.backgroundImagePath.setFont(font)
        self.backgroundImagePath.setObjectName("backgroundImagePath")
        self.horizontalLayout.addWidget(self.backgroundImagePath)
        self.verticalLayout.addWidget(self.backgroundImageSettingsArea)
        self.backgroundImagePreviewArea = QtWidgets.QWidget(BackgroundImageConf)
        self.backgroundImagePreviewArea.setObjectName("backgroundImagePreviewArea")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.backgroundImagePreviewArea)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backgroundImagePreview = QtWidgets.QWidget(self.backgroundImagePreviewArea)
        self.backgroundImagePreview.setObjectName("backgroundImagePreview")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.backgroundImagePreview)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.backgroundImagePreviewLayout = QtWidgets.QVBoxLayout()
        self.backgroundImagePreviewLayout.setObjectName("backgroundImagePreviewLayout")
        self.verticalLayout_4.addLayout(self.backgroundImagePreviewLayout)
        self.horizontalLayout_2.addWidget(self.backgroundImagePreview)
        self.imagewidthHeightArea = QtWidgets.QWidget(self.backgroundImagePreviewArea)
        self.imagewidthHeightArea.setObjectName("imagewidthHeightArea")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.imagewidthHeightArea)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelImageWidth = QtWidgets.QLabel(self.imagewidthHeightArea)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.labelImageWidth.setFont(font)
        self.labelImageWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImageWidth.setObjectName("labelImageWidth")
        self.verticalLayout_2.addWidget(self.labelImageWidth)
        self.labelImageHeight = QtWidgets.QLabel(self.imagewidthHeightArea)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.labelImageHeight.setFont(font)
        self.labelImageHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImageHeight.setObjectName("labelImageHeight")
        self.verticalLayout_2.addWidget(self.labelImageHeight)
        self.horizontalLayout_2.addWidget(self.imagewidthHeightArea)
        self.verticalLayout.addWidget(self.backgroundImagePreviewArea)

        self.retranslateUi(BackgroundImageConf)
        QtCore.QMetaObject.connectSlotsByName(BackgroundImageConf)

    def retranslateUi(self, BackgroundImageConf):
        _translate = QtCore.QCoreApplication.translate
        BackgroundImageConf.setWindowTitle(_translate("BackgroundImageConf", "BackgroundImageConf"))
        self.backgroundImageLabel.setText(_translate("BackgroundImageConf", "Background Path : "))
        self.labelImageWidth.setText(_translate("BackgroundImageConf", "Width :  0"))
        self.labelImageHeight.setText(_translate("BackgroundImageConf", "Height :  0"))

