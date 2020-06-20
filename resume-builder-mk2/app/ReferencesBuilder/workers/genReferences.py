from PyQt5.QtCore import QObject,QRunnable,QThread,QThreadPool,pyqtSignal,pyqtSlot
from .generator import generator

class genReferencesSignals(QObject):
    killMe:bool=False
    finished:pyqtSignal=pyqtSignal()
    hasError:pyqtSignal=pyqtSignal(Exception)

    @pyqtSlot()
    def kill(self):
        self.killMe=True

class genReferences(QRunnable):
    def __init__(self,parent,contact,references,path):
        super(genReferences,self).__init__()
        self.parent=parent
        self.contact=contact
        self.references=references
        self.signals=genReferencesSignals()
        self.path=path

    def run(self):
        try:
            generator(self.contact,self.references,self.path)
            #print(self.contact)
            #print(self.references)
        except Exception as e:
            self.signals.hasError.emit(e)
        self.signals.finished.emit()
 
