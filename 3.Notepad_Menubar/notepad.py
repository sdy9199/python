import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 


form_class = uic.loadUiType("c:\\Python\\pyQt5\\3.Notepad_Menubar\\notepad.ui")[0]
class Windowclass(QMainWindow,form_class): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.action_load.triggered.connect(self.openfunction)
        self.action_save.triggered.connect(self.savefunction)


    def openfunction(self):
        print("open!!")
    
    def savefunction(self):
        print("save!!")
        
app = QApplication(sys.argv)
MainWindow = Windowclass()
MainWindow.show()
app.exec_()
