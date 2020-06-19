from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

import os,sys,json
from ..MainWindow.default_fields import *
from ..MainWindow.ModelDelegates import *
from ..MainWindow.TableModel import TableModel

class Skills:
    def __init__(self,parent):
        self.parent=parent


        self.parent.newSkill.clicked.connect(self.newSkill)

    def newSkill(self,state):
        pass
