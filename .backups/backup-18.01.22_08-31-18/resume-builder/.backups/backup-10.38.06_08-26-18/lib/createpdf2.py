#!/usr/bin/env python
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer 
from reportlab.platypus.flowables import HRFlowable

#doc generation import
from xml.etree.ElementTree import Element as element,SubElement as subElement, tostring as ts

#read doc
import xml.etree.ElementTree as ET
import os,argparse,sys

class gen:
    missingContactExit=True
    docPath=''
    referencesPDF='references.pdf'
    resumePDF='resume.pdf'
    class stylesReferences:
        bullet='&#8226 '
        style=None
        styleIndent=None
        styleBold=None
        styleItalic=None
        
        titleCenter=None
        titleCenterBold=None
        titleCenterNormal=None
        titleCenterItalic=None
        
        def __init__(self):
            self.style = ParagraphStyle(
                    name='Normal',
                    fontName='Times-Roman',
                    fontSize=10,
                    leftIndent=14
                    )

            self.titleCenterNormal = ParagraphStyle(
                    name='Normal',
                    fontName='Times-Roman',
                    fontSize=10,
                    alignment=1,
                    )

            self.titleCenter=ParagraphStyle(
                    name='center',
                    fontName='Times-Roman',
                    fontSize=12,
                    alignment=1,
                    )

            self.titleCenterBold=ParagraphStyle(
                    name='center',
                    fontName='Times-Bold',
                    fontSize=12,
                    alignment=1,
                    )   

            self.styleIndent=ParagraphStyle(
                    name='indent',
                    fontName='Times-Roman',
                    fontSize=10,
                    leftIndent=28,
                    )

            self.styleBold=ParagraphStyle(
                    name='bold',
                    fontName='Times-Bold',
                    fontSize=11,
                    leftIndent=14
                    )

            self.styleBold_m1=ParagraphStyle(
                    name='bold',
                    fontName='Times-Bold',
                    fontSize=10,
                    )

            self.styleItalic=ParagraphStyle(
                    name='italic',
                    fontName='Times-Italic',
                    fontSize=11,
                    leftIndent=14,
                    )

            self.titleCenterItalic=ParagraphStyle(
                    name='italic',
                    fontName='Times-Italic',
                    fontSize=11,
                    alignment=1,
                    )
            self.styleControl=ParagraphStyle(
                    name='control',
                    fontName='Times-Roman',
                    fontSize=10,
                    )

    class stylesResume:
        styleNormal=None
        def __init__(self):
            self.styleNormal=ParagraphStyle(
                    name='normal',
                    fontName='Times-Roman',
                    fontSize=10,
                    )
    def mkTitle(self,resume,style):
        if resume.contact == None:
            return []
        parts=[]
        keys=['email','name','street','locale','phone']
        fail=0
        contacts=0
        for i in resume.contact.keys():
            if i not in keys:
                keys.append(i)
        for i in keys:
            print('Resume [{}]: {}'.format(i,resume.contact[i]))            
            if i == 'name':
                if resume.contact[i] == ' ':
                    fail+=1
                backup=style.titleCenterBold.fontSize
                style.titleCenterBold.fontSize=16
                parts.append(Paragraph(resume.contact[i],style.titleCenterBold))
                parts.append(Spacer(1,0.1*inch))
                style.titleCenterBold.fontSize=backup
                del(backup)
            elif i in ['phone','email']:
                if resume.contact[i] == ' ':
                    contacts+=1
                if contacts > 1:
                    fail+=1
                #if you have either a phone number or a email address, fail does not increment
                parts.append(Paragraph(resume.contact[i],style.titleCenterItalic))
            else:
                if resume.contact[i] == ' ':
                    fail+=1
                parts.append(Paragraph(resume.contact[i],style.titleCenter))
        if fail > 1:
            if self.missingContactExit == False:
                parts=[]
            else:
                exit('bad resume! missing contact information!')
        else:
            parts.append(Spacer(1,0.1*inch))
            parts.append(HRFlowable(width=letter[0]-100))
        return parts

    def mkTitleReferences(self,contact,style):
        parts=[]
        keys=['email','name','street','locale','phone']
        fail=0
        contacts=0
        for i in contact.keys():
            if i not in keys:
                keys.append(i)
        for i in keys:
            if contact[i] == None:
                contact[i]=' '
            print('references [{}]: {}'.format(i,contact[i]))
            if i == 'name':
                backup=style.titleCenterBold.fontSize
                style.titleCenterBold.fontSize=16
                parts.append(Paragraph(contact[i],style.titleCenterBold))
                parts.append(Spacer(1,0.1*inch))
                style.titleCenterBold.fontSize=backup
                del(backup)
                if contact[i] == ' ':
                    fail+=1
            elif i in ['phone','email']:
                if contact[i] == ' ':
                    parts.append(Spacer(1,0.2*inch))
                    if contacts < 2:
                        contacts+=1
                    if contacts > 1:
                        fail+=1
                else:
                    parts.append(Paragraph(contact[i],style.titleCenterItalic))
            else:
                parts.append(Paragraph(contact[i],style.titleCenter))
                if contact[i] == ' ':
                    fail+=1
        parts.append(Spacer(1,0.1*inch))
        parts.append(HRFlowable(width=letter[0]-100))
        if fail > 0:
            parts=[]
        return parts

    def mkHeader(self,head,style):
        parts=[]
        tmp=style.styleBold
        tmp.underlineProportion=0.01
        tmp.fontSize+=2
        parts.append(Spacer(1,0.05*inch))
        parts.append(Paragraph('{}'.format(head),tmp))
        parts.append(Spacer(1,0.05*inch))
        parts.append(HRFlowable(width=letter[0]-100))
        parts.append(Spacer(1,0.05*inch))
        tmp.fontSize-=2
        return parts

    def mkWorkXp(self,resume,style):
        if resume.employers == None:
            return []
        parts=[]
        parts.extend(self.mkHeader('Work Experience',style))
        badEntry=[]
        for employer in resume.employers.keys():
            partExt=[]
            fail=0
            for info in resume.employers[employer].keys():
                if 'title' in info:
                    for title in resume.employers[employer][info]:
                        partExt.append(Paragraph(title,style.styleBold))
                        if title == ' ':
                            fail+=1
                if info == 'employer_region':
                    for empR in resume.employers[employer][info]:
                        partExt.append(Paragraph(empR,style.styleItalic))
                        if empR == ' ':
                            fail+=1
                if info == 'start2end':
                    for start2end in resume.employers[employer][info]:
                        partExt.append(Paragraph(start2end,style.style))
                        if start2end == ' ':
                            fail+=1
                if info == 'duties':
                    for duty in resume.employers[employer][info]:
                        partExt.append(Paragraph('{1} {0}'.format(duty,style.bullet),style.styleIndent))
                        if duty == ' ':
                            fail+=1
            if fail < 1:
                parts.extend(partExt)
            else:
                badEntry.append(True)
                
                
            parts.append(Spacer(1,0.1*inch))
        if len(badEntry) >= len(resume.employers.keys()):
            parts=[]
        return parts
            

    def mkEdu(self,resume,style):
        if resume.schools == None:
            return []
        parts=[]
        parts.extend(self.mkHeader('Education',style))
        order=['school_region','degree','start2end']
        fail=0
        for edu in resume.schools.keys():
            for info in order:
                if info == 'school_region':
                    parts.append(Paragraph(resume.schools[edu][info],style.styleBold))
                    if resume.schools[edu][info] == ' ':
                        fail+=1
                if info == 'degree':
                    parts.append(Paragraph(resume.schools[edu][info],style.styleItalic))
                    if resume.schools[edu][info] == ' ':
                        fail+=1
                if info == 'start2end':
                    parts.append(Paragraph(resume.schools[edu][info],style.style))
                    if resume.schools[edu][info] == ' ':
                        fail+=1
            parts.append(Spacer(1,0.1*inch))
        if fail > 0:
            parts=[]
        return parts

    def mkSkills(self,resume,style):
        if resume.skills == None:
            return []
        parts=[]
        parts.extend(self.mkHeader('Skills',style))
        fail=0
        for skill in resume.skills.keys():
            if skill != 'tag':
                if resume.skills[skill] != ' ':
                    parts.append(Paragraph('{} {}'.format(style.bullet,resume.skills[skill]),style.style))
                else:
                    fail+=1
        if fail > 0:
            parts=[]
        return parts

    def mkLinks(self,resume,style):
        if resume.links == None:
            return []
        parts=[]
        parts.extend(self.mkHeader('Links',style))
        fail=0
        for link in resume.links.keys():
            if link != 'tag':
                parts.append(Paragraph('{} {}'.format(style.bullet,resume.links[link]),style.style))
                if resume.links[link] == ' ':
                    fail=+1
        if fail > 0:
            parts=[]
        return parts

    def mkCerts(self,resume,style):
        if resume.certs == None:
            return []
        parts=[]
        parts.extend(self.mkHeader('Certifications and Licenses',style))
        fail=0
        order=['name','start2end']
        for cert in resume.certs.keys():
            if cert != 'tag':
                for info in order:
                    if info == 'name':
                        parts.append(Paragraph(resume.certs[cert][info],style.styleBold))
                        if resume.certs[cert][info] == ' ':
                            fail+=1
                    if info == 'start2end':
                        parts.append(Paragraph(resume.certs[cert][info],style.styleItalic))
                        if resume.certs[cert][info] == ' ':
                            fail+=1
                parts.append(Spacer(1,0.1*inch))
        if fail > 0:
            parts=[]
        return parts

    def mkAddInfo(self,resume,style):
        if resume.addInfo == None:
            return []
        parts=[]
        parts.extend(self.mkHeader('Additional Information and Personal Skills',style))
        success=0
        for key in resume.addInfo.keys():
            if key != 'tag':
                for bullet in resume.addInfo[key]:
                    parts.append(Paragraph('{} {}'.format(style.bullet,bullet),style.style))
                    success+=1
                parts.append(Spacer(1,0.1*inch))
        if success < 1:
            parts=[]
        return parts
    
    def pageNum(self,canvas,doc):
        pageNum=canvas.getPageNumber()
        text="Page {}".format(pageNum)
        canvas.setFont('Times-Roman',10)
        canvas.drawString(letter[0]-50,letter[1]-(letter[1]-20),text)

    def genResume(self,resume):
        style=self.stylesReferences()
        doc = SimpleDocTemplate(os.path.join(self.docPath,self.resumePDF),pagesize=letter,leftMargin=50,rightMargin=10,topMargin=36,bottomMargin=46)
        parts=[]
        tmp=self.mkTitle(resume,style)
        if self.missingContactExit == True:
            if tmp == []:
                return 'bad contact info'
        parts.extend(tmp)
        parts.extend(self.mkWorkXp(resume,style))
        parts.extend(self.mkEdu(resume,style))
        parts.extend(self.mkSkills(resume,style))
        parts.extend(self.mkLinks(resume,style))
        parts.extend(self.mkCerts(resume,style))
        parts.extend(self.mkAddInfo(resume,style))
        if parts == []:
            parts.append(Paragraph('Some kind of Error was created and a resume could not be generated!',style.style))
        doc.build(parts,onFirstPage=self.pageNum,onLaterPages=self.pageNum)

    def genReferencesDoc(self,ref,contacts):    
        style=self.stylesReferences()
        doc = SimpleDocTemplate(os.path.join(self.docPath,self.referencesPDF), pagesize=letter,leftMargin=50,rightMargin=10,topMargin=36,bottomMargin=46)

        parts = []
        
        orders=[
                ['name',style.styleBold],
                ['title',style.styleItalic],
                ['employer',style.style],
                ['street',style.style],
                ['locale',style.style],
                ['email',style.style],
                ['phone',style.style]
                ]
        tmp=self.mkTitleReferences(contacts,style)
        if self.missingContactExit == True:
            if tmp == []:
                return 'bad contact information'
        parts.extend(tmp)
        counter=0
        contactsFail=0
        for i in ref:
            entryFailed=False
            partsExt=[]
            if counter >= 8:
                partsExt.append(Spacer(1,0.2*inch))
                counter=0
            partsExt.append(Spacer(1,0.05*inch))
            for tag in orders:
                if tag in ['phone','email']:
                    if i[tag[0]] != None: 
                        partsExt.append(Paragraph(i[tag[0]],tag[1]))
                    else:
                        contactsFail+=1
                    if contactsFail > 1:
                        entryFailed=True
                        break
                else:
                    if tag == 'name':
                        if i[tag[0]] == None:
                            entryFailed=True
                            break
                        else:
                            partsExt.append(Paragraph(i[tag[0]],tag[1]))
                    else:
                        partsExt.append(Paragraph(i[tag[0]],tag[1]))

            if entryFailed == False:
                parts.extend(partsExt)

            counter+=1
        if parts == []:
            parts.append(Paragraph('Errors were created! No references document was created! This message is a sign of that.',style.style))
        doc.build(parts,onFirstPage=self.pageNum,onLaterPages=self.pageNum)

class readXmlDoc:
    master=None
    references=[]
    reference={}
    local='831'
    country='1'
    referencesXml='references.xml'
    resumeXml='resume.xml'
    class resume:
        addInfo=None
        certs=None
        links=None
        skills=None
        schools=None
        employers=None
        relocation=None
        work_auth=None
        contact=None
        def __init__(self):
            pass

    def reformatPhoneNumber(self,num):
        if num != None:
            num=''.join([i for i in num if i.isdigit()])
            if len(num) == 10:
                num='+{}-({}) {}-{}'.format(self.country,num[:3],num[3:6],num[6:10])
            elif len(num) == 7:
                num='+{}-({}) {}-{}'.format(self.country,self.local,num[:3],num[3:7])
            elif len(num) == 11:
                num='+{}-({}) {}-{}'.format(num[:1],num[1:4],num[4:7],num[7:11])
            else:
                num=num
                print('Bad Phone Number!')
        else:
            num=' '
        return num


    def wordCap(self,sentence):
        if sentence == None:
            return ' '
        return ' '.join([i[:1].upper()+i[1:] for i in sentence.split(' ')])

    def getResume(self):
        res=self.resume()
        tree=ET.parse(self.resumeXml)
        root=tree.getroot()
        for child in root:
            if child.tag == 'contact':
                contact={}
                for contactInfo in child:
                    if contactInfo.text == None:
                        contactInfo.text=' '
                    if contactInfo.tag == 'phone':
                        if contactInfo.text != ' ':
                            contactInfo.text=self.reformatPhoneNumber(contactInfo.text)
                    contact[contactInfo.tag]=contactInfo.text
                res.contact=contact
            if child.tag == 'relocation':
                res.relocation=child.text
            if child.tag == 'work_auth':
                res.work_auth=child.text
            if child.tag == 'work_xp':
                employers={}
                for subchild in child:
                    employers[subchild.attrib['name']]={}
                    for subchild1 in subchild:
                        if subchild1.attrib == {}:
                            if subchild1.text != None:
                                employers[subchild.attrib['name']][subchild1.tag]=[i for i in subchild1.text.replace('\t','').replace('\xa0',' ').split('\n') if i != '']
                            else:
                                employers[subchild.attrib['name']][subchild1.tag]=' '
                        else:
                            if subchild1.text != None: 
                                employers[subchild.attrib['name']]['{}_{}'.format(subchild1.tag,subchild1.attrib['num'])]=[ i for i in subchild1.text.replace('\t','').replace('\xa0',' ').split('\n') if i != '']
                            else:
                                employers[subchild.attrib['name']]['{}_{}'.format(subchild1.tag,subchild1.attrib['num'])]=' '
                res.employers=employers
            if child.tag == 'education':
                schools={}
                for school in child:
                    schools['{}_{}'.format(school.attrib['num'],school.attrib['type'])]={}
                    for schoolInfo in school:
                        if schoolInfo.text == None:
                            schoolInfo.text=' '
                        schools['{}_{}'.format(school.attrib['num'],school.attrib['type'])][schoolInfo.tag]=schoolInfo.text
                res.schools=schools
            if child.tag == 'skills':
                skills={}
                skills['tag']=child.tag
                for skill in child:
                    if skill.text == None:
                        skill.text=' '
                    skills[skill.attrib['num']]=skill.text
                res.skills=skills
            if child.tag == 'links':
                links={}
                links['tag']=child.tag
                for link in child:
                    if link.text == None:
                        link.text=' '
                    links[link.attrib['num']]=link.text
                res.links=links
            if child.tag == 'certs':
                certs={}
                certs['tag']=child.tag
                for cert in child:
                    certs[cert.attrib['num']]={}
                    for certInfo in cert:
                        if certInfo.text == None:
                            certInfo.text=' '
                        certs[cert.attrib['num']][certInfo.tag]=certInfo.text
                res.certs=certs
            if child.tag == 'additional_info':
                addInfo={}
                addInfo['tag']=child.attrib['tag']
                addInfo[child.tag]=[i.replace('\t','').replace('\xa0',' ') for i in child.text.split('\n') if i != '']
                res.addInfo=addInfo
        return res
    
    def getContacts(self,root):
        for child in root:
            if child.tag == 'contact':
                contact={}
                for contactInfo in child:
                    if contactInfo.tag == 'phone':
                        contactInfo.text=self.reformatPhoneNumber(contactInfo.text)
                    contact[contactInfo.tag]=contactInfo.text
                return contact


    def readReferences(self):
        tree=ET.parse(self.referencesXml)
        root=tree.getroot()
        ref=self.getReferences(root)
        contacts=self.getContacts(root)
        return ref,contacts
    
    def getReferences(self,root):
        references=[]
        for child in root:
            if child.tag == 'employer':
                reference={}
                counter=0
                reference['employer']=self.wordCap(child.attrib['name'])
                for subChild in child:
                    fail=0
                    if subChild.tag == 'street_address':
                        reference['street']=self.wordCap(subChild.text)
                        if subChild.text == None:
                            reference['street']=' '
                    elif subChild.tag in ['zip','state','city']:
                        if counter < 3:
                            reference[subChild.tag]=subChild.text
                            if subChild.text == None:
                                reference[subChild.tag]=' '
                            counter+=1
                        if counter == 3:
                            reference['locale']='%s, %s %s' % tuple((
                                    reference['city'],
                                    reference['state'],
                                    reference['zip']
                                    ))
                            reference['locale']=self.wordCap(reference['locale'])
                            for tag in ['city','state','zip']:
                                reference.pop(tag)
                    elif subChild.tag == 'phone':
                        if subChild.text == None:
                            subChild.text=' '
                        else:
                            subby={}
                            subby['phone']=self.reformatPhoneNumber(subChild.text)
                            if subChild.attrib['email'] != None:
                                subby['email']=subChild.attrib['email']
                            else:
                                subby['email']=None
                            subby['name']=self.wordCap(subChild.attrib['owner'])
                            subby['title']=self.wordCap(subChild.attrib['title'])
                            subby['locale']=reference['locale']
                            subby['employer']=reference['employer']
                            subby['street']=reference['street']
                            references.append(subby)
                    if fail > 0:
                        exit('no references sheet could be generated. Bad XML Document')
        return references

class checks:
    references='templates/reference/references.xml'
    resume='templates/resume/resume.xml'
    docPath='documents'
    missingContactExit=True
    def init(self):
        self.xml=readXmlDoc()
        self.build=gen()
        if os.path.exists(self.docPath):
            self.build.docPath=self.docPath
        self.build.missingContactExit=self.missingContactExit
        if os.path.exists(self.references):
            self.xml.referencesXml=self.references
            references,contact=self.xml.readReferences()
            res=self.build.genReferencesDoc(references,contact)
            if res != None:
                print('References [Error]: {}'.format(res))
        if os.path.exists(self.resume):
            self.xml.resumeXml=self.resume
            resume=self.xml.getResume()
            res=self.build.genResume(resume)
            if res != None:
                print('Resume [Error]: {}'.format(res))
    #perform checks to selectively read files that exist

if __name__ == '__main__':
    app=checks()
    app.init()
'''
xml=readXmlDoc()
'''
#xml.resumeXml='resume-blank-missing-field.xml'
#xml.resumeXml='resume-missing-field.xml'
#need a way to detect where a section is on the page, and ensure it does not jump pages
#xml.resumeXml='templates/resume/resume.xml'
#xml.referencesXml='templates/reference/references.xml'
'''
xml.referencesXml='./references.xml'
build=gen()
'''
#force resume generation even if contact info is missing
#build.missingContactExit=False

#check if exists first
#resume=xml.getResume()
#build.genResume(resume)

#check if exists first
'''
references,contact=xml.readReferences()
build.genReferencesDoc(references,contact)
'''
#fix phone number
#resume.contact['phone']=a.reformatPhoneNumber(resume.contact['phone'])
#build.genResume(resume)

#code to generate a references sheet from xml
#'''
#ref,contacts=a.readReferences()
#'''
