#! /usr/bin/env python3
######################
# NoGuiLinux         #
# Generate Resume    #
# Document           #
######################
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

class styles:
    def __init__(self):
        self.head=self.header()
        self.objective=self.obj()
        self.document=self.doc()
        self.registerFonts()

    def registerFonts(self):
        fonts=[
            ('ArialI','ariali.ttf'),
            ('ArialBI','arialbi.ttf'),
            ('ArialB','arialbd.ttf'),
            ('Arial','arial.ttf'),
            ('GeorgiaB','georgiab.ttf'),
            ('GeorgiaI','georgiai.ttf'),
            ('Georgia','georgia.ttf'),
            ('Times','times.ttf'),
            ('TimesI','timesi.ttf'),
            ('TimesB','timesbd.ttf'),
            ('TimesBI','timesbi.ttf'),
                ]
        for p1,p2 in fonts:
            pdfmetrics.registerFont(TTFont(p1,p2))

    class obj:
        def __init__(self):
            self.tasks()
        def tasks(self):
            self.mkObjective()

        def mkObjective(self):
            self.objective=ParagraphStyle(
                    'objective',
                    fontName='ArialI',
                    fontSize=12,
                    leading=12,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=0,
                    spaceAfter=0,
                    bulletFontName='ArialI',
                    bulletFontSize=12,
                    bulletIndent=0,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )

    class header:
        def __init__(self):
            self.tasks()

        def tasks(self):
            self.mkHeaderName()
            self.mkHeaderAddress()
            self.mkHeaderAddressPhone()
            self.mkHeaderAddressEmail()

        def mkHeaderName(self):
                self.headerName=ParagraphStyle(
                    'Name',
                    fontName='GeorgiaB',
                    fontSize=32,
                    leading=32,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=0,
                    spaceAfter=0,
                    bulletFontName='GeorgiaB',
                    bulletFontSize=32,
                    bulletIndent=0,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )
        def mkHeaderAddressEmail(self):
                self.headerAddressEmail=ParagraphStyle(
                    'email',
                    fontName='TimesI',
                    fontSize=14,
                    leading=14,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_RIGHT,
                    spaceBefore=0,
                    spaceAfter=0,
                    bulletFontName='TimesI',
                    bulletFontSize=14,
                    bulletIndent=0,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )
        def mkHeaderAddressPhone(self):
                self.headerAddressPhone=ParagraphStyle(
                    'phone',
                    fontName='TimesB',
                    fontSize=14,
                    leading=14,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_RIGHT,
                    spaceBefore=0,
                    spaceAfter=0,
                    bulletFontName='TimesB',
                    bulletFontSize=14,
                    bulletIndent=0,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )

        def mkHeaderAddress(self):
                self.headerAddress=ParagraphStyle(
                    'address',
                    fontName='Times',
                    fontSize=12,
                    leading=12,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_RIGHT,
                    spaceBefore=0,
                    spaceAfter=0,
                    bulletFontName='Times',
                    bulletFontSize=12,
                    bulletIndent=0,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )
    class doc:
        bullet='&#8226 '
        def __init__(self):
            self.tasks()

        def tasks(self):
            self.mkTextNormal()
            self.mkTextNormalDate()
            self.mkTextItalic()
            self.mkTextItalic10()
            self.mkTextBold()
            self.mkTextBoldfs15()
            self.mkHeader2()
            self.mkDefaultTableStyle()
            self.mkDefaultTableStyleLeft()
            self.mkDefaultTableStyleCenter()
            self.mkEmploymentTableStyle()

        def mkTextNormalDate(self):
            self.normalDate=ParagraphStyle(
                    'normalDate',
                    fontName='Arial',
                    fontSize=11,
                    leading=11,
                    leftIndent=10,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=2,
                    spaceAfter=2,
                    bulletFontName='Arial',
                    bulletFontSize=11,
                    bulletIndent=0,
                    tracking=1,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )

        def mkTextNormal(self):
            self.normal=ParagraphStyle(
                    'normal',
                    fontName='Times',
                    fontSize=12,
                    leading=12,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=2,
                    spaceAfter=2,
                    bulletFontName='Times',
                    bulletFontSize=12,
                    bulletIndent=10,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )
        def mkTextBold(self):
            self.bold=ParagraphStyle(
                    'bold',
                    fontName='TimesB',
                    fontSize=12,
                    leading=12,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=2,
                    spaceAfter=2,
                    bulletFontName='TimesB',
                    bulletFontSize=12,
                    bulletIndent=0,
                    tracking=1,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )
        def mkTextBoldfs15(self):
            self.boldfs15=ParagraphStyle(
                    'bold',
                    fontName='TimesB',
                    fontSize=15,
                    leading=15,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=2,
                    spaceAfter=2,
                    bulletFontName='TimesB',
                    bulletFontSize=15,
                    bulletIndent=0,
                    tracking=1,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )

        def mkTextItalic(self):
            self.italic=ParagraphStyle(
                    'italic',
                    fontName='TimesI',
                    fontSize=12,
                    leading=13,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=0,
                    spaceAfter=0,
                    bulletFontName='TimesI',
                    bulletFontSize=12,
                    bulletIndent=0,
                    tracking=1,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )
        def mkTextItalic10(self):
            self.italic10=ParagraphStyle(
                    'italic10',
                    fontName='TimesI',
                    fontSize=12,
                    leading=12,
                    leftIndent=10,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=2,
                    spaceAfter=2,
                    bulletFontName='TimesI',
                    bulletFontSize=12,
                    bulletIndent=0,
                    tracking=1,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )

        def mkDefaultTableStyle(self):
            self.defaultTable=TableStyle([('ALIGN',(0,0),(-1,-1),'RIGHT'),
                                    ('VALIGN',(0,0),(-1,-1),'TOP'),

                           ])
        def mkDefaultTableStyleCenter(self):
            self.defaultTableCenter=TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                                    ('VALIGN',(0,0),(-1,-1),'TOP'),

                           ])
        def mkDefaultTableStyleLeft(self):
            self.defaultTableLeft=TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),
                                    ('VALIGN',(0,0),(-1,-1),'TOP'),

                           ])
        def mkEmploymentTableStyle(self):
            self.employmentTable=TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),
                                    ('VALIGN',(0,0),(-1,-1),'TOP'),
                                    ('LINEBELOW',(-2,-1),(-1,-1),0.5,gray),
                                    ('BOTTOMPADDING',(0,0),(-1,-1),6),
                                    ('LINEBEFORE',(0,1),(-2,-1),0.5,gray),
                           ])


        def mkHeader2(self):
            self.header2=ParagraphStyle(
                    'header2',
                    fontName='TimesB',
                    fontSize=20,
                    leading=20,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=0,
                    spaceAfter=0,
                    bulletFontName='TimesB',
                    bulletFontSize=14,
                    bulletIndent=0,
                    tracking=1,
                    textColor=black,
                    backColor=None,
                    wordWrap=None,
                    borderWidth= 0,
                    borderPadding= 0,
                    borderColor= None,
                    borderRadius= None,
                    allowWidows= 1,
                    allowOrphans= 0,
                    textTransform=None,
                    endDots=None,
                    splitLongWords=1,
            )
class resumeGen:
    failedStates=[None,{},[]]
    resumePDF='./resume.pdf'
    resumeXML='./default-resume.xml'
    autostart=False
    def mkResume(self):
        self.styling=styles()
        self.xml=import_xml.get_xml()
        self.xml.resumeXml=self.resumeXML
        self.docX=self.xml.returnXml(self.xml.resumeXml) 
        if self.docX != None:
            self.data=self.xml.resumeGetAllFields(self.docX)
            return True
        else:
            return None
            #print(self.data)

    def doc_init(self,title):
        doc=SimpleDocTemplate(title,pagesize=letter,
                rightMargin=25,
                leftMargin=25,
                topMargin=25,
                bottomMargin=25)
        doc.title=os.path.basename(title)
        return doc,[]
        
    def header(self,data='self'):
        if data == 'self':
            data=self.data['contact']
        else:
            data=data

        if data in self.failedStates:
            return None
        self.status('header',data)
        name='{0} {1} {2}'.format(data['fname'],data['mname'],data['lname']) 
        
        nameFM='{} {}'.format(data['fname'],data['mname'])
        nameL='{}'.format(data['lname'])
        
        phoneString='+{} ({}) {}-{}'.format(data['phone_international'],data['phone_region'],data['phone_local'][:3],data['phone_local'][3:])
        localeString='{} {} {}'.format(data['city'],data['state'],data['zip'])
        
        tbl1=[[Paragraph(nameFM,self.styling.head.headerName)],[Paragraph(nameL,self.styling.head.headerName)]]
        tbl2=[
                [Paragraph(phoneString,self.styling.head.headerAddressPhone)],
                [Paragraph(data['email'],self.styling.head.headerAddressEmail)],
                [Paragraph(data['street'],self.styling.head.headerAddress)],
                [Paragraph(localeString,self.styling.head.headerAddress)]
                ]
        tbl1=Table(tbl1)
        tbl1.setStyle(self.styling.document.defaultTableLeft)
        
        tbl2=Table(tbl2)
        tbl2.setStyle(self.styling.document.defaultTable)

        tbls=[[tbl1,tbl2]]
        tbls=Table(tbls,colWidths=(0.1*inch)*39)
        return [tbls,flowables.HRFlowable(width=letter[0]-75)]
        #self.story.append(tbls)
        #self.story.append(flowables.HRFlowable(width=letter[0]-75))
        
    def spacer(self):
        self.story.append(flowables.Spacer(1,0.075*inch))
        #self.story.append(flowables.HRFlowable(width=letter[0]))
        self.story.append(flowables.Spacer(1,0.05*inch))

    def objective(self):
        data=self.data['objective']
        if data in self.failedStates:
            return None
        objectives=[]
        for key in data.keys():
            objectives.append(Paragraph(data[key],self.styling.objective.objective))
        tbl=Table([objectives])
        tbl.setStyle(self.styling.document.defaultTableCenter)
        return [tbl]
        self.status('objective',data)

    def skills(self):
        data=self.data['skills']
        if data in self.failedStates:
            return None
        skills=[]
        tbls=[[Paragraph('Skills',self.styling.document.header2)],[flowables.HRFlowable(width=letter[0]-75)],]
        for key in data.keys():
            years=data[key]['years']
            months=data[key]['months']
            grade=data[key]['grade']
            skill=data[key]['skill']
            dateString=''
            if years != '':
                dateString+='{} Years'.format(years)
                if months != '':
                    dateString+=', '
            if months != '':
                dateString+='{} Months'.format(months)
            if grade != '':
                dateString='{}'.format(grade)+dateString
            skillString='{} ({})'.format(skill,dateString)
            skills.append(Paragraph(skillString,self.styling.document.normal))

        chunks=2
        uls=[skills[i:i+chunks] for i in range(0,len(skills),chunks)]
        ul1=[]
        ul2=[]
        self.status('uls',uls)
        self.status('uls[0]',uls[0])
        if len(uls[-1]) < 2:
            uls[-1].append(None)
    
        for col1,col2 in uls:
            if col1 != None:
                ul1.append(col1)
            if col2 != None:
                ul2.append(col2)
        
        ul1=ListFlowable(ul1,bulletType='bullet',leftIndent=10)
        ul2=ListFlowable(ul2,bulletType='bullet',leftIndent=10)

        tbl_data=[[ul1,ul2]]
        tbl=Table(tbl_data,colWidths=(0.1*inch)*36)
        tbl.setStyle(self.styling.document.defaultTableCenter)
        tbls.append([tbl])
        tbls=Table(tbls)
        tbls=flowables.KeepTogether(tbls)
        return [tbls]
        #self.story.append(Paragraph(skillString,self.styling.document.normal))
        self.status('skills',data)

    def workHistory(self):
        #self.spacer()
        data=self.data['employment']
        if data in self.failedStates:
            return None
        self.status('Work History',data)
        #self.story.append(Paragraph('Work History',self.styling.document.header2))
        #self.story.append(Spacer(1,0.1*inch))      
        tbls=[[Paragraph('Work History',self.styling.document.header2)],[flowables.HRFlowable(width=letter[0]-75)],]
        for key in data.keys():
            duties=[]
            date='{} - {}'.format(data[key]['startDate'],data[key]['endDate'])
            locale='{}, {} {}'.format(data[key]['city'],data[key]['state'],data[key]['zip'])
            companyString='{} - {}'.format(data[key]['employer'],locale)

            tbl_data=[
                    [Paragraph(data[key]['title'],self.styling.document.boldfs15)],
                    [Paragraph(companyString,self.styling.document.italic)],
                    [Paragraph(date,self.styling.document.normal)]
                        ]
            
            for d in [i for i in data[key]['duties'].split('\n') if i != '']:
                duties.append(Paragraph(d,self.styling.document.normal))
           
            chunk=2
            cols=[duties[i:i+chunk] for i in range(0,len(duties),chunk)]
            col1=[]
            col2=[]
            for col in cols:
                if len(col) > 1:
                    col1.append(col[0])
                    col2.append(col[1])
                else:
                    col1.append(col[0])
            if col1 not in self.failedStates:
                col1=ListFlowable(col1,bulletType='bullet',leftIndent=10)
            if col2 not in self.failedStates:
                col2=ListFlowable(col2,bulletType='bullet',leftIndent=10)

            tbl_data.append([col1,col2])
            tbl=Table(tbl_data,colWidths=(0.1*inch)*36)

            self.status('len of table',len(tbl_data))
            
            tbl.setStyle(self.styling.document.employmentTable)
            #tbl=flowables.KeepTogether(tbl)
            tbls.append([tbl])
        tbls=Table(tbls)
        return [tbls]

    def education(self):
        data=self.data['education']
        if data in self.failedStates:
            return None
        self.status('Education',data)
        tbls=[[Paragraph('Education',self.styling.document.header2)],[flowables.HRFlowable(width=letter[0]-75)],]
        for key in data.keys():
            date='{} - {}'.format(data[key]['startDate'],data[key]['endDate'])
            locale='{}, {} {}'.format(data[key]['city'],data[key]['state'],data[key]['zip'])
            schoolString='{} - {}'.format(data[key]['school'],locale)
            tbl_data=[
                    [Paragraph(schoolString,self.styling.document.bold)],
                    [Paragraph(data[key]['degree'],self.styling.document.italic)],
                    [Paragraph(date,self.styling.document.normal)],
                    ]
            tbl=Table(tbl_data)
            tbl.setStyle(self.styling.document.defaultTable)
            tbls.append([tbl])
        tbls=Table(tbls)
        tbls=flowables.KeepTogether(tbls)
        return [tbls]

    def certs(self):
        data=self.data['certifications']
        if data in self.failedStates:
            return None
        self.status('Certs',data)
        tbls=[[Paragraph('Certifications and Licenses',self.styling.document.header2)],[flowables.HRFlowable(width=letter[0]-75)],]
        for key in data.keys():
            date='{} - {}'.format(data[key]['startDate'],data[key]['endDate'])
            tbl_data=[
                        [Paragraph(data[key]['name'],self.styling.document.bold),Paragraph(date,self.styling.document.normal)],
                        ]
            tbl=Table(tbl_data,colWidths=[(0.1*inch)*34,None])
            tbl.setStyle(self.styling.document.defaultTable)
            tbls.append([tbl])
        tbls=Table(tbls)
        tbls=flowables.KeepTogether(tbls)
        return [tbls]

    def awards(self,skey,name):
        data=self.data[skey]
        if data in self.failedStates:
            return None
        tbls=[[Paragraph(name,self.styling.document.header2)],[flowables.HRFlowable(width=letter[0]-75)],]
        if data not in self.failedStates:
            self.spacer()
            self.status(skey,data)
            awards=[]
            for key in data.keys():
                for line in data[key].split('\n'):
                    awards.append(Paragraph(line,self.styling.document.normal))
            chunk=2
            cols=[awards[i:i+chunk] for i in range(0,len(awards),chunk)]
            col1=[]
            col2=[]
            for col in cols:
                if len(col) > 1:
                    col1.append(col[0])
                    col2.append(col[1])
                else:
                    col1.append(col[0])
            if col1 not in self.failedStates:
                col1=ListFlowable(col1,bulletType='bullet',leftIndent=10)
            if col2 not in self.failedStates:
                col2=ListFlowable(col2,bulletType='bullet',leftIndent=10)

            tbl=Table([[col1,col2]],colWidths=(0.1*inch)*36)
            tbl.setStyle(self.styling.document.defaultTableCenter)
            tbls.append([tbl])
        tbls=Table(tbls)
        tbls=flowables.KeepTogether(tbls)
        return [tbls]
        self.status(skey,data)
    
    def additional_info_other(self):
        data={}
        for key in self.data.keys():
            if key.startswith('additional_info'):
                key_sub=key.replace('additional_info','')
                if key_sub not in ['','_activities','_hobbies','_awards']:
                    if key not in data.keys():
                        data[key]=self.data[key]
        if data in self.failedStates:
            return None
        for key in data.keys():
            self.status('additional info other: {}'.format(key),data[key])
            tbls=[[Paragraph(key.replace('additional_info_',''),self.styling.document.header2)],[flowables.HRFlowable(width=letter[0]-75)],]
            items=[]
            for skey in data[key].keys():
                items.append(Paragraph(data[key][skey],self.styling.document.normal))

            chunk=2
            cols=[items[i:i+chunk] for i in range(0,len(items),chunk)]
            col1=[]
            col2=[]
            for col in cols:
                if len(col) > 1:
                    col1.append(col[0])
                    col2.append(col[1])
                else:
                    col1.append(col[0])

            if col1 not in self.failedStates:
                col1=ListFlowable(col1,bulletType='bullet',leftIndent=10)
            if col2 not in self.failedStates:
                col2=ListFlowable(col2,bulletType='bullet',leftIndent=10)

            tbl=Table([[col1,col2],],colWidths=(0.1*inch)*36)
            tbl.setStyle(self.styling.document.defaultTableCenter)
            tbls.append([tbl])
             
            tbls=Table(tbls)
            tbls=flowables.KeepTogether(tbls)
            return [tbls]


    def links(self):
        data=self.data['links']
        if data in self.failedStates:
            return None
        self.status('links',data)
        tbls=[
                [Paragraph('Links',self.styling.document.header2)],
                [flowables.HRFlowable(width=letter[0]-75)],
            ]
        links=[]
        for key in data.keys():
            links.append(Paragraph(data[key]['link'],self.styling.document.normal))
        links=ListFlowable(links,bulletType='bullet',leftIndent=10)
        tbl_data=[[links],]
        tbl=Table(tbl_data)
        tbl.setStyle(self.styling.document.defaultTable)
        tbls.append([tbl])
        tbls=Table(tbls)
        tbls=flowables.KeepTogether(tbls)
        return [tbls]

    def status(self,msg,data):
        print('\033[1;31;40m{}\033[1;40;m'.format(msg),data)

    def pageNum(self,canvas,doc):
        pageNum=canvas.getPageNumber()
        text="Page {}".format(pageNum)
        canvas.setFont('Times-Roman',10)
        canvas.drawString(letter[0]-50,letter[1]-(letter[1]-20),text)

    def build(self):
        self.docP.build(self.story,onFirstPage=self.pageNum,onLaterPages=self.pageNum)
    
    def tasks(self):
        state=self.mkResume()
        content=[]
        if state == True:
            comp=self.doc_init(self.resumePDF)
            self.story=comp[1]
            self.docP=comp[0]
            calls=[self.header,self.objective,self.skills,self.certs,self.workHistory,self.education]
            for call in calls:
                res=call()
                if res != None:
                    content.extend(res)
            '''
            content.extend(self.header())
            content.extend(self.objective())
            content.extend(self.skills())
            content.extend(self.certs())
            content.extend(self.workHistory())
            content.extend(self.education())
            '''
            for i,n in [
                    ['additional_info_awards','Awards'],
                    ['additional_info_hobbies','Hobbies'],
                    ['additional_info_activities','Activities'],
                    ['additional_info','Additional Information']
                    ]:
                res=self.awards(i,n)
                if res != None:
                    content.extend(res)
            calls=[self.additional_info_other,self.links]
            for call in calls:
                res=call()
                if res != None:
                    content.extend(res)

            #content.extend(self.additional_info_other())
            #content.extend(self.links())
            
            for i in content:
                if i != None:
                    self.story.append(i)
            self.build()
        else:
            print('could not make document')

if __name__ == '__main__':
    res=resumeGen()
    res.resumePDF='default'
    res.resumeXML='default-resume.xml'
    res.tasks()
