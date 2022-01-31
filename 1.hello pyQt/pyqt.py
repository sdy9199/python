import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 


form_class = uic.loadUiType("c:\\Python\\pyQt5\\1.hello pyQt\\pyqt.ui")[0]
class Windowclass(QMainWindow, form_class): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
app = QApplication(sys.argv)
MainWindow = Windowclass()
MainWindow.show()
app.exec_()
