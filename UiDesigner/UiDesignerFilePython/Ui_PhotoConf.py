# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PhotoConf.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from CheckBoxSpecial import checkboxSpecial

class Ui_PhotoConf(object):
    def setupUi(self, PhotoConf, observableCount):
        PhotoConf.setObjectName("PhotoConf")
        PhotoConf.resize(771, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PhotoConf.sizePolicy().hasHeightForWidth())
        PhotoConf.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(PhotoConf)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 19)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkButton = checkboxSpecial(observableCount, PhotoConf)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkButton.sizePolicy().hasHeightForWidth())
        self.checkButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.checkButton.setFont(font)
        self.checkButton.setText("")
        self.checkButton.setObjectName("checkButton")
        self.horizontalLayout.addWidget(self.checkButton)
        self.photoPreview = QtWidgets.QWidget(PhotoConf)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoPreview.sizePolicy().hasHeightForWidth())
        self.photoPreview.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.photoPreview.setFont(font)
        self.photoPreview.setObjectName("photoPreview")
        self.horizontalLayout.addWidget(self.photoPreview)
        self.photoWeigth = QtWidgets.QWidget(PhotoConf)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoWeigth.sizePolicy().hasHeightForWidth())
        self.photoWeigth.setSizePolicy(sizePolicy)
        self.photoWeigth.setObjectName("photoWeigth")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.photoWeigth)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelWeigth = QtWidgets.QLabel(self.photoWeigth)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelWeigth.sizePolicy().hasHeightForWidth())
        self.labelWeigth.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.labelWeigth.setFont(font)
        self.labelWeigth.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelWeigth.setObjectName("labelWeigth")
        self.horizontalLayout_2.addWidget(self.labelWeigth)
        self.valueWeigth = QtWidgets.QSpinBox(self.photoWeigth)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valueWeigth.sizePolicy().hasHeightForWidth())
        self.valueWeigth.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.valueWeigth.setFont(font)
        self.valueWeigth.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.valueWeigth.setAlignment(QtCore.Qt.AlignCenter)
        self.valueWeigth.setMinimum(1)
        self.valueWeigth.setMaximum(3)
        self.valueWeigth.setObjectName("valueWeigth")
        self.horizontalLayout_2.addWidget(self.valueWeigth)
        self.horizontalLayout.addWidget(self.photoWeigth)

        self.retranslateUi(PhotoConf)
        QtCore.QMetaObject.connectSlotsByName(PhotoConf)

    def retranslateUi(self, PhotoConf):
        _translate = QtCore.QCoreApplication.translate
        PhotoConf.setWindowTitle(_translate("PhotoConf", "PhotoConf"))
        self.labelWeigth.setText(_translate("PhotoConf", " Importance [1:3] :   "))

