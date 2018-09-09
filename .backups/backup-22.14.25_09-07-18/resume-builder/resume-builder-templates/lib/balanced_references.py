#! /usr/bin/env python3
########################
# NoGuiLinux           #
# Generate References  #
# Sheet                #
########################

import import_xml
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
        self.xml=import_xml.get_xml()
        self.xml.referencesXml=self.referencesXml
        self.docX=self.xml.returnXml(self.xml.referencesXml)
        if self.docX != None:
            self.data=self.xml.referencesGetAllFields(self.docX) 
            return True
        else:
            self.data=None
            return None

    def tasks(self):
        self.init()
        com=self.func.doc_init(self.referencesPdf)
        self.docP=com[0]
        self.story=com[1]
        content=[] 
        calls=[self.func.header]
        for call in calls:
            if call == self.func.header:
                res=call(data=self.data['contact'])
                if res != None:
                    content.extend(res)
        for i in content:
            if i != None:
                self.story.append(i)
        self.docP.build(self.story)

if __name__ == '__main__':
    gen=referencesGen()
    gen.tasks()
