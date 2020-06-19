from ..MainWindow.TableModel import TableModel
from ..MainWindow.ModelDelegates import ComboBoxDelegate,CheckBoxDelegate,DateEditDelegate,TextEditDelegate
from ..MainWindow.default_fields import states,employment,prep_table
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class Employment:
    def __init__(self,parent):
        self.models=[]
        self.views=[]

        self.parent=parent
        parent.newEmployment.clicked.connect(self.newEmployment)

    def newEmployment(self):
        wid=QWidget(self.parent)       
        emp=TableModel(item=employment())
        def clear():
            emp.load_data(employment(),re=True)
        self.models.append(emp)
        def remove():
            self.views.remove(wid)
            self.models.remove(emp)
            self.parent.employmentGrid.removeWidget(wid)
            wid.deleteLater()
         
        uic.loadUi("app/MainWindow/forms/entry.ui",wid)
        self.views.append(wid)
        wid.view.setModel(emp)
        wid.groupBox.setTitle(__name__.split(".")[-1])
        wid.clear.clicked.connect(clear)
        wid.remove.clicked.connect(remove)
        prep_table(wid.view)
        for num,i in enumerate(employment().keys()):
            if i.lower() == "state":
                wid.view.setItemDelegateForRow(num,ComboBoxDelegate(wid,states()))
            if i.lower() == "present":
                wid.view.setItemDelegateForRow(num,CheckBoxDelegate(wid,state=False))
            if i.lower() in ['start_date','end_date']:
                wid.view.setItemDelegateForRow(num,DateEditDelegate(wid))
            if i.lower() in ['duties']:
                wid.view.setItemDelegateForRow(num,TextEditDelegate(wid))

        self.parent.employmentGrid.addWidget(wid,self.parent.employmentGrid.count(),0,1,1)
