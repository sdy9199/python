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


    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0] :
            with open(fname[0], encoding = 'UTF8') as f:
                data = f.read()
        self.plainTextEdit.setPlainText(data)
        
        print("open {}!!".format(fname[0]))        
          
    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self)
        if fname[0] :
            data = self.plainTextEdit.toPlainText()
            with open(fname[0],'w', encoding = 'UTF8') as f:
              f.write(data)
        
        print("save{}!!",format(fname[0]))
        
app = QApplication(sys.argv)
MainWindow = Windowclass()
MainWindow.show()
app.exec_()
