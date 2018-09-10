#! /usr/bin/env python3
########################
# NoGuiLinux           #
# Generate References  #
# Sheet                #
########################

import import_xml_t
from reportlab.lib.enums import *
from reportlab.lib.pagesizes import letter
from reportlab.platypus import *
#SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import *
import reportlab.lib.styles
from reportlab.lib.units import inch
from reportlab.lib.colors import *
#set fonts
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os,sys
import balanced


class referencesGen:
    failedStates=None
    referencesXml='default-references.xml'
    referencesPdf='references.pdf'
    def init(self):
        #fuckk... bootstrapping......
        self.styling=balanced.styles()
        self.func=balanced.resumeGen()
        self.func.styling=self.styling
        self.failedStates=self.func.failedStates
        self.xml=import_xml_t.get_xml()
        self.xml.referencesXml=self.referencesXml
        self.docX=self.xml.returnXml(self.xml.referencesXml)
        if self.docX != None:
            self.data=self.xml.referencesGetAllFields(self.docX) 
            return True
        else:
            self.data=None
            return None

    def references(self,data=None):
        cell=TableStyle([
                ('ALIGN',(0,0),(-1,-1),'LEFT'),
                ('LINEBELOW',(0,0),(0,0),0.5,black),
                ('LINEBEFORE',(0,0),(0,0),0.2,gray),
                ('LINEAFTER',(0,0),(0,0),0.5,black),
                ('LINEABOVE',(0,0),(0,0),0.2,gray),
        ])

        normal=self.styling.document.normal
        normal.fontSize=10
        if data in self.failedStates:
            data=self.data['references']
        self.func.status('references data',data)
        if data not in self.failedStates:
            tbls=[]
            for key in data.keys():
                reference=[]
                name='{0} {1} {2}'.format(data[key]['fname'],data[key]['mname'],data[key]['lname'])
                self.func.status('name:',name)
                reference.append(Paragraph(name,self.styling.document.bold))
                reference.append(Paragraph(data[key]['title'],self.styling.document.italic))
                for skey in ['employer','street']:
                    reference.append(Paragraph(data[key][skey],normal))
                #start phone handling
                locale='{0}, {1} {2}'.format(data[key]['city'],data[key]['state'],data[key]['zip'])
                reference.append(Paragraph(locale,normal))
                
                region=data[key]['phone_region']
                local=data[key]['phone_local']
                if len(local) == 7:
                    local='{}-{}'.format(local[:3],local[3:])
                
                phone=''
                international=data[key]['phone_international']
                if region not in self.failedStates and international not in self.failedStates:
                    phone='+{} ({})-{}'.format(international,region,local)
                else:
                    phone='{}'.format(local)
                #end phone handling
                reference.append(Paragraph(phone,normal))
                reference=Table([[reference]])
                reference.setStyle(cell) 

                tbls.append(reference)
            
            tbls=Table(self.mk3Col(tbls))
            
            tbls.setStyle(self.styling.document.defaultTable)
            return [tbls]
        else:
            return None

    def mk3Col(self,table):
        chunk=3
        #shit i wish i had realized this in the resume generation script
        #this will make the three cols desired without the extra labor done in resumeGen
        cols=[table[i:i+chunk] for i in range(0,len(table),chunk)]
        return cols

    def tasks(self):
        self.init()
        com=self.func.doc_init(self.referencesPdf)
        self.docP=com[0]
        self.story=com[1]
        content=[] 
        calls=[self.func.header,self.references]
        for call in calls:
            if call == self.func.header:
                res=call(data=self.data['contact'])
                if res not in self.failedStates:
                    content.extend(res)
            else:
                res=call()
                if res not in self.failedStates:
                    content.extend(res)
        for i in content:
            if i != None:
                self.story.append(i)
        self.docP.build(self.story,onFirstPage=self.func.pageNum,onLaterPages=self.func.pageNum)

if __name__ == '__main__':
    gen=referencesGen()
    gen.tasks()
