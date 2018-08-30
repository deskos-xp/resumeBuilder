#! /usr/bin/python3

from PyQt5 import QtGui,QtWidgets
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

class logic(QtWidgets.QMainWindow,resume_ui.Ui_MainWindow,empl.emp,school_widget.Ui_school,school_lib.school,certifications_widget.Ui_certs,certifications_lib.certs,skills_widget.Ui_skills,skills_lib.skills,additional_info_widget.Ui_additional_info,additional_info_lib.ai,links_widget.Ui_links,links_lib.links,references_widget.Ui_references,references_lib.ref,gen_lib.gen,checkers_lib.checkers):
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

        self.groupBox_emp=None
        self.groupBox_school=None
        self.groupBox_cert=None
        self.groupBox_skill=None
        self.groupBox_ai=None
        self.groupBox_link=None
        self.groupBox_ref=None

        self.setupUi(self)
        self.combobox()
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

        self.contact_tab_orders()
        self.contact_phone_check()
        self.contact_invalidUntilFilled()

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
    def contact_invalidUntilFilled_email(self,qtype):
        if len(self.lineEdit_5.text()) > 0:
            self.setValidFields(self.lineEdit_3)
        else:
            self.setInvalidFields(self.lineEdit_3)
        self.invalidUntilFilled(qtype,self.lineEdit_5)

    def contact_invalidUntilFilled(self): 
        self.setInvalidFields(self.lineEdit)
        self.lineEdit.textChanged.connect(lambda:self.invalidUntilFilled('le',self.lineEdit))

        self.setInvalidFields(self.lineEdit_2)
        self.setInvalidFields(self.lineEdit_4)
        self.setInvalidFields(self.lineEdit_5)
        self.setInvalidFields(self.lineEdit_6)
        self.setInvalidFields(self.lineEdit_7)
        self.setInvalidFields(self.lineEdit_8)
        
        self.lineEdit_2.textChanged.connect(lambda:self.invalidUntilFilled('le',self.lineEdit_2))
        self.lineEdit_4.textChanged.connect(lambda:self.invalidUntilFilled('le',self.lineEdit_4))
        self.lineEdit_5.textChanged.connect(lambda:self.contact_invalidUntilFilled_email('le'))
        self.lineEdit_6.textChanged.connect(lambda:self.invalidUntilFilled('le',self.lineEdit_6))
        self.lineEdit_7.textChanged.connect(lambda:self.invalidUntilFilled('le',self.lineEdit_7))
        self.lineEdit_8.textChanged.connect(lambda:self.invalidUntilFilled('le',self.lineEdit_8))

    def quit(self):
        self.actionExit.triggered.connect(QtWidgets.QApplication.quit)
   
    def next_submit(self,tabname,nextTab):
        calls={'Contact':self.contact_submit,'Employment':self.emp_submit,'Education':self.school_submit,'Certifications':self.cert_submit,'Skills':self.skill_submit,'Links':self.link_submit,'Additional Information':self.ai_submit,'References':self.ref_submit}
        if tabname in calls.keys():
            call=calls[tabname]
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

    def contact_proper_phone(self):
        if len(self.lineEdit_3.text()) > 0:
            phone=''.join([i for i in self.lineEdit_3.text() if i in ['1','2','3','4','5','6','7','8','9','0']])
            if len(phone) in [7,10,11]:
                self.contact_invalid_phone.hide()
                self.setValidFields(self.lineEdit_3)
                self.setValidFields(self.lineEdit_5)
            else:
                self.contact_invalid_phone.show()
                self.setInvalidFields(self.lineEdit_3)
                self.setInvalidFields(self.lineEdit_5)
        else:
            self.contact_invalid_phone.show()
            self.setInvalidFields(self.lineEdit_5)
            if len(self.lineEdit_5.text()) < 1:
                self.setInvalidFields(self.lineEdit_3)
            else:
                self.setValidFields(self.lineEdit_3)

    def contact_phone_check(self):
        self.lineEdit_3.setMaxLength(16)
        self.setInvalidFields(self.lineEdit_3)
        self.lineEdit_3.textChanged.connect(self.contact_proper_phone)

    def nextCallBack(self):
        tab=self.tabWidget.currentIndex()
        self.tabWidget.setCurrentIndex(tab+1)
        tname=self.tabWidget.tabText(tab)
        tnameNext=self.tabWidget.tabText(tab+1)
        self.next_submit(tname,tnameNext)

    def previousCallBack(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex()-1)
        
    def previous(self):
        self.pushButton_5.clicked.connect(self.previousCallBack)
        self.pushButton_7.clicked.connect(self.contact_submit)
        self.pushButton_8.clicked.connect(self.previousCallBack)
        self.pushButton_12.clicked.connect(self.previousCallBack)
        self.pushButton_16.clicked.connect(self.previousCallBack)
        self.pushButton_20.clicked.connect(self.previousCallBack)
        self.pushButton_29.clicked.connect(self.previousCallBack)
        self.pushButton_24.clicked.connect(self.previousCallBack)
        self.pushButton_36.clicked.connect(self.previousCallBack)

    def next(self):
        self.pushButton.clicked.connect(self.nextCallBack)
        self.pushButton_4.clicked.connect(self.nextCallBack)
        self.pushButton_2.clicked.connect(self.contact_clear)
        self.pushButton_11.clicked.connect(self.nextCallBack)
        self.pushButton_15.clicked.connect(self.nextCallBack)
        self.pushButton_19.clicked.connect(self.nextCallBack)
        self.pushButton_23.clicked.connect(self.nextCallBack)
        self.pushButton_32.clicked.connect(self.nextCallBack)
        self.pushButton_27.clicked.connect(self.nextCallBack)

    def combobox(self):
        for state in self.states:
            self.comboBox.addItem(state)

    def contact_submit(self):
        contact={}
        contact['fname']=self.lineEdit.text()
        contact['lname']=self.lineEdit_2.text()
        contact['mname']=self.lineEdit_4.text()
        contact['email']=self.lineEdit_5.text()
        contact['phone']=self.lineEdit_3.text()
        contact['street']=self.lineEdit_6.text()
        contact['zip']=self.lineEdit_7.text()
        contact['city']=self.lineEdit_8.text()
        contact['state']=str(self.comboBox.currentText())
        count=0
        contactCount=0
        for key in contact.keys():
            if contact[key] == '':
                if key in ['email','phone']:
                    if contact[key]=='':
                        contactCount+=1
                    if contactCount > 1:
                        count+=1
                else:
                    if key != 'mname':
                        count+=1
        if count == 0:
            self.contact_data=contact
        else:
            self.contact_data={}
        print(self.contact_data)

    def contact_tab_orders(self):
        tabChains=[
                [self.lineEdit,self.lineEdit_4],
                [self.lineEdit_4,self.lineEdit_2],
                [self.lineEdit_2,self.lineEdit_5],
                [self.lineEdit_5,self.lineEdit_3],
                [self.lineEdit_3,self.lineEdit_6],
                [self.lineEdit_6,self.lineEdit_8],
                [self.lineEdit_8,self.comboBox],
                [self.comboBox,self.lineEdit_7],
                ]
        for p1,p2 in tabChains:
            self.setTabOrder(p1,p2)

    def contact_clear(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
        self.comboBox.setCurrentText('Set Your State')

def main():
    app=QtWidgets.QApplication(sys.argv)
    form=logic()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
