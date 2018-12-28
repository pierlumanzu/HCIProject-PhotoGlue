from PyQt5.QtWidgets import QCheckBox

class checkboxSpecial(QCheckBox):

    def __init__(self, observableCountPhoto, *__args):

        super().__init__(*__args)

        self.observableCountPhoto = observableCountPhoto
        self.changeCheckboxProperties()
        self.observableCountPhoto.observe(self.changeCheckboxProperties)

        self.stateChanged.connect(self.modifyCount)

    def changeCheckboxProperties(self):
        if self.observableCountPhoto.value == 15 and not(self.isChecked()):
            self.setCheckable(False)
        if self.observableCountPhoto.value < 15 and not(self.isCheckable()):
            self.setCheckable(True)

    def modifyCount(self):
        if self.isChecked():
            self.observableCountPhoto.value = self.observableCountPhoto.value + 1
        else:
            self.observableCountPhoto.value = self.observableCountPhoto.value - 1