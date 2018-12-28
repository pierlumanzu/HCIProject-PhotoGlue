from PyQt5.QtWidgets import QWidget, QColorDialog
import sys
sys.path.append("UiDesigner/UiDesignerFilePython/")
from Ui_ChosenBackgroundColor import Ui_ChosenBackgroundColor
from Ui_ChosenBackgroundGradient import Ui_ChosenBackgroundGradient

class ChosenBackgroundColor(QWidget):

    def __init__(self, observableCountColors):

        super().__init__()

        self.ui = Ui_ChosenBackgroundColor()
        self.ui.setupUi(self)

        self.observableCountColors = observableCountColors

        self.ui.colorPreview.setFixedSize(150,50)
        self.ui.dialogButton.setFixedSize(150,50)

        self.selectedColor = None

        self.ui.dialogButton.clicked.connect(self.chooseColor)

    def chooseColor(self):
        self.selectedColor = QColorDialog.getColor()

        if self.selectedColor.isValid():
            self.ui.colorPreview.setStyleSheet('background-color:%s;'% self.selectedColor.name())
            self.selectedColor = self.selectedColor.getRgb()[0:3]
            if self.observableCountColors.value < 1:
                self.observableCountColors.value = self.observableCountColors.value + 1


class ChosenBackgroundGradient(QWidget):

    def __init__(self, observableCountColors):

        super().__init__()

        self.ui = Ui_ChosenBackgroundGradient()
        self.ui.setupUi(self)

        self.observableCountColors = observableCountColors

        self.ui.firstColorPreview.setFixedSize(150,50)
        self.ui.firstDialogButton.setFixedSize(150,50)
        self.ui.secondColorPreview.setFixedSize(150,50)
        self.ui.secondDialogButton.setFixedSize(150,50)

        self.firstSelectedColor = None
        self.secondSelectedColor = None

        self.ui.firstDialogButton.clicked.connect(self.chooseFirstColor)
        self.ui.secondDialogButton.clicked.connect(self.chooseSecondColor)

    def chooseFirstColor(self):
        self.firstSelectedColor = QColorDialog.getColor()

        if self.firstSelectedColor.isValid():
            self.ui.firstColorPreview.setStyleSheet('background-color:%s;' % self.firstSelectedColor.name())
            self.firstSelectedColor = self.firstSelectedColor.getRgb()[0:3]
            if self.observableCountColors.value != 1 or self.secondSelectedColor is not None:
                self.observableCountColors.value = self.observableCountColors.value + 1


    def chooseSecondColor(self):
        self.secondSelectedColor = QColorDialog.getColor()

        if self.secondSelectedColor.isValid():
            self.ui.secondColorPreview.setStyleSheet('background-color:%s;' % self.secondSelectedColor.name())
            self.secondSelectedColor = self.secondSelectedColor.getRgb()[0:3]
            if self.observableCountColors.value != 1 or self.firstSelectedColor is not None:
                self.observableCountColors.value = self.observableCountColors.value + 1

