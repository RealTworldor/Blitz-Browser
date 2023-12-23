# Base imports
import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# WEB ENGINE
from PyQt5.QtWebEngineWidgets import *

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # ADD WINDOW ELEMENTS
        # ADD WINDOW TAB WIDGETS TO DISPLAY WEB TABS
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)

        self.setCentralWidget(self.tabs)

        # ADD NAVIGATION TOOLBAR
        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(30, 30))
        self.addToolBar(navtb)

        # ADD BUTTONS TO NAVIGATION TOOLBAR
        back_btn = QAction(QIcon(os.path.join('icons', 'back_btn.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        navtb.addAction(back_btn)





        # SHOW MAIN WINDOW
        self.show()


app = QApplication(sys.argv)
#APPLICATION NAME
app.setApplicationName("Blitz Web")
#APPLICATION COMPANY NAME
app.setOrganizationName("Blitz and Blaze Web")
#APPLICATION COMPANY DOMAIN
app.setOrganizationDomain("blitz-and-blaze-web")

window = MainWindow()

app.exec_()