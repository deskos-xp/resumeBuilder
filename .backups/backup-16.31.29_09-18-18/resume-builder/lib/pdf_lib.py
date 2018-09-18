#! /usr/bin/env python3

import createpdf2
import xml_lib
import os,sys
import lxml.etree
import shutil
sys.path.insert(0,'./resume-builder-templates/lib')
import balanced
import balanced_references
class pdf:
    statusBar=None
    tmpdir='./tmp'
    tmpRefXml='reference-tmp.xml'
    tmpResXml='resume-tmp.xml'
    referenceXml=None
    resumeXml=None
    compiledData=None
    referencesPDF='references.pdf'
    resumePDF='resume.pdf'
    docPath='./'
    def mkTempDoc(self,doc,data):
        with open(doc,'wb') as ofile:
            ofile.write(data)

    def mkTemp(self,doc,statusBar):
        self.tmpdir=os.path.join(os.environ['HOME'],self.tmpdir)
        if not os.path.exists(self.tmpdir):
            os.mkdir(self.tmpdir)
        xmlGen=xml_lib.data()
        xmlGen.master=self.compiledData
        print('#compiled data#',self.compiledData)
        docs=xmlGen.mkDocs()
        if doc == 'references':
            if docs[1] != None:
                data=lxml.etree.tostring(docs[1])
                path=os.path.join(self.tmpdir,self.tmpRefXml)
                self.mkTempDoc(path,data)
                '''
                xml=createpdf2.readXmlDoc()
                xml.referencesXml=path
                references,contact=xml.readReferences()

                build=createpdf2.gen()
                build.docPath=self.docPath
                build.referencesPDF=self.referencesPDF
                build.genReferencesDoc(references,contact)
                '''
                build=balanced_references.referencesGen()
                build.referencesXml=path
                build.referencesPdf=os.path.join(self.docPath,self.referencesPDF)
                build.tasks()
                shutil.rmtree(self.tmpdir)
            else:
                msg='Not enough information to create document!'
                print(msg)
                statusBar.showMessage(msg)
        elif doc == 'resume':
            if docs[0] != None:
                data=lxml.etree.tostring(docs[0])
                path=os.path.join(self.tmpdir,self.tmpResXml)
                self.mkTempDoc(path,data)
                #old code stays for now
                #just in a stitch is needed
                '''
                xml=createpdf2.readXmlDoc()
                xml.resumeXml=path
                resume=xml.getResume()
                '''

                build=balanced.resumeGen()
                build.resumePDF=self.resumePDF
                build.resumeXML=path
                res=build.tasks()
                if self.statusBar != None:
                    if res == False:
                        self.statusBar().showMessage('Error entry too big! resume PDF was not created!')
                '''
                build=createpdf2.gen()
                build.docPath=self.docPath
                build.resumePDF=self.resumePDF
                build.genResume(resume)
                '''

                shutil.rmtree(self.tmpdir)
            else:
                msg='Not enough information to create document!'
                print(msg)
                statusBar.showMessage(msg)

    def mkDoc(self,doc,statusBar):
        self.mkTemp(doc,statusBar)
