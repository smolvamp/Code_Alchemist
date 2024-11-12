import sys
from ui_4 import *
from PyQt6.QtWidgets import *

class appl(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.windowTitle("PG6")
        
        self.icon_name_widget.setHidden(True)
        
        self.normal_icon.clicked.connect(self.switch_to_normal)
        self.normal_expanded.clicked.connect(self.switch_to_normal)
        
        self.advanced_icon.clicked.connect(self.switch_to_advanced)
        self.advanced_expanded.clicked.connect(self.switch_to_advanced)
        
        self.about_icon.clicked.connect(self.switch_to_about)
        self.about_expanded.clicked.connect(self.switch_to_about)
        
        
    def switch_to_normal(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_advanced(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_about(self):
        self.stackedWidget.setCurrentIndex(2)