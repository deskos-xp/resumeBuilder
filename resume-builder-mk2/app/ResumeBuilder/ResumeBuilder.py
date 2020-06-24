from PyQt5.QtCore import QThreadPool
from .workers.genResume import genResume
from PyQt5.QtWidgets import QFileDialog
import os
class ResumeBuilder:
    def __init__(self,parent):
        self.parent=parent
        self.data=dict()
        self.contact=dict()
        self.path=parent.resume_path_pdf.text()
        #parent.submit_resume.clicked.connect(self.gen)
        parent.navigate_resume_pdf.clicked.connect(self.getPath)
        def setPath(text):
            self.path=text
        parent.resume_path_pdf.textChanged.connect(setPath)


    def getPath(self):
        path=QFileDialog.getSaveFileName(self.parent,"Save Resume PDF",'',"PDF/pdf Files(*.pdf);;All Files(*)",options=QFileDialog.DontUseNativeDialog)
        if path:
            if path[0]:
                self.parent.resume_path_pdf.setText(path[0])

    def load_data(self,data):
        self.contact=data.get("contact")
        for i in data.keys():
            if i not in ['contact','references']:
                self.data[i]=data.get(i)

    def gen(self):
        self.path=self.parent.resume_path_pdf.text()
        if self.path != "":
            if os.path.exists(os.path.split(os.path.abspath(self.path))[0]):
                self.worker=genResume(self.parent,self.data,self.contact,self.path)
                QThreadPool.globalInstance().start(self.worker)
