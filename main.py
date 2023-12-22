import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.showMaximized()


app = QApplication(sys.argv)
QApplication.setApplicationName('Blitz Browser')
window = MainWindow()
app.exec_()
print('Blitz has started sucessfully')