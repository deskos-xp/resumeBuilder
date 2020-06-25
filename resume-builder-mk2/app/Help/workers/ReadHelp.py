from PyQt5.QtCore import QObject,QRunnable,QThread,QThreadPool,pyqtSignal,pyqtSlot

import os,sys,json

class ReadHelpSignals(QObject):
    killMe:bool=False
    finished:pyqtSignal=pyqtSignal()
    hasError:pyqtSignal=pyqtSignal(Exception)
    hasHelp:pyqtSignal=pyqtSignal(dict)

    @pyqtSlot()
    def kill(self):
        self.killMe=True

class ReadHelp(QRunnable):
    def __init__(self,helpFile:str):
        super(ReadHelp,self).__init__()
        self.helpFile=helpFile
        self.signals=ReadHelpSignals()

    def run(self):
        try:
            with open(os.path.abspath(self.helpFile),"r") as fd:
                d=json.load(fd)
                self.signals.hasHelp.emit(d)
        except Exception as e:
            self.signals.hasError.emit(e)
        self.signals.finished.emit()
