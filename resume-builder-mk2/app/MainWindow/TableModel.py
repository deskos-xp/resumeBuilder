from PyQt5.QtCore import QAbstractTableModel,Qt,QModelIndex 
from PyQt5.QtGui import QColor

class TableModel(QAbstractTableModel):
    def __init__(self,*args,item=None,**kwargs):
        super(TableModel,self).__init__()
        self.item = item or {}
        self.row_count=0
        self.column_count=2

        self.align=[]
        self.init_align()
        self.fields=[]
        self.values=[]
        self.load_data(item)

    def init_align(self):
        for i in range(2):
            if i > 0:
                self.align.append(Qt.AlignCenter)
            else:
                self.align.append(Qt.AlignLeft)

    def load_data(self,data,re=False):
        if re == True:
            self.fields.clear()
            self.values.clear()
            
        if isinstance(data,dict):
            for k in data.keys():
                self.fields.append(k)
                self.values.append(data[k])
            #self.column_count=len(self.fields)
            self.row_count=len(self.values)
        print(self.values)
        self.tableToDict()
        self.layoutChanged.emit()
    
    def rowCount(self,parent=QModelIndex()):
        return self.row_count

    def columnCount(self,parent=QModelIndex()):
        return self.column_count

    def headerData(self,section,orientation,role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Fields","Values")[section]
        else:
            return "{}".format(section)

    def flags(self,index):
        baseflags=QAbstractTableModel.flags(self,index)
        if index.column() > 0:
            return baseflags | Qt.ItemIsEditable
        else:
            return baseflags 

    def data(self,index,role=Qt.DisplayRole):
        col=index.column()
        row=index.row()
        if role == Qt.DisplayRole:
            if col == 0:
                return self.fields[row]
            else:
                return self.values[row]
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return self.align[col]
        return None

    def setData(self,index,value,role):
        col=index.column()
        row=index.row()
        if col == 0:
            pass
        else:
            self.values[row]=value
        self.dataChanged.emit(index,index)
        self.tableToDict()
        return True

    def tableToDict(self):
        self.item=dict(zip(self.fields,self.values))

     
