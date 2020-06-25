from PyQt5.QtCore import QObject,QRunnable,QThread,QThreadPool,pyqtSignal,pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
import os,sys,time

from ..MainWindow.default_fields import *
from ..MainWindow.ModelDelegates import *
from ..MainWindow.TableModel import TableModel,TableModelEnum
from .workers.ReadHelp import ReadHelp
from .workers.ReadLogo import ReadLogo
class Help(QDialog):
    def __init__(self,parent):
        super(Help,self).__init__()
        self.parent=parent
        self.model=TableModel(item=help_(),ReadOnly=TableModelEnum.READONLY)
        uic.loadUi("app/Help/forms/help.ui",self)
        
        def load_data(data):
            self.logoPath=data.get("logo")
            self.readLogo=ReadLogo("app/MainWindow/{}".format(self.logoPath))
            self.readLogo.signals.hasError.connect(lambda x:print(x))
            self.readLogo.signals.hasQPixmap.connect(self.logo.setPixmap)
            self.readLogo.signals.finished.connect(lambda:print("finished reading logo"))
            QThreadPool.globalInstance().start(self.readLogo)

            self.logo.setText(self.logoPath)
            data.__delitem__("logo")
            self.model.load_data(data,re=True)

        self.rh=ReadHelp("app/MainWindow/about.json")
        self.rh.signals.hasError.connect(lambda x:print(x))
        self.rh.signals.hasHelp.connect(load_data)
        self.rh.signals.finished.connect(lambda: print("done reading config"))
        QThreadPool.globalInstance().start(self.rh)

        self.view.setModel(self.model)
        prep_table(self.view)

        self.exec_()
