import os
from PIL import Image
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap
from ChosenBackground import ChosenBackgroundColor, ChosenBackgroundGradient
import sys
sys.path.append("UiDesigner/UiDesignerFilePython/")
from Ui_BackgroundImageConf import Ui_BackgroundImageConf
from Ui_BackgroundCustomConf import Ui_BackgroundCustomConf

class BackgroundImageConf(QWidget):

    def __init__(self):

        super().__init__()

        self.ui = Ui_BackgroundImageConf()
        self.ui.setupUi(self)

        self.ui.backgroundImagePath.textChanged.connect(self.setBackgroundImagePreview)

    def setBackgroundImagePreview(self):

        for i in reversed(range(self.ui.backgroundImagePreviewLayout.count())):
            self.ui.backgroundImagePreviewLayout.itemAt(i).widget().setParent(None)

        if os.path.exists(self.ui.backgroundImagePath.text()) and self.ui.backgroundImagePath.text().lower().endswith(
                ('.png', '.jpg', '.jpeg')):

            backgroundImagePreview = QLabel()
            widthFixed = 300

            photo = Image.open(self.ui.backgroundImagePath.text())
            width, height = photo.size
            photo = photo.resize((widthFixed, int((widthFixed / width) * height)), Image.ANTIALIAS)
            photo.save('smallerPhotoB.jpg')

            pixmap = QPixmap('smallerPhotoB.jpg')
            backgroundImagePreview.setPixmap(pixmap)

            self.ui.backgroundImagePreviewLayout.addWidget(backgroundImagePreview)
            self.ui.backgroundImagePreview.setFixedSize(widthFixed, int((widthFixed / width) * height))
            os.remove('smallerPhotoB.jpg')

            self.ui.labelImageWidth.setText('Width :  {}'.format(width))
            self.ui.labelImageHeight.setText('Height :  {}'.format(height))
        else:
            self.ui.backgroundImagePreviewLayout.addWidget(QLabel("Insert a path of an image."))


class BackgroundCustomConf(QWidget):

    def __init__(self, observableCountColors):

        super().__init__()

        self.ui = Ui_BackgroundCustomConf()
        self.ui.setupUi(self)

        self.observableCountColors = observableCountColors

        self.ui.colorChoice.clicked.connect(self.setCustomBackgroundChoice)
        self.ui.gradientChoice.clicked.connect(self.setCustomBackgroundChoice)

    def setCustomBackgroundChoice(self):

        for i in reversed(range(self.ui.chosenCustomBackgroundLayout.count())):
            self.ui.chosenCustomBackgroundLayout.itemAt(i).widget().setParent(None)

        if self.ui.colorChoice.isChecked():
            self.observableCountColors.value = 0
            self.ui.chosenCustomBackgroundLayout.addWidget(ChosenBackgroundColor(self.observableCountColors))
        if self.ui.gradientChoice.isChecked():
            self.observableCountColors.value = 0
            self.ui.chosenCustomBackgroundLayout.addWidget(ChosenBackgroundGradient(self.observableCountColors))