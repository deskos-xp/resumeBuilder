from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

import os,sys,json

from ..MainWindow.ModelDelegates import *
from ..MainWindow.TableModel import TableModel
from ..MainWindow.default_fields import *

class Links:
    def __init__(self,parent):
        self.parent=parent
        self.models=[]
        self.views=[]
        parent.newLink.clicked.connect(self.newLink)

    def newLink(self,state):
        wid=QWidget(self.parent)
        emp=TableModel(item=links())
        self.models.append(emp)
        self.views.append(wid)
        def clear():
            emp.load_data(links(),re=True)
        def remove():
            self.views.remove(wid)
            self.models.remove(emp)
            self.parent.linksGrid.removeWidget(wid)
            wid.deleteLater()

        uic.loadUi("app/MainWindow/forms/entry.ui",wid)
        wid.view.setModel(emp)
        prep_table(wid.view)
        wid.remove.clicked.connect(remove)
        wid.clear.clicked.connect(clear)
        for num,i in enumerate(links().keys()):
            if i in ['link']:
                wid.view.setItemDelegateForRow(num,TextEditDelegate(wid))
        self.parent.linksGrid.addWidget(wid,self.parent.linksGrid.count(),0,1,1)
