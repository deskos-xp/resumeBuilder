from ..MainWindow.TableModel import TableModel
from ..MainWindow.default_fields import *
from ..MainWindow.ModelDelegates import ComboBoxDelegate,PhoneTextEditDelegate
from ..MainWindow.default_fields import prep_table,phoneTypes

class Contact:
    def __init__(self,parent):
        self.parent=parent

        print(states())
        self.model=TableModel(item=dict(contact()))
        self.parent.contactView.setModel(self.model)
        for num,i in enumerate(contact().keys()):
            if i.lower() == "state":
                self.parent.contactView.setItemDelegateForRow(num,ComboBoxDelegate(self.parent,states()))
            if i.lower() == "phone_type":
                self.parent.contactView.setItemDelegateForRow(num,ComboBoxDelegate(self.parent,phoneTypes()))
            if i.lower() == "phone_number":
                self.parent.contactView.setItemDelegateForRow(num,PhoneTextEditDelegate(self.parent))

        prep_table(self.parent.contactView)
        self.parent.clear_contact.clicked.connect(self.clearModel)

    def clearModel(self,state):
        self.model.load_data(contact(),re=True)
        
