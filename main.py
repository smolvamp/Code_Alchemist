from PyQt6.QtWidgets import *
import sys
from connections import appl

app= QApplication(sys.argv)

window= appl()
window.show()
app.exec()