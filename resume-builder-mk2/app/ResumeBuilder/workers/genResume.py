from PyQt5.QtCore import QObject,QRunnable,QThread,QThreadPool,pyqtSignal,pyqtSlot

from .generator import generator

class genResumeSignals(QObject):
    killMe:bool=False
    finished:pyqtSignal=pyqtSignal()
    hasError:pyqtSignal=pyqtSignal(Exception)
    
    @pyqtSlot()
    def kill(self):
        self.killMe=True

class genResume(QRunnable):
    def __init__(self,parent,data:dict,contact:dict,path:str):
        super(genResume,self).__init__()
        self.signals=genResumeSignals()
        self.path=path
        self.data=data
        self.contact=contact

    def run(self):
        generator(self.data,self.contact,self.path)
        try:
            pass
            #self.gen.signals.finished.connect(lambda x:print(x))
            #self.gen.signals.hasError.connect(lambda x:print(x))
            #QThreadPool.globalInstance().start(self.gen)
        except Exception as e:
            self.signals.hasError.emit(e)
        self.signals.finished.emit()
