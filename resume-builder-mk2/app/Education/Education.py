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

    def newEducation(self,state):
        wid=QWidget(self.parent)
                
        emp=TableModel(item=education())
        self.models.append(emp)
        self.views.append(wid)

        uic.loadUi("app/Education/forms/education.ui",wid)
        wid.educationView.setModel(emp)
        prep_table(wid.educationView)
        def clear():
            emp.load_data(education(),re=True)
            
        def remove():
            self.models.remove(emp)
            self.views.remove(wid)
            self.parent.educationGrid.removeWidget(wid)
            wid.deleteLater()

        wid.remove_education.clicked.connect(remove)
        wid.clear_education.clicked.connect(clear)
        
        for num,i in enumerate(education().keys()):
            if i.lower() in ['start_date','end_date']:
                wid.educationView.setItemDelegateForRow(num,DateEditDelegate(wid))
            if i.lower() in ['present']:
                wid.educationView.setItemDelegateForRow(num,CheckBoxDelegate(wid))
            if i.lower() in ['state']:
                wid.educationView.setItemDelegateForRow(num,ComboBoxDelegate(wid,states()))
            if i.lower() in ['school_type']:
                wid.educationView.setItemDelegateForRow(num,ComboBoxDelegate(wid,schoolTypes()))

        self.parent.educationGrid.addWidget(wid,self.parent.educationGrid.count(),0,1,1)
