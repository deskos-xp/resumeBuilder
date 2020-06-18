from PyQt5 import uic
from PyQt5.QtCore import QRunnable,QObject,QThread,QThreadPool
from PyQt5.QtWidgets import QApplication,QMainWindow
from .MainWindow.TableModel import TableModel
from .You.You import You
from .Employment.Employment import Employment
from .Education.Education import Education
from .MenuBar.MenuBar import MenuBar
class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        uic.loadUi("app/MainWindow/forms/app.ui",self)
        self.tabs={}
        self.tabs['you']=You(self)
        self.tabs['employment']=Employment(self)
        self.tabs['education']=Education(self)
        self.submit.clicked.connect(self.saveData)
        
        self.mb=MenuBar(self)

    def saveData(self):
        for i in self.tabs.keys():
            if i in ['employment','education']:
                for model in self.tabs[i].models:
                    print(model.item)
            else:
                print(self.tabs.get(i).model.item)

def main(*args):
    app=QApplication(list(args))
    win=Main()
    win.show()
    app.exec_()
