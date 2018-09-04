#! /usr/bin/env python3
from PyQt5 import QtGui,QtWidgets,QtCore
import import_xml
import os,sys
class importer:
    def __init__(self):
        pass

    def setContactTabFields(self,obj):
        self.bar('Contact')
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
        c.phoneType.setCurrentText(obj['type'])
        self.contact_submit(c)

    def import_getFname(self,ext='xml',docType=''):
        fname=QtWidgets.QFileDialog.getOpenFileName(self,'Import {} {}'.format(ext,docType),os.environ['HOME'],filter='{0} Files (*.{0})'.format(ext))
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
    def bar(self,msg):
        self.statusBar().showMessage('Importing {} Data!'.format(msg))

    def resumeGetEmployer(self,fields):
        self.bar('Employment')
        emp=fields['work_xp']
        for num,work in enumerate(emp.keys()):
            self.newEmployer()
            b=self.groupBox_emp[str(num)][1]
            b.lineEdit_16.setText(emp[work]['employer'])
            b.lineEdit_9.setText(emp[work]['title'])
            #set dates
            self.mkStartDate(emp[work]['startDate'],b.startDate)
            #b.startDate.setDate(startDate)
            self.mkEndDate(emp[work]['endDate'],b)
            #set dates
            b.comboBox_2.setCurrentText(emp[work]['state'])
            b.textEdit.setPlainText(emp[work]['duties'])
            b.lineEdit_14.setText(emp[work]['zip'])
            b.lineEdit_15.setText(emp[work]['city'])
        self.emp_submit()

    def mkEndDate(self,dString,obj):
        if dString == 'Present':
            try:
                obj.checkBox.setChecked(True)
            except:
                print('invalid "Present"')
                pass
        else:
            endDate=QtCore.QDate()
            endDate=endDate.fromString(dString,'MMMM d, yyyy')
            obj.endDate.setDate(endDate)


    def mkStartDate(self,dString,obj):
        startDate=QtCore.QDate()
        startDate=startDate.fromString(dString,'MMMM d, yyyy')
        obj.setDate(startDate)

    def resumeGetSchool(self,fields):
        self.bar('Education')
        schools=fields['schools']
        for num,school in enumerate(schools.keys()):
            self.newSchool()
            b=self.groupBox_school[str(num)][1]
            b.name.setText(schools[school]['school'])
            b.degree.setText(schools[school]['degree'])
            #set dates
            self.mkStartDate(schools[school]['startDate'],b.startDate)
            self.mkEndDate(schools[school]['endDate'],b)
            #set dates
            b.state.setCurrentText(schools[school]['state'])
            b.zip.setText(schools[school]['zip'])
            b.city.setText(schools[school]['city'])
            b.school_type_edit.setText(schools[school]['type'])
            b.school_type.setCurrentText(schools[school]['type'])
        self.school_submit()

    def resumeGetCert(self,fields):
        self.bar('Certification')
        certs=fields['certs']
        for num,cert in enumerate(certs.keys()):
            self.newCert()
            b=self.groupBox_cert[str(num)][1]
            b.name.setText(certs[cert]['name'])
            self.mkStartDate(certs[cert]['startDate'],b.startDate)
            self.mkEndDate(certs[cert]['endDate'],b)
        self.cert_submit()

    def resumeGetSkill(self,fields):
        self.bar('Skill')
        skills=fields['skills']
        for num,skill in enumerate(skills.keys()):
            print('#{}# "{}" m "{}" y'.format(skills[skill]['skill'],skills[skill]['months'],skills[skill]['years']))
            self.newSkill()
            b=self.groupBox_skill[str(num)][1]
            
            b.name.setText(skills[skill]['skill'])
            if skills[skill]['months'] == '':
                mval=0
            else:
                try:
                    mval=int(skills[skill]['months'])
                except:
                    mval=0

            b.months.setValue(mval)

            if skills[skill]['years'] == '':
                yval=0
            else:
                try:
                    yval=int(skills[skill]['years'])
                except:
                    yval=0

            b.years.setValue(yval)
            
            grade=skills[skill]['grade']
            if grade == '+':
                b.gthan.setChecked(True)
            elif grade == '-':
                b.lthan.setChecked(True)
            else:
                b.eqto.setChecked(True)
        self.skill_submit()

    def resumeGetLink(self,fields):
        self.bar('Link')
        links=fields['links']
        for num,link in enumerate(links.keys()):
            self.newLink()
            b=self.groupBox_link[str(num)][1]
            b.link.setText(links[link]['link'])
        self.link_submit()

    def resumeGetAi(self,fields):
        self.bar('Additional Information')
        lines=fields['additional_info']
        keys=[i for i in lines.keys() if lines[i] != {'line':''}]
        for num,line in enumerate(keys):
            text=lines[line]['line']
            if text != '':
                self.newAi()
                b=self.groupBox_ai[str(num)][1]
                print('{} "{}"'.format(lines,text.encode()))
                b.line.setPlainText(text)
                t=lines[line]['type']
                if t == 'Disabled':
                    b.skip_type.setChecked(True)
                else:
                    if t not in self.aiTypes:
                        b.ai_type.setCurrentText('Other')
                        b.ai_type_edit.setText(t)
                    else:
                        b.ai_type.setCurrentText(t)
        self.ai_submit()

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
            self.resumeGetEmployer(resumeFields)
            self.resumeGetSchool(resumeFields)
            self.resumeGetCert(resumeFields)
            self.resumeGetSkill(resumeFields)
            self.resumeGetLink(resumeFields)
            self.resumeGetAi(resumeFields)
            self.gen_compile_data()
        else:
            print("user hit cancel, most likely!")
    
    def referencesClearWidgets(self):
        if self.groupBox_ref != None:
            k=[self.groupBox_ref[i] for i in self.groupBox_ref.keys()]
            for num,i in enumerate(k):
                self.ref_remove(self.groupBox_ref[str(num)][0],num)
            self.groupBox_ref=None
            self.contact_clear(self.groupBox_contact['0'][1])

    def getReferences(self,referencesEmp):
        self.bar('References')
        print(referencesEmp)
        for num,ref in enumerate(referencesEmp.keys()):
            self.newRef()
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
        self.ref_submit()
        self.gen_compile_data()

    def getRefData(self):
        x=import_xml.get_xml()
        x.references=self.import_getFname(ext='xml',docType='References')
        if x.references != None:        
            self.referencesClearWidgets()

            refXml=x.getXml(x.references)[1]
            referencesContact=x.contact(refXml)
            referencesEmp=x.referencesEmployer(refXml)
            print(referencesEmp)
                    
            self.setContactTabFields(referencesContact)
            self.getReferences(referencesEmp)
            self.ref_submit()
            self.gen_compile_data()
        else:
            print('file does not exist!')



    def im_buttons_connect(self):
        self.actionImport_References.triggered.connect(self.getRefData)
        self.actionImport_Resume.triggered.connect(self.getResumeData)
