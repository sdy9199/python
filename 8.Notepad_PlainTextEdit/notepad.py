import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 


form_class = uic.loadUiType("c:\\Python\\pyQt5\\8.Notepad_PlanTexiEdit\\notepad.ui")[0]

class Windowclass(QMainWindow,form_class): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.file_load.triggered.connect(self.openFunction)
        self.file_save.triggered.connect(self.saveFunction)
        self.file_saveas.triggered.connect(self.saveAsFunction)
        self.file_close.triggered.connect(self.closeEvent)
        
        self.opened = False
        self.opened_file_path = "제목 없음"
        
    def save_changed_data(self):
        msgBox = QMessageBox()
        msgBox.setText("변경 내용을 {}에 저장하시겠습니까?".format(self.opened_file_path))
        msgBox.addButton('저장', QMessageBox. YesRole) #0
        msgBox.addButton('저장 안 함', QMessageBox. NoRole) #1
        msgBox.addButton('취소', QMessageBox. RejectRole) #2
        ret = msgBox.exec_()
        print(ret)  #저장여부 번호로 출력
        # msgBox.addButton()
        if ret == 2:
            return ret

    def closeEvent(self, event):
        ret = self.save_changed_data()
        if ret == 2:
            event.ignore() #취소시 창단기 금지
        print("close test") #클로저 이벤트 발스
        
        
    def save_file(self, fname):
        data = self.plainTextEdit.toPlainText()
        
        with open(fname,'w', encoding="UTF8") as f:
            f.write(data)
            
        self.opened = True
        self.opened_file_path = fname
            
        print("save {}!!", format(fname))
        
        
    def open_file(self, fname):
        with open(fname, encoding="UTF8") as f:
            data = f.read()        
        self.plainTextEdit.setPlainText(data)
        
        self.opened = True
        self.opened_file_path = fname
        
        print("open {}!!", format(fname))        
        
    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]:
            self.open_file(fname[0])
            
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
