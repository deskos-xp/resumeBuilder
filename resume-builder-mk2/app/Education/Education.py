from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from ..MainWindow.TableModel import TableModel
from ..MainWindow.ModelDelegates import *
from ..MainWindow.default_fields import *

class Education:
    def __init__(self,parent):
        self.parent=parent
        self.models=[]
        self.views=[]

        parent.newEducation.clicked.connect(self.newEducation)

    def newEducation(self):
        wid=QWidget(self.parent)
                
        emp=TableModel(item=education())
        self.models.append(emp)
        self.views.append(wid)

        uic.loadUi("app/MainWindow/forms/entry.ui",wid)
        wid.view.setModel(emp)
        wid.groupBox.setTitle(__name__.split(".")[-1])
        prep_table(wid.view)
        def clear():
            emp.load_data(education(),re=True)
            
        def remove():
            self.models.remove(emp)
            self.views.remove(wid)
            self.parent.educationGrid.removeWidget(wid)
            wid.deleteLater()

        wid.remove.clicked.connect(remove)
        wid.clear.clicked.connect(clear)
        
        for num,i in enumerate(education().keys()):
            if i.lower() in ['start_date','end_date']:
                wid.view.setItemDelegateForRow(num,DateEditDelegate(wid))
            if i.lower() in ['present']:
                wid.view.setItemDelegateForRow(num,CheckBoxDelegate(wid))
            if i.lower() in ['state']:
                wid.view.setItemDelegateForRow(num,ComboBoxDelegate(wid,states()))
            if i.lower() in ['school_type']:
                wid.view.setItemDelegateForRow(num,ComboBoxDelegate(wid,schoolTypes()))

        self.parent.educationGrid.addWidget(wid,self.parent.educationGrid.count(),0,1,1)
