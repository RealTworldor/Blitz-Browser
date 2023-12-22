#This is the blitz browser :)
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://search.brave.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Foward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        github_page_btn = QAction('Github page', self)
        github_page_btn.triggered.connect(self.navigate_github_page)
        navbar.addAction(github_page_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://search.brave.com'))

    def navigate_github_page(self):
        self.browser.setUrl(QUrl('http://github.com/RealTworldor/Blitz-Browser'))




app = QApplication(sys.argv)
QApplication.setApplicationName('Blitz Browser')
window = MainWindow()
app.exec_()
print('Blitz has started successfully')