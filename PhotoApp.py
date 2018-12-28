from PyQt5.QtWidgets import QMainWindow
from multiprocessing import Process
import os
import sys
sys.path.append("OptimizationProblem/")
from MilpForPhotos import *
sys.path.append("UiDesigner/UiDesignerFilePython/")
from Ui_PhotoApp import Ui_PhotoApp
from PhotoConf import PhotoConf
from BackgroundConf import BackgroundImageConf, BackgroundCustomConf
from Dialogs import ProgressBarDialog, CollageCompleted
from Observable import Observable

class PhotoApp(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_PhotoApp()
        self.ui.setupUi(self)

        self.ui.refreshButton.clicked.connect(self.insertPhotoConf)

        self.countPhotos = Observable(0)
        self.countPhotos.observe(self.updateStatusBar)

        self.ui.imageChoice.clicked.connect(self.setBackgroundChoice)
        self.ui.imageChoice.clicked.connect(self.updateStatusBar)
        self.ui.customChoice.clicked.connect(self.setBackgroundChoice)
        self.ui.customChoice.clicked.connect(self.updateStatusBar)

        self.ui.makeCollageButton.clicked.connect(self.makeCollageControl)

    def insertPhotoConf(self):

        if os.path.isdir(self.ui.folderPath.text()):

            self.ui.statusBar.setStyleSheet("color:black;")
            self.ui.statusBar.showMessage("Number of selected Photos (min 2-max 15): {}".format(self.countPhotos.value))

            photoInListArray = []
            for i in reversed(range(self.ui.photoList.count())):
                if not(self.ui.photoList.itemAt(i).widget().ui.checkButton.isChecked()):
                    self.ui.photoList.itemAt(i).widget().setParent(None)
                else:
                    photoInListArray.append(self.ui.photoList.itemAt(i).widget().filePath)

            fileList = os.listdir(self.ui.folderPath.text())
            for fileName in fileList:
                if fileName.lower().endswith(('.png', '.jpg', '.jpeg')) and (self.ui.folderPath.text() + "/" + fileName) not in photoInListArray:
                    photoConf = PhotoConf(self.ui.folderPath.text() + "/" + fileName, self.countPhotos)
                    self.ui.photoList.addWidget(photoConf)
            self.ui.labelRefreshRelated.clear()
        else:
            self.ui.statusBar.setStyleSheet("color:red;")
            self.ui.statusBar.showMessage("Please insert a directory path. Number of selected Photos (min 2-max 15): {}".format(self.countPhotos.value))

    def backgroundControlForStatusBar(self):
        if os.path.exists(self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.backgroundImagePath.text()) and self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.backgroundImagePath.text().lower().endswith(('.png', '.jpg', '.jpeg')):
            self.updateStatusBar()

    def colorBackgroundControlForStatusBar(self):
        if self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.colorChoice.isChecked() and self.countColors.value == 1:
            self.updateStatusBar()
        if self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.gradientChoice.isChecked() and self.countColors.value == 2:
            self.updateStatusBar()

    def updateStatusBar(self):
        self.ui.statusBar.setStyleSheet("color:black;")
        self.ui.statusBar.showMessage("Number of selected Photos (min 2-max 15): {}".format(self.countPhotos.value))

    def setBackgroundChoice(self):

        for i in reversed(range(self.ui.chosenBackgroundLayout.count())):
            self.ui.chosenBackgroundLayout.itemAt(i).widget().setParent(None)

        if self.ui.imageChoice.isChecked():
            self.ui.chosenBackgroundLayout.addWidget(BackgroundImageConf())
            self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.backgroundImagePath.textChanged.connect(self.backgroundControlForStatusBar)

        if self.ui.customChoice.isChecked():
            self.countColors = Observable(0)
            self.countColors.observe(self.colorBackgroundControlForStatusBar)

            self.ui.chosenBackgroundLayout.addWidget(BackgroundCustomConf(self.countColors))
            self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.colorChoice.clicked.connect(self.updateStatusBar)
            self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.gradientChoice.clicked.connect(self.updateStatusBar)

    def makeCollageControl(self):

        if self.countPhotos.value > 1:
            if self.ui.imageChoice.isChecked():
                if os.path.exists(self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.backgroundImagePath.text()) and self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.backgroundImagePath.text().lower().endswith(('.png', '.jpg', '.jpeg')):
                    self.startProgressBarandCollageWindow()
                else:
                    self.ui.statusBar.setStyleSheet("color:red;")
                    self.ui.statusBar.showMessage("Please insert a background image path.")
            else:
                if self.ui.customChoice.isChecked():
                    if self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.colorChoice.isChecked():
                        if self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.chosenCustomBackgroundLayout.itemAt(0).widget().selectedColor is None:
                            self.ui.statusBar.setStyleSheet("color:red;")
                            self.ui.statusBar.showMessage("Please select a background color.")
                        else:
                            self.startProgressBarandCollageWindow()
                    else:
                        if self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.gradientChoice.isChecked():
                            if self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.chosenCustomBackgroundLayout.itemAt(0).widget().firstSelectedColor is None or self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.chosenCustomBackgroundLayout.itemAt(0).widget().secondSelectedColor is None:
                                self.ui.statusBar.setStyleSheet("color:red;")
                                self.ui.statusBar.showMessage("Please select background colors.")
                            else:
                                self.startProgressBarandCollageWindow()
                        else:
                            self.ui.statusBar.setStyleSheet("color:red;")
                            self.ui.statusBar.showMessage("Please choice between a background color and a background gradient.")
                else:
                    self.ui.statusBar.setStyleSheet("color:red;")
                    self.ui.statusBar.showMessage("Please choice between a background image and a custom background.")
        else:
            self.ui.statusBar.setStyleSheet("color:red;")
            self.ui.statusBar.showMessage("Please select at least two photos from a directory path. Number of selected Photos (min 2-max 15): {}".format(self.countPhotos.value))


    def callingOptimization(self):

        photosURLs = []
        weigths = []

        for i in range(self.ui.photoList.count()):
            if self.ui.photoList.itemAt(i).widget().ui.checkButton.isChecked():
                photosURLs.append(self.ui.photoList.itemAt(i).widget().filePath)
                weigths.append(self.ui.photoList.itemAt(i).widget().ui.valueWeigth.value())

        if self.ui.imageChoice.isChecked():
            Milp(self.ui.executionTimeValue.value(), self.countPhotos.value, photosURLs, weigths, self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.backgroundImagePath.text())
        else:
            if self.ui.customChoice.isChecked():
                colors = []

                if self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.colorChoice.isChecked():
                    colors.append(self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.chosenCustomBackgroundLayout.itemAt(0).widget().selectedColor)
                else:
                    if self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.gradientChoice.isChecked():
                        colors.append(self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.chosenCustomBackgroundLayout.itemAt(0).widget().firstSelectedColor)
                        colors.append(self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.chosenCustomBackgroundLayout.itemAt(0).widget().secondSelectedColor)
                Milp(self.ui.executionTimeValue.value(), self.countPhotos.value, photosURLs, weigths, None, colors, self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.customWidthChoice.value(), self.ui.chosenBackgroundLayout.itemAt(0).widget().ui.customHeightChoice.value())


    def startProgressBarandCollageWindow(self):
        process = Process(target=self.callingOptimization)
        process.start()
        self.setEnabled(False)
        window = ProgressBarDialog(process, self.ui.executionTimeValue.value())
        window.exec_()
        if process.is_alive():
            process.terminate()
        else:
            window = CollageCompleted()
            window.exec_()
        self.setEnabled(True)

