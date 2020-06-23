from PyQt5.QtCore import QObject,QRunnable,QThread,QThreadPool,pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import QDialog,QWidget,QFileDialog
import os,sys,json
from copy import deepcopy

#need worker to read importable file
class Importer:
    def __init__(self,parent):
        self.parent=parent
        parent.actionImport.triggered.connect(self.import_data)

    def import_data(self):
        data=dict()
        for i in self.parent.tabs.keys():
            if i in ['employment','education','certification','links','additionalInfo','references']:
                data[i]=[]
                for model in self.parent.tabs[i].models:
                    data[i].append(deepcopy(model.item))
                    #print(model.item)
            else:
                data[i]=deepcopy(self.parent.tabs.get(i).model.item)
                #print(self.tabs.get(i).model.item) 
        print(data)
