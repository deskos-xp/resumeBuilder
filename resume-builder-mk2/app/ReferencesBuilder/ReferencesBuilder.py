from PyQt5.QtCore import QObject,QThreadPool,QRunnable
from PyQt5.QtWidgets import QWidget,QFileDialog
from .workers.genReferences import genReferences
from ..MainWindow.default_fields import *
import os
class ReferencesBuilder:
    def __init__(self,parent):
        self.parent=parent
        self.contact=dict()
        self.references=list()
        self.path=default_pdf
        parent.navigate_references_pdf.clicked.connect(self.getPath)

    def getPath(self):
        d=QFileDialog.getSaveFileName(self.parent,"Save References","","PDF/pdf files (*.pdf);;All files(*)",options=QFileDialog.DontUseNativeDialog)
        if d:
            if d[0]:
                self.path=d[0]
        self.parent.references_path_pdf.setText(d[0])

    def load_data(self,data,path):
        self.contact=data.get("contact")
        self.references=data.get("references")
        self.path=path

    def gen(self):
        self.path=self.parent.references_path_pdf.text()
        print(self.path)
        if self.path != "":
            if os.path.exists(os.path.split(os.path.abspath(self.path))[0]):
                def deleteMe():
                    del(self.generator)
                self.generator=genReferences(self.parent,self.contact,self.references,self.path)
                self.generator.signals.hasError.connect(lambda x:print(x))
                self.generator.signals.finished.connect(deleteMe)
                QThreadPool.globalInstance().start(self.generator)

        #print(self.contact,self.references)
