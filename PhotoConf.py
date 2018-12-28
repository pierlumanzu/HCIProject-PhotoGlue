from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap
import os
from PIL import Image
import sys
sys.path.append("UiDesigner/UiDesignerFilePython/")
from Ui_PhotoConf import Ui_PhotoConf

class PhotoConf(QWidget):

    def __init__(self, filePath, observableCountPhoto):

        super().__init__()

        self.ui = Ui_PhotoConf()
        self.ui.setupUi(self, observableCountPhoto)

        self.filePath = filePath

        photoPreview = QLabel(self.ui.photoPreview)
        widthFixed = 250

        photo = Image.open(filePath)
        width , height = photo.size
        photo = photo.resize((widthFixed, int((widthFixed/width) * height)), Image.ANTIALIAS)
        photo.save('smallerPhotoP.jpg')

        pixmap = QPixmap('smallerPhotoP.jpg')
        photoPreview.setPixmap(pixmap)

        self.ui.photoPreview.setFixedSize(widthFixed, int((widthFixed/width) * height))
        os.remove('smallerPhotoP.jpg')