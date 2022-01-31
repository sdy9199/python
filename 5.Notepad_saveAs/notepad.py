import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 


form_class = uic.loadUiType("c:\\Python\\pyQt5\\5.Notepad_saveAs\\notepad.ui")[0]

class Windowclass(QMainWindow,form_class): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.file_load.triggered.connect(self.openFunction)
        self.file_save.triggered.connect(self.saveFunction)
        self.file_saveas.triggered.connect(self.saveAsFunction)
        

        self.opened = False
        self.opened_file_path = ""
        
        
    def save_file(self, fname):
        data = self.plainTextEdit.toPlainText()
        
        with open(fname,'w', encoding ="UTF8") as f:
            f.write(data)
            
        self.opened = True
        self.opened_file_path = fname
            
        print("save{}!!", format(fname))
        
        
    def open_file(self, fname):
        with open(fname, encoding= "UTF8") as f:
            data = f.read()        
        self.plainTextEdit.setPlainText(data)
        
        self.opened = True
        self.opened_file_path = fname
        
        print("open{}!!", format(fname))        
        
    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]:
            self.save_file(fname[0])
            
    def saveFunction(self):
        if self.opened:
            self.save_file(self.opened_file_path)
        else:
            self.saveAsFunction()
            
    def saveAsFunction(self):
        fname = QFileDialog.getSaveFileName(self)
        if fname[0]:
            self.save_file(fname[0])
            
            
app = QApplication(sys.argv)
MainWindow = Windowclass()
MainWindow.show()

app.exec_()
