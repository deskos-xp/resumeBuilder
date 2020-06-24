from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

import os,sys,json
from ..MainWindow.TableModel import TableModel
from ..MainWindow.ModelDelegates import *
from ..MainWindow.default_fields import *

class Certification:
    def __init__(self,parent):
        self.parent=parent
        self.models=[]
        self.views=[]
        
        parent.newCertification.clicked.connect(self.newCertification)

    def newCertification(self):
        wid=QWidget(self.parent)
        
        emp=TableModel(item=certification())

        self.models.append(emp)
        self.views.append(wid)
        def clear():
            emp.load_data(certification(),re=True)

        def remove():
            self.models.remove(emp)
            self.views.remove(wid)
            self.parent.certificationGrid.removeWidget(wid)
            wid.deleteLater()

        uic.loadUi("app/MainWindow/forms/entry.ui",wid)
        wid.view.setModel(emp)
        wid.groupBox.setTitle(__name__.split(".")[-1])
        prep_table(wid.view)
        wid.clear.clicked.connect(clear)
        wid.remove.clicked.connect(remove)

        for num,i in enumerate(certification().keys()):
            if i.lower() in ['date_acquired','date_expires']:
                wid.view.setItemDelegateForRow(num,DateEditDelegate(wid))

        self.parent.certificationGrid.addWidget(wid,self.parent.certificationGrid.count(),0,1,1)
