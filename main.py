from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import QKeyEvent,QCloseEvent
from ui_24 import Ui_MainWindow
import sys,random,json,os
path=os.path.dirname(os.path.abspath(__file__))
class main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.currentNum=[]
        with open(path+os.sep+'avaliableNums.json','r')as f:
            self.avaliablenums=json.load(f)
        with open(path+os.sep+'highest.json','r')as f:
            self.highest=json.load(f)
        self.label_2.setText(f'最高分：{self.highest}')
        self.score=0
        self.update()
        self.show()
    def update(self):
        numList=random.choice(self.avaliablenums)
        pbtns=[self.pushButton,self.pushButton_2,self.pushButton_3,self.pushButton_4]
        for i in range(len(pbtns)):
            n=str(numList[i])
            pbtns[i].setText(n)
            self.currentNum.append(n)
        del pbtns
    def keyPressEvent(self, event: QKeyEvent):
        if event.key()==Qt.Key_Return:
            self.judge()
    def judge(self):
        if self.isCheat():
            QMessageBox.critical(self,'作弊！','系统检测到你存在作弊行为，已取消游戏资格')
            sys.exit(app.exec_())
        if eval(self.lineEdit.text())==24:
            QMessageBox.information(self,'result','true')
            self.score+=1
            self.label.setText(f'得分：{self.score}')
            self.update()
        else:
            QMessageBox.information(self,'result','false')
        self.lineEdit.clear()
    def isCheat(self):
        nums=['1','2','3','4','5','6','7','8','9']
        for i in list(self.lineEdit.text()):
            if i in nums and i not in self.currentNum:
                return True
            else:
                pass
        return False
    def closeEvent(self, event: QCloseEvent):
        if self.score>self.highest:
            with open(path+os.sep+'highest.json','w')as f:
                json.dump(self.score,f)
        return super().closeEvent(event)
if __name__=='__main__':
    app=QApplication(sys.argv)
    m=main()
    sys.exit(app.exec_())