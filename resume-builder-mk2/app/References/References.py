from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from ..MainWindow.ModelDelegates import *
from ..MainWindow.TableModel import TableModel
from ..MainWindow.default_fields import *
import os,sys,json

class References:
    def __init__(self,parent):
        self.parent=parent
        self.models=[]
        self.views=[]

        parent.newReferences.clicked.connect(self.newReferences)

    def newReferences(self):
        wid=QWidget(self.parent)
        emp=TableModel(item=reference())
        self.models.append(emp)
        self.views.append(wid)

        def clear():
            emp.load_data(reference(),re=True)
        def remove():
            self.models.remove(emp)
            self.views.remove(wid)
            self.parent.referencesGrid.removeWidget(wid)
            wid.deleteLater()

        uic.loadUi("app/MainWindow/forms/entry.ui",wid)
        wid.view.setModel(emp)
        prep_table(wid.view)
        wid.remove.clicked.connect(remove)
        wid.clear.clicked.connect(clear)
    
        for num,i in enumerate(reference().keys()):
            if i.lower() in ['state']:
                wid.view.setItemDelegateForRow(num,ComboBoxDelegate(wid,states()))
            if i.lower() in ['phone_type']:
                wid.view.setItemDelegateForRow(num,ComboBoxDelegate(wid,phoneTypes()))
            if i.lower() in ['email']:
                wid.view.setItemDelegateForRow(num,TextEditDelegate(wid))
            if i.lower() in ['phone_number']:
                wid.view.setItemDelegateForRow(num,PhoneTextEditDelegate(wid))

        self.parent.referencesGrid.addWidget(wid,self.parent.referencesGrid.count(),0,1,1)

