from ..MainWindow.TableModel import TableModel
from ..MainWindow.default_fields import you,states
from ..MainWindow.ModelDelegates import ComboBoxDelegate
from ..MainWindow.default_fields import prep_table,phoneTypes

class You:
    def __init__(self,parent):
        self.parent=parent

        print(states())
        self.model=TableModel(item=dict(you()))
        self.parent.youView.setModel(self.model)
        for num,i in enumerate(you().keys()):
            if i.lower() == "state":
                self.parent.youView.setItemDelegateForRow(num,ComboBoxDelegate(self.parent,states()))
            if i.lower() == "phone_type":
                self.parent.youView.setItemDelegateForRow(num,ComboBoxDelegate(self.parent,phoneTypes()))
        prep_table(self.parent.youView)
        self.parent.clear_you.clicked.connect(self.clearModel)

    def clearModel(self,state):
        self.model.load_data(you(),re=True)
        
