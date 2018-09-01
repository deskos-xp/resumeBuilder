#! /usr/bin/env python3
from PyQt5 import QtGui,QtWidgets,QtCore
import import_xml
import os,sys
class importer:
    def __init__(self):
        pass

    def setContactTabFields(self,obj):
        c=self.groupBox_contact['0'][1]
        c.fname.setText(obj['fname'])
        c.lname.setText(obj['lname'])
        c.mname.setText(obj['mname'])
        c.email.setText(obj['email'])
        c.phone.setText(obj['phone'])
        c.street.setText(obj['street'])
        c.city.setText(obj['city'])
        c.state.setCurrentText(obj['state'])
        c.zip.setText(obj['zip'])

    def import_getFname(self,ext='xml',docType=''):
        fname=QtWidgets.QFileDialog.getOpenFileName(self,'Import {} {}'.format(ext,docType),'.',filter='{0} Files (*.{0})'.format(ext))
        if fname[0]:
            if os.path.exists(fname[0]):
                return fname[0]
            else:
                return None
        else:
            return None

    def resumeClearWidgets_emp(self):
        if self.groupBox_emp != None:
            k=[self.groupBox_emp[i] for i in self.groupBox_emp.keys()]
            for num,i in enumerate(k):
                self.emp_remove(self.groupBox_emp[str(num)][0],num)
            self.groupBox_emp=None

    def resumeClearWidgets_contact(self):
        self.contact_clear(self.groupBox_contact['0'][1])

    def resumeClearWidgets_school(self):
        if self.groupBox_school != None:
            k=[self.groupBox_school[i] for i in self.groupBox_school.keys()]
            for num,i in enumerate(k):
                self.school_remove(self.groupBox_school[str(num)][0],num)
            self.groupBox_school=None

    def resumeClearWidgets_cert(self):
        if self.groupBox_cert != None:
            k=[self.groupBox_cert[i] for i in self.groupBox_cert.keys()]
            for num,i in enumerate(k):
                self.cert_remove(self.groupBox_cert[str(num)][0],num)
            self.groupBox_cert=None
    def resumeClearWidgets_skill(self):
        if self.groupBox_skill != None:
            k=[self.groupBox_skill[i] for i in self.groupBox_skill.keys()]
            for num,i in enumerate(k):
                self.skill_remove(self.groupBox_skill[str(num)][0],num)
            self.groupBox_skill=None

    def resumeClearWidgets_ai(self):
        if self.groupBox_ai != None:
            k=[self.groupBox_ai[i] for i in self.groupBox_ai.keys()]
            for num,i in enumerate(k):
                self.ai_remove(self.groupBox_ai[str(num)][0],num)
            self.groupBox_ai=None

    def resumeClearWidgets_link(self):
        if self.groupBox_link != None:
            k=[self.groupBox_link[i] for i in self.groupBox_link.keys()]
            for num,i in enumerate(k):
                self.link_remove(self.groupBox_link[str(num)][0],num)
            self.groupBox_link=None


    def resumeClearWidgets(self):
        self.resumeClearWidgets_emp()
        self.resumeClearWidgets_contact()
        self.resumeClearWidgets_school()
        self.resumeClearWidgets_cert()
        self.resumeClearWidgets_skill()
        self.resumeClearWidgets_ai()
        self.resumeClearWidgets_link()

    def getResumeData(self):
        x=import_xml.get_xml()
        x.resume=self.import_getFname(ext='xml',docType='Resume')
        if x.resume != None:
            self.resumeClearWidgets()
        resXml=x.getXml(x.resume)[1]
        resumeContact=x.contact(resXml)
        resumeFields=x.getResumeFields(resXml)
        x.printResDict(resumeFields)
        self.setContactTabFields(resumeContact)
        
        #individual functions for each tab should be used beyond this point in the function

    def getRefData(self):
        x=import_xml.get_xml()
        x.references=self.import_getFname(ext='xml',docType='References')
        if x.references != None:        
            if self.groupBox_ref != None:
                k=[self.groupBox_ref[i] for i in self.groupBox_ref.keys()]
                for num,i in enumerate(k):
                    self.ref_remove(self.groupBox_ref[str(num)][0],num)
                self.groupBox_ref=None
                self.contact_clear(self.groupBox_contact['0'][1])

            refXml=x.getXml(x.references)[1]
            referencesContact=x.contact(refXml)
            referencesEmp=x.referencesEmployer(refXml)
            print(referencesEmp)
            for ref in referencesEmp.keys():
                self.newRef()
        
            self.setContactTabFields(referencesContact)
    
            for num,ref in enumerate(referencesEmp.keys()):
                b=self.groupBox_ref[str(num)][1]
                b.employer.setText(referencesEmp[ref]['employer'])
                b.title.setText(referencesEmp[ref]['title'])
                b.fname.setText(referencesEmp[ref]['fname'])
                b.lname.setText(referencesEmp[ref]['lname'])
                b.mname.setText(referencesEmp[ref]['mname'])
                b.phone.setText(referencesEmp[ref]['phone'])
                b.email.setText(referencesEmp[ref]['email'])
                b.street.setText(referencesEmp[ref]['street'])
                b.city.setText(referencesEmp[ref]['city'])
                b.state.setCurrentText(referencesEmp[ref]['state'])
                b.zip.setText(referencesEmp[ref]['zip'])
                b.phoneType.setCurrentText(referencesEmp[ref]['type'])
        else:
            print('file does not exist!')



    def im_buttons_connect(self):
        self.actionImport_References.triggered.connect(self.getRefData)
        self.actionImport_Resume.triggered.connect(self.getResumeData)
