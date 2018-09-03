#! /usr/bin/python3

from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5 import Qt
import sys
sys.path.insert(0,'./lib')
sys.path.insert(0,'./widgets_lib')
import resume_ui
import employer_widget
import empl
import school_widget
import school_lib
import certifications_widget
import certifications_lib
import skills_widget
import skills_lib
import additional_info_widget
import additional_info_lib
import links_widget
import links_lib
import references_widget
import references_lib
import gen_lib
import checkers_lib
import string
import contact_widget
import contact_lib
import importer_lib
import import_json

class logic(QtWidgets.QMainWindow,resume_ui.Ui_MainWindow,empl.emp,school_widget.Ui_school,school_lib.school,certifications_widget.Ui_certs,certifications_lib.certs,skills_widget.Ui_skills,skills_lib.skills,additional_info_widget.Ui_additional_info,additional_info_lib.ai,links_widget.Ui_links,links_lib.links,references_widget.Ui_references,references_lib.ref,gen_lib.gen,contact_widget.Ui_contact,contact_lib.contact,importer_lib.importer,import_json.get_json):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.employer_data=None
        self.contact_data=None
        self.school_data=None
        self.cert_data=None
        self.skill_data=None
        self.link_data=None
        self.ai_data=None
        self.ref_data=None
        self.states='''Set Your State
Alabama
Alaska
Arizona
Arkansas
California
Colorado
Connecticut
Delaware
Florida
Georgia
Hawaii
Idaho
Illinois
Indiana
Iowa
Kansas
Kentucky
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
Nebraska
Nevada
New Hampshire
New Jersey
New Mexico
New York
North Carolina
North Dakota
Ohio
Oklahoma
Oregon
Pennsylvania
Rhode Island
South Carolina
South Dakota
Tennessee
Texas
Utah
Vermont
Virginia
Washington
West Virginia
Wisconsin
Wyoming'''.split('\n')
        self.phoneTypes='''
Phone Type
Home
Work
Cell'''.split('\n')
        self.phoneTypes=[i for i in self.phoneTypes if i != '']

        self.groupBox_contact=None
        self.groupBox_emp=None
        self.groupBox_school=None
        self.groupBox_cert=None
        self.groupBox_skill=None
        self.groupBox_ai=None
        self.groupBox_link=None
        self.groupBox_ref=None
        self.counted={}
        self.dFormat='MMMM d, yyyy'

        self.setupUi(self)
        #self.contact_combobox()
        self.next()
        self.previous()
        self.quit()
        
        self.emp_buttons_connect()
        self.school_buttons_connect()
        self.cert_buttons_connect()
        self.skill_buttons_connect()
        self.ai_buttons_connect()
        self.link_buttons_connect()
        self.ref_buttons_connect()
        self.gen_buttons_connect()
        self.next_action_tab()
        self.newContact()
        self.im_buttons_connect()
        self.json_buttons_connect()
        self.timed()
        #self.contact_tab_orders()
        #self.contact_phone_check()
        #self.contact_invalidUntilFilled()

    def invalidUntilFilled(self,qtype,widget):
        if qtype == 'le':
            if len(widget.text()) < 1:
                self.setInvalidFields(widget)
            else:
                self.setValidFields(widget)
        if qtype == 'te':
            if len(widget.toPlainText()) < 1:
                self.setInvalidFields(widget)
            else:
                self.setValidFields(widget)
        self.validateFields()

    def entity(self,e):
        if e.isEnabled():
            self.actionNext.setEnabled(True)
        else:
            self.actionNext.setEnabled(False)

    def timed(self):
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.adjust_next)
        self.timer.start(500)

    def adjust_next(self):
        tab=self.tabWidget.currentIndex()
        handles=[tab]
        for i in handles:
            tname=self.tabWidget.tabText(i)
            if tname != 'Gen':
                t=[
                        ('Contact',self.pushButton),
                        ('Employment',self.pushButton_4),
                        ('Education',self.pushButton_11),
                        ('Certifications',self.pushButton_15),
                        ('Skills',self.pushButton_19),
                        ('Links',self.pushButton_32),
                        ('Additional Information',self.pushButton_23),
                        ('References',self.pushButton_27),
                    ]
                for tab,button in t:
                    if tname == tab:
                        self.entity(button)
            else:
                self.actionNext.setEnabled(False)
        self.previous_action_disable()
        #self.validateFields() 

    def previous_action_disable(self):
        if self.tabWidget.currentIndex() < 1:
            self.actionPrevious.setEnabled(False)
        else:
            self.actionPrevious.setEnabled(True)

    def next_action_tab(self):
        self.tabWidget.currentChanged.connect(self.adjust_next)
        
    def quit(self):
        self.actionExit.triggered.connect(QtWidgets.QApplication.quit)
   
    def next_submit(self,tabname,nextTab,widget):
        calls={'Contact':self.contact_submit,'Employment':self.emp_submit,'Education':self.school_submit,'Certifications':self.cert_submit,'Skills':self.skill_submit,'Links':self.link_submit,'Additional Information':self.ai_submit,'References':self.ref_submit}
        if tabname in calls.keys():
            call=calls[tabname]
            if tabname == 'Contact':
                call(self.groupBox_contact['0'][1])
            else:
                call()
        if nextTab == 'Gen':
            self.gen_compile_data()
        print(tabname)

    def setInvalidFields(self,widget):
        widget.setAutoFillBackground(True)
        p=widget.palette()
        p.setColor(QtGui.QPalette.Base,QtGui.QColor(255,0,0))
        #p.setColor(widget.backgroundRole(),QtGui.QColor(255,0,0))
        p.setColor(QtGui.QPalette.Text,QtGui.QColor(255,255,255))
        widget.setPalette(p)

    def setValidFields(self,widget):
        widget.setAutoFillBackground(True)
        p=widget.palette()
        p.setColor(QtGui.QPalette.Base,QtGui.QColor(255,255,255))
        #p.setColor(widget.backgroundRole(),QtGui.QColor(255,255,255))
        p.setColor(QtGui.QPalette.Text,QtGui.QColor(0,0,0))
        widget.setPalette(p)
        self.validateFields()     

    def validateFields_internal(self,w,i,Num):
        tname=self.tabWidget.tabText(self.tabWidget.currentIndex())
        #need to get children of w
        a=[attr for attr in dir(w) if not callable(getattr(w,attr)) and not attr.startswith("__") and type(getattr(w,attr)) in (QtWidgets.QLineEdit,QtWidgets.QTextEdit,QtWidgets.QComboBox)]
        a=[i for i in a if i not in ['mname']]
        if i not in self.counted.keys():
            self.counted[i]={}
        self.counted[i][Num]={}
        self.counted[i][Num]['0']=0
        self.counted[i][Num]['1']=len(a)
        #print(self.counted)
        for num,x in enumerate(a):
            item=type(getattr(w,x))
            if item in [QtWidgets.QLineEdit,QtWidgets.QTextEdit,QtWidgets.QComboBox]:
                if item in [QtWidgets.QLineEdit,QtWidgets.QTextEdit]:
                    #print(item,x)
                    color=getattr(w,x).palette().color(QtGui.QPalette.Base)
                    red=color.red()
                    green=color.green()
                    blue=color.blue()            
                    colorT=(red,green,blue)
                    if x in ['mname']:
                        self.counted[i][Num]['0']+=1
                    if colorT == (255,255,255):
                        self.counted[i][Num]['0']+=1
                else:
                    #self.counted[i][Num]['1']+=1
                    if item in [QtWidgets.QComboBox]:
                        status=getattr(w,x).currentText()
                        if x == 'school_type':
                            self.counted[i][Num]['0']+=1
                        else:
                            if status not in ['Set Your State','Basic School Types','Phone Type']:
                                self.counted[i][Num]['0']+=1
                            else: 
                                if type(getattr(w,a[num-1])) == QtWidgets.QLineEdit:    
                                    content=getattr(w,a[num-1]).text()
                                    subc=getattr(w,a[num-1]).palette().color(QtGui.QPalette.Base)
                                    subColorT=(subc.red(),subc.green(),subc.blue())
                                    if subColorT == (255,255,255) and len(content) < 1:
                                        self.counted[i][Num]['0']+=1
                #print(self.counted[i][Num]['0'],i,self.counted[i][Num]['1'],tname,getattr(w,x).objectName())
                self.locker(i,Num)
    def locker(self,i,Num):
        states={
                'Contact':0,
                'Employment':0,
                'Education':0,
                'Certifications':0,
                'Skills':0,
                'Links':0,
                'Additional Information':0,
                'References':0,
                }
        up=0
        for key in self.counted.keys():
            tname=key
            for num in self.counted[key].keys():
                if tname in ['Contact','References']:
                    if self.counted[key][num]['0'] >= self.counted[key][num]['1']+up:
                        states[tname]+=1
                else:
                    if self.counted[key][num]['0'] >= self.counted[key][num]['1']:
                        states[tname]+=1

            if states[tname] >= len(self.counted[key].keys()):
                if tname == 'Employment':
                    self.pushButton_4.setEnabled(True)
                elif tname == 'Education':
                    self.pushButton_11.setEnabled(True)
                elif tname == 'Certifications':
                    self.pushButton_15.setEnabled(True)
                elif tname == 'Skills':
                    self.pushButton_19.setEnabled(True)
                elif tname == 'Links':
                    self.pushButton_32.setEnabled(True)
                elif tname == 'Additional Information':
                    self.pushButton_23.setEnabled(True)
                elif tname == 'References':
                    self.pushButton_27.setEnabled(True)
                elif tname == 'Contact':
                    self.pushButton.setEnabled(True)
                self.actionNext.setEnabled(True)
            else:
                if tname == 'Employment':
                    self.pushButton_4.setEnabled(False)
                elif tname == 'Education':
                    self.pushButton_11.setEnabled(False)
                elif tname == 'Certifications':
                    self.pushButton_15.setEnabled(False)
                elif tname == 'Skills':
                    self.pushButton_19.setEnabled(False)
                elif tname == 'Links':
                    self.pushButton_32.setEnabled(False)
                elif tname == 'Additional Information':
                    self.pushButton_23.setEnabled(False)
                elif tname == 'References':
                    self.pushButton_27.setEnabled(False)
                    #print(QtCore.QObject.findChildren(w,QtWidgets.QLineEdit))
                elif tname == 'Contact':
                    self.pushButton.setEnabled(False)
                self.actionNext.setEnabled(False)
        
    def validateFields(self):
        currentTab=self.tabWidget.currentIndex()
        boxes=[
            [self.groupBox_contact,'Contact'],
            [self.groupBox_emp,'Employment'],
            [self.groupBox_school,'Education'],
            [self.groupBox_cert,'Certifications'],
            [self.groupBox_skill,'Skills'],
            [self.groupBox_ai,'Additional Information'],
            [self.groupBox_link,'Links'],
            [self.groupBox_ref,'References'],
        ]
        for i in boxes:
            if i[0] != None:
                if type(i[0]) == type(dict()):
                    for num,key in enumerate(i[0].keys()):
                        w=i[0][key][1]
                        self.validateFields_internal(w,i[1],str(num))
                else:
                    self.validateFields_internal(i[0],i[1])

    def phoneStripper(self,number):
        phone=''.join([i for i in number if i in string.digits])
        return phone

    def nextCallBack(self,widget=None):
        tab=self.tabWidget.currentIndex()
        if tab > 0:
            self.actionPrevious.setEnabled(True)
        self.tabWidget.setCurrentIndex(tab+1)
        tname=self.tabWidget.tabText(tab)
        tnameNext=self.tabWidget.tabText(tab+1)
        self.next_submit(tname,tnameNext,widget)

    def previousCallBack(self):
        self.previous_action_disable()
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex()-1)
        
    def previous(self):
        self.pushButton_5.clicked.connect(self.previousCallBack)
        #self.pushButton_7.clicked.connect(self.contact_submit)
        self.pushButton_8.clicked.connect(self.previousCallBack)
        self.pushButton_12.clicked.connect(self.previousCallBack)
        self.pushButton_16.clicked.connect(self.previousCallBack)
        self.pushButton_20.clicked.connect(self.previousCallBack)
        self.pushButton_29.clicked.connect(self.previousCallBack)
        self.pushButton_24.clicked.connect(self.previousCallBack)
        self.pushButton_36.clicked.connect(self.previousCallBack)
        self.actionPrevious.triggered.connect(self.previousCallBack)

    def next(self):
        #self.pushButton.clicked.connect(self.nextCallBack)
        self.pushButton_4.clicked.connect(self.nextCallBack)
        #self.pushButton_2.clicked.connect(self.contact_clear)
        self.pushButton_11.clicked.connect(self.nextCallBack)
        self.pushButton_15.clicked.connect(self.nextCallBack)
        self.pushButton_19.clicked.connect(self.nextCallBack)
        self.pushButton_23.clicked.connect(self.nextCallBack)
        self.pushButton_32.clicked.connect(self.nextCallBack)
        self.pushButton_27.clicked.connect(self.nextCallBack)
        self.actionNext.triggered.connect(self.nextCallBack)

def main():
    app=QtWidgets.QApplication(sys.argv)
    form=logic()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
