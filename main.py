from PyQt5.QtWidgets import QApplication
import sys
from PhotoGlue import PhotoGlue

app = QApplication(sys.argv)
window = PhotoGlue()
window.show()
sys.exit(app.exec_())