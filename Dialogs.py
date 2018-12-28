from PyQt5.QtWidgets import QDialog
import time
import webbrowser
import threading
import sys
sys.path.append("UiDesigner/UiDesignerFilePython/")
from Ui_ProgressBarDialog import Ui_ProgressBarDialog
from Ui_CollageCompleted import Ui_CollageCompleted

TIME_LIMIT = 100

class ProgressBarDialog(QDialog):

    def __init__(self, processOptimization, executionTime):
        super().__init__()

        self.ui = Ui_ProgressBarDialog()
        self.ui.setupUi(self)

        self.show()
        t = threading.Thread(target=self.progressFunction, args=[processOptimization, executionTime])
        t.start()

    def progressFunction(self, processOptimization, executionTime):
        count = 0
        while count < TIME_LIMIT:
            if processOptimization.is_alive():
                count += 1
                if count == 100:
                    while processOptimization.is_alive():
                        pass
            else:
                count = 100
            time.sleep(executionTime / 100)
            self.onCountChanged(count)
            if count == 100:
                break

    def onCountChanged(self, value):
        self.ui.progressBar.setValue(value)

        if value == 100:
            time.sleep(1)
            self.close()

class CollageCompleted(QDialog):

    def __init__(self):

        super().__init__()

        self.ui=Ui_CollageCompleted()
        self.ui.setupUi(self)

        self.ui.okButton.clicked.connect(self.closeDialog)
        self.ui.folderButton.clicked.connect(self.goToTheFolder)

    def closeDialog(self):
        self.close()

    def goToTheFolder(self):
        webbrowser.open("OutputPhotos")
