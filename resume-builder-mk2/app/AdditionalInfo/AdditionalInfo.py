from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from ..MainWindow.ModelDelegates import *
from ..MainWindow.TableModel import TableModel
from ..MainWindow.default_fields import *
import os,sys,json

class AdditionalInfo:
    def __init__(self,parent):
        self.parent=parent
        self.models=[]
        self.views=[]
        
        parent.newAdditionalInfo.clicked.connect(self.newAdditionalInfo)

    def newAdditionalinfo(self):
        self.newAdditionalInfo()

    def newAdditionalInfo(self):
        wid=QWidget(self.parent)
        emp=TableModel(item=additionalInfo())
        self.models.append(emp)
        self.views.append(wid)
        def remove():
            self.views.remove(wid)
            self.models.remove(emp)
            self.parent.additionalInfoGrid.removeWidget(wid)
            wid.deleteLater()
        def clear():
            emp.load_data(additionalInfo(),re=True)

        uic.loadUi("app/MainWindow/forms/entry.ui",wid)
        wid.view.setModel(emp)
        prep_table(wid.view)
        wid.clear.clicked.connect(clear)
        wid.remove.clicked.connect(remove)
        for num,i in enumerate(additionalInfo().keys()):
            if i in ['additional_info']:
                wid.view.setItemDelegateForRow(num,TextEditDelegate(wid))
            if i in ['type']:
                wid.view.setItemDelegateForRow(num,ComboBoxDelegate(wid,AdditionalInfoTypes()))

        self.parent.additionalInfoGrid.addWidget(wid,self.parent.additionalInfoGrid.count(),0,1,1)

