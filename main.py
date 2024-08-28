from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction
import sys


class application(QMainWindow):
    
    def __init__(self):
        super().__init__()
        #to open in maximized state
        self.showMaximized()
        
        #to initiate widget(app)
        self.home= QWidget()
        
        #to centralize widget(in other words it allow use to start making widgets from very centre unless specified).
        self.setCentralWidget(self.home)
        
        #saaj sringaar for our widget
        self.home.setStyleSheet("QWidget""{"
                                "color: white"
                           "background-color:#131422;"
                           "}")

        #everyone like sidepanels....
        self.sidebar= QVBoxLayout()
        self.home.setLayout(self.sidebar)
        
        self.dock= QDockWidget("Tools",self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)
        side_panel_widget = QWidget()
        side_panel_layout = QVBoxLayout()
        side_panel_widget.setLayout(side_panel_layout)
        side_panel_widget.setStyleSheet(
            "QWidget""{"
            "min-width: 200px;"
            "background-color: #12141D;"
            "}"
        )
        self.dock.setStyleSheet(
            "QDockWidget"
            "{"
            "color:white;"
            "padding: 100px;"
            "}"
        )

        #side panel widget inside the dock(nhi toh color nhi aaenga)
        self.dock.setWidget(side_panel_widget)
        
        
        #toggle button coz who likes always on side panels?
        self.toggle_button= QPushButton('',self)
        self.toggle_button.setIcon(QIcon("pg6/src/side-menu.png"))
        self.toggle_button.setGeometry(150,500,20,30)
        self.toggle_button.clicked.connect(self.toggle)
        self.sidebar.addWidget(self.toggle_button)
        self.toggle_button.setFixedHeight(50)
        self.toggle_button.setFixedWidth(30)
        
    def toggle(self):
        if self.dock.isVisible():
            self.dock.hide()
        else:
            self.dock.show()
            
if __name__=='__main__':   
    app= QApplication(sys.argv)   
    wi=application()
    wi.show()
    sys.exit(app.exec())
