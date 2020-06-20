from PyQt5 import uic
from PyQt5.QtCore import QRunnable,QObject,QThread,QThreadPool
from PyQt5.QtWidgets import QApplication,QMainWindow
from .MainWindow.TableModel import TableModel
from .Contact.Contact import Contact
from .Employment.Employment import Employment
from .Education.Education import Education
from .MenuBar.MenuBar import MenuBar
from .Certification.Certification import Certification
from .Links.Links import Links
from .AdditionalInfo.AdditionalInfo import AdditionalInfo
from .References.References import References
from .Json.Json import Json
from copy import deepcopy
from .ReferencesBuilder.ReferencesBuilder import ReferencesBuilder
from .ResumeBuilder.ResumeBuilder import ResumeBuilder
class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        uic.loadUi("app/MainWindow/forms/app.ui",self)
        self.tabs={}
        self.tabs['contact']=Contact(self)
        self.tabs['employment']=Employment(self)
        self.tabs['education']=Education(self)
        self.tabs['certification']=Certification(self)
        self.tabs['links']=Links(self)
        self.tabs['additionalInfo']=AdditionalInfo(self)
        self.tabs['references']=References(self)

        self.submit_json.clicked.connect(self.saveData)
        self.submit_resume.clicked.connect(self.saveData)
        self.submit_references.clicked.connect(self.saveData)

        self.references=ReferencesBuilder(self)
        self.resume=ResumeBuilder(self)

        self.j=Json(self)        
        self.mb=MenuBar(self)

    def saveData(self):
        data={}
        for i in self.tabs.keys():
            if i in ['employment','education','certification','links','additionalInfo','references']:
                data[i]=[]
                for model in self.tabs[i].models:
                    data[i].append(deepcopy(model.item))
                    #print(model.item)
            else:
                data[i]=deepcopy(self.tabs.get(i).model.item)
                #print(self.tabs.get(i).model.item)
        name=self.sender().objectName()
        print(name)
        if name == "submit_json":
            self.j.setData(data)
        elif name == "submit_references":
            self.references.load_data(data,self.references_path_pdf.text())
            self.references.gen()
        elif name == "submit_resume":
            self.resume.load_data(data)
            self.resume.gen()
            
def main(*args):
    app=QApplication(list(args))
    win=Main()
    win.show()
    app.exec_()
