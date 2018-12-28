from PyQt5.QtWidgets import QApplication
import sys
from PhotoApp import PhotoApp

app = QApplication(sys.argv)
window = PhotoApp()
window.show()
sys.exit(app.exec_())