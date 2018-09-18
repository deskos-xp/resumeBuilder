#! /usr/bin/env python3
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QMessageBox
import time,json
import os,sys
sys.path.insert(0,'./lib')
import xml_lib
import pdf_lib
import lxml.etree
import string
#sys.path.insert(0,'./resume-builder-templates/lib')
class gen:
    compiledData={}
    prefix='first_last'
    def gen_compile_data(self):
        #call this function when any buttons on gen tab are used,
        #save for the previous button
        
        compiledData={
                'employment':self.employer_data,
                'contact':self.contact_data,
                'education':self.school_data,
                'certifications':self.cert_data,
                'skills':self.skill_data,
                'links':self.link_data,
                'additional_info':self.ai_data,
                'references':self.ref_data
                }
        self.compiledData=compiledData
        if compiledData['contact'] != {}:
            self.prefix='{}_{}'.format(compiledData['contact']['fname'],compiledData['contact']['lname'])
        print(self.compiledData)

    def mkPath(self,fname):
        print('\033[1;31;40m{}\033[1;40;m'.format(fname))
        if fname != '':
            if os.path.exists(fname):
                if os.path.isdir(fname):
                    path=fname
                else:
                    path=os.path.dirname(fname)
            else:
                path=os.environ['HOME']
        else:
            path=path=os.environ['HOME']
        return path

    def getFName(self,ext,default,data=None,returnName=False):
        fname=self.save.text()
        path=self.mkPath(fname)
        fnameDialog=['']
        while fnameDialog[0] == '':
            fnameDialog=QtWidgets.QFileDialog.getSaveFileName(self,'Save as {}'.format(ext),os.path.join(path,'{}.{}'.format('{}-{}'.format(self.prefix,default),ext)),filter='{0} Files(*.{0})'.format(ext))
            if fnameDialog != ('',''):
                fnameDialog=self.verifyFname(fnameDialog) 
                if fnameDialog[0] == '':
                    errorDialog=QtWidgets.QErrorMessage()
                    errorDialog.showMessage('Invalid File Name!')
                else:
                    if os.path.splitext(fnameDialog[0])[1] == '':
                        fnameDialog=['{}.{}'.format(fnameDialog[0],ext),fnameDialog[1]]
            else:
                break
        #force extension
                
        if fnameDialog[0] != '':
            self.save.setText(fnameDialog[0])

        if data != None:
            if fnameDialog[0] != '':
                with open(fnameDialog[0],'wb') as ofile:
                    ofile.write(data)
        if returnName == True:
            return fnameDialog[0]

    def verifyFname(self,fnameDialog):
        for char in string.whitespace:
            text=os.path.basename(fnameDialog[0]).split(char)
            count=0
            check=len(text)
            for x in text:
                if x == '':
                    count+=1

            if count == check:
                fnameDialog=['']
                return fnameDialog
            second=string.ascii_letters+string.digits+string.punctuation
            count=0
            check=len(second)
            for char in second:
                if char not in os.path.basename(fnameDialog[0]):
                    count+=1
            if count == check:
                fnameDialog=['']
                return fnameDialog
        return fnameDialog


    def gen_pdf(self,doc):
        self.gen_compile_data()
        pdf=pdf_lib.pdf()
        pdf.statusBar=self.statusBar
        pdf.compiledData=self.compiledData
        if doc == 'resume':
            pdf.resumePDF=self.getFName('pdf','resume',returnName=True)
        elif doc == 'references':
            pdf.referencesPDF=self.getFName('pdf','references',returnName=True)

        if pdf.referencesPDF != '' and doc == 'references':
            pdf.mkDoc(doc,self.statusBar())
        if pdf.resumePDF != '' and doc == 'resume':
            pdf.mkDoc(doc,self.statusBar())

    def gen_xml(self,doc):
        self.gen_compile_data()
        xmlGen=xml_lib.data()
        xmlGen.master=self.compiledData
        docs=xmlGen.mkDocs()
        if doc == 'resume':
            self.getFName('xml','resume',lxml.etree.tostring(docs[0]))
        elif doc == 'references':
            ref=docs[1]
            if docs[1] != None:
                ref=lxml.etree.tostring(docs[1])
                self.getFName('xml','references',ref)
            else:
                msg="Missing information required to make references doc"
                print(msg)
                self.statusBar().showMessage(msg)
        else:
            print('invalid option provided')

    def gen_json(self):
        self.gen_compile_data()
        jsonData=json.dumps(self.compiledData)
        fname=self.getFName('json','all',jsonData.encode())

    def gen_set_tab_orders(self):
        tabChains=[
                [self.pushButton_36,self.save],
                [self.save,self.pushButton_33],
                [self.pushButton_33,self.pushButton_28],
                [self.pushButton_28,self.pushButton_37],
                [self.pushButton_37,self.pushButton_34],
                [self.pushButton_34,self.pushButton_35],
                [self.pushButton_35,self.pushButton_38],
                ]
        for p1,p2 in tabChains:
            QtWidgets.QWidget().setTabOrder(p1,p2)

    def gen_buttons_connect(self):
        self.pushButton_33.clicked.connect(self.gen_json)
        self.pushButton_37.clicked.connect(lambda:self.gen_xml('resume'))
        self.pushButton_28.clicked.connect(lambda:self.gen_xml('references'))
        self.pushButton_35.clicked.connect(lambda:self.gen_pdf('references'))
        self.pushButton_34.clicked.connect(lambda:self.gen_pdf('resume'))
        self.pushButton_38.clicked.connect(QtWidgets.QApplication.quit)
        self.gen_set_tab_orders()
