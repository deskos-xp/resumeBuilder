#! /usr/bin/env python3
from PyQt5 import QtGui,QtWidgets,QtCore
import import_xml

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

    def getFname(self,ext='xml'):
        pass
        #get filename 

    def getRefData(self):
        x=import_xml.get_xml()
        x.references='./templates/xml/references/references.xml'
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



    def im_buttons_connect(self):
        self.actionImport_References.triggered.connect(self.getRefData)
