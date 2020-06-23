from PyQt5.QtCore import QRunnable,QObject,QThread,QThreadPool,pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import QDialog,QWidget

import os,sys,json

class FileReaderSignals(QObject):
    killMe:bool=False
    finished:pyqtSignal=pyqtSignal()
    hasError:pyqtSignal=pyqtSignal(Exception)
    hasData:pyqtSignal=pyqtSignal(dict)    
    data:dict=dict()

    @pyqtSlot()
    def kill(self):
        self.killMe=True

class FileReader(QRunnable):
    def __init__(self,parent,path):
        super(FileReader,self).__init__()
        self.signals=FileReaderSignals()
        self.path=path

    def run(self):
        try:
            data=dict()
            with open(self.path,"r") as fd:
                data=json.load(fd)
            self.signals.hasData.emit(data)
        except Exception as e:
            self.signals.hasError.emit(e)
        self.signals.finished.emit()
