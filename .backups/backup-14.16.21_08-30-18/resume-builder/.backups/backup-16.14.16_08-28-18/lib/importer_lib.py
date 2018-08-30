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
        fname=QtWidgets.QFileDialog.getOpenFileName(self,'Import {} {}'.format(ext,docType),'.')
        if fname[0]:
            if os.path.exists(fname[0]):
                return fname[0]
            else:
                return None
        else:
            return None

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
