from PyQt5.QtCore import Qt,pyqtSlot,QDate
from PyQt5.QtWidgets import QHeaderView,QItemDelegate,QComboBox,QCheckBox,QDateEdit,QTextEdit
import time

class TextEditDelegate(QItemDelegate):
    def __init__(self,parent):
        QItemDelegate.__init__(self,parent)

    def createEditor(self,parent,option,index):
        date=QTextEdit(parent) 
        return date

    def setEditorData(self,editor,index):
        editor.blockSignals(True)
        editor.setText(index.model().data(index))        
        editor.blockSignals(False)

    def setModelData(self,editor,model,index):
        model.setData(index,editor.toPlainText(),Qt.EditRole)
    
    @pyqtSlot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())
 

class DateEditDelegate(QItemDelegate):
    def __init__(self,parent):
        QItemDelegate.__init__(self,parent)

    def createEditor(self,parent,option,index):
        date=QDateEdit(parent)
        date.setCalendarPopup(True)
        return date

    def setEditorData(self,editor,index):
        editor.blockSignals(True)
        d=index.model().data(index)
        if d != '':
            asTime=time.strptime(d,"%m/%d/%Y")
            asTuple=(asTime.tm_year,asTime.tm_mon,asTime.tm_mday)
            editor.setDate(QDate(*asTuple))
        #print(d)
        
        editor.blockSignals(False)

    def setModelData(self,editor,model,index):
        #model.setData(index,editor.
        #print(type(editor.date().getDate()))
        d="{1}/{2}/{0}".format(*editor.date().getDate())
        model.setData(index,d,Qt.EditRole)
        #print(editor.date())
    
    @pyqtSlot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())
    
class ComboBoxDelegate(QItemDelegate):
    def __init__(self,parent,values=[]):
        QItemDelegate.__init__(self,parent)
        self.values=values

    def createEditor(self,parent,option,index):
        box=QComboBox(parent)
        box.addItems(self.values)
        return box

    def setEditorData(self,editor,index):
        editor.blockSignals(True)
        editor.setCurrentText(index.model().data(index))
        editor.blockSignals(False)
    def setModelData(self,editor,model,index):
        model.setData(index,editor.currentText(),Qt.EditRole)

    @pyqtSlot()
    def currentIndexChanged(self):
       self.commitData.emit(self.sender())


class CheckBoxDelegate(QItemDelegate):
    def __init__(self,parent,state=False):
        QItemDelegate.__init__(self,parent)
        self.state=state

    def createEditor(self,parent,option,index):
        box=QCheckBox(parent)
        box.setChecked(self.state)
        return box

    def setEditorData(self,editor,index):
        editor.blockSignals(True)
        editor.setChecked(index.model().data(index))
        editor.blockSignals(False)

    def setModelData(self,editor,model,index):
        model.setData(index,editor.isChecked(),Qt.EditRole)

    @pyqtSlot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender()) 