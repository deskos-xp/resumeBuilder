from PyQt5.QtCore import QObject,QRunnable,QThread,QThreadPool,pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import QDialog,QWidget,QFileDialog
import os,sys,json
from copy import deepcopy
from .workers.FileReader import FileReader
from ..MainWindow.default_fields import *
#need worker to read importable file
class Importer:
    def __init__(self,parent):
        self.parent=parent
        parent.actionImport.triggered.connect(self.import_data)
        self.path=""
        self.data=dict()

    def getPath(self):
        p=QFileDialog.getOpenFileName(self.parent,"Open To Import",'',"JSON/json files(*.json);;All Files(*)",options=QFileDialog.DontUseNativeDialog)
        if p and p[0]:
            self.path=p[0]

    def store_data(self,data):
        def pre_clear():
            for k in self.parent.tabs.keys():
                if k in ['employment','education','certification','links','additionalInfo','references','skills']:
                    parent=self.parent.tabs.get(k)
                    parent.models.clear()
                    for v in parent.views:
                        getattr(self.parent,"{k}Grid".format(**dict(k=k))).removeWidget(v)
                        v.deleteLater()
                    parent.views.clear()
                else:
                    self.parent.tabs[k].model.load_data(contact(),re=True)
        def load():
            self.data=data
            for k in data.keys():
                if k in ['employment','education','certification','links','additionalInfo','references','skills']:
                    for num,i in enumerate(data.get(k)):
                        parent=self.parent.tabs.get(k)
                        nameUpper=k[0].upper()+k[1:].lower()
                        name="new{name}".format(**dict(name=nameUpper))
                        x=getattr(parent,name)
                        x()
                        parent.models[num].load_data(i,re=True)
                    pass
                else:
                    self.parent.tabs[k].model.load_data(data.get(k),re=True)
        pre_clear()
        load()
    def import_data(self):
        self.getPath()
        self.reader=FileReader(self.parent,self.path)
        self.reader.signals.hasError.connect(lambda x: print(x))
        self.reader.signals.finished.connect(lambda: print(self.data))
        self.reader.signals.hasData.connect(self.store_data)

        QThreadPool.globalInstance().start(self.reader)
        #print(self.path)

    def importer(self):
        data=dict()
        for i in self.parent.tabs.keys():
            if i in ['employment','education','certification','links','additionalInfo','references','skills']:
                data[i]=[]
                for model in self.parent.tabs[i].models:
                    data[i].append(deepcopy(model.item))
                    #print(model.item)
            else:
                data[i]=deepcopy(self.parent.tabs.get(i).model.item)
                #print(self.tabs.get(i).model.item) 
        print(data)
