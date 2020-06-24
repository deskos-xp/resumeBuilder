from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

import os,sys,json
from ..MainWindow.default_fields import *
from ..MainWindow.ModelDelegates import *
from ..MainWindow.TableModel import TableModel

class Skills:
    def __init__(self,parent):
        self.parent=parent
        self.models=[]
        self.views=[]

        self.parent.newSkill.clicked.connect(self.newSkill)


    def newSkills(self):
        self.newSkill()

    def newSkill(self):
        wid=QWidget(self.parent)
        mod=TableModel(item=skills())
        self.models.append(mod)
        self.views.append(wid)

        def remove():
            self.parent.skillsGrid.removeWidget(wid)
            self.views.remove(wid)
            wid.deleteLater()
            self.models.remove(mod)

        def clear():
            mod.load_data(skills(),re=True)


        uic.loadUi("app/MainWindow/forms/entry.ui",wid)
        wid.view.setModel(mod)
        prep_table(wid.view)
        
        wid.clear.clicked.connect(clear)
        wid.remove.clicked.connect(remove)
        for num,key in enumerate(skills().keys()):
            if key == 'comment':
                wid.view.setItemDelegateForRow(num,TextEditDelegate(wid))
            if key in ['months_experience','years_experience']:
                wid.view.setItemDelegateForRow(num,SpinBoxDelegate(wid))

        self.parent.skillsGrid.addWidget(wid,self.parent.skillsGrid.count(),0,1,1)

