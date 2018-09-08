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
                ]
        for p1,p2 in fonts:
            pdfmetrics.registerFont(TTFont(p1,p2))

        pdfmetrics.registerFont(TTFont('Times','times.ttf'))
        pdfmetrics.registerFont(TTFont('TimesI','timesi.ttf'))
        pdfmetrics.registerFont(TTFont('TimesB','timesbd.ttf'))
        pdfmetrics.registerFont(TTFont('TimesBI','timesbi.ttf'))
        
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
 
        def mkHeaderName(self):
                self.headerName=ParagraphStyle(
                    'Name',
                    fontName='TimesB',
                    fontSize=28,
                    leading=28,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=0,
                    spaceAfter=0,
                    bulletFontName='Times',
                    bulletFontSize=10,
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
                    fontName='Arial',
                    fontSize=12,
                    leading=12,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=0,
                    spaceAfter=0,
                    bulletFontName='Arial',
                    bulletFontSize=10,
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
    class doc:
        bullet='&#8226 '
        def __init__(self):
            self.tasks()

        def tasks(self):
            self.mkTextNormal()
            self.mkTextNormalDate()
            self.mkTextItalic()
            self.mkTextBold()
            self.mkHeader2()
            self.mkDefaultTableStyle()
            self.mkDefaultTableStyleCenter()

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
        def mkTextItalic(self):
            self.italic=ParagraphStyle(
                    'italic',
                    fontName='TimesI',
                    fontSize=12,
                    leading=12,
                    leftIndent=0,
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
    def __init__(self):
        self.styling=styles()
        self.xml=import_xml.get_xml()
        self.xml.resumeXml='./default-resume.xml'
        self.docX=self.xml.returnXml(self.xml.resumeXml) 
        if self.docX != None:
            self.data=self.xml.resumeGetAllFields(self.docX)
            #print(self.data)

    def doc_init(self):
        doc=SimpleDocTemplate(self.resumePDF,pagesize=letter,
                rightMargin=25,
                leftMargin=25,
                topMargin=25,
                bottomMargin=25)
        doc.title=self.resumePDF
        self.docP=doc
        self.story=[]
        
    def header(self):
        data=self.data['contact']
        self.status('header',data)
        name='{0} {1} {2}'.format(data['fname'],data['mname'],data['lname']) 
               
        self.story.append(Paragraph(name,self.styling.head.headerName))
        self.spacer()

        phoneString='+{} ({}) {}-{}'.format(data['phone_international'],data['phone_region'],data['phone_local'][:3],data['phone_local'][3:])
        addressString='{},'.format(data['street'])+' {} {} {}'.format(data['city'],data['state'],data['zip'])

        contactString='{} | {} | {}'.format(addressString,phoneString,data['email'])
        self.story.append(Paragraph(contactString,self.styling.head.headerAddress)) 
    
    def spacer(self):
        self.story.append(flowables.Spacer(1,0.075*inch))
        self.story.append(flowables.HRFlowable(width=letter[0]))
        self.story.append(flowables.Spacer(1,0.05*inch))

    def objective(self):
        self.spacer()
        data=self.data['objective']
        for key in data.keys():
            self.story.append(Paragraph(data[key],self.styling.objective.objective))
        self.status('objective',data)

    def skills(self):
        self.spacer()
        data=self.data['skills']
        self.story.append(Paragraph('Skills',self.styling.document.header2))
        self.story.append(Spacer(1,0.05*inch))
        skills=[]
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

        self.story.append(tbl)
        #self.story.append(Paragraph(skillString,self.styling.document.normal))
        self.status('skills',data)

    def workHistory(self):
        self.spacer()

        data=self.data['employment']
        self.status('Work History',data)
        self.story.append(Paragraph('Work History',self.styling.document.header2))
        self.story.append(Spacer(1,0.1*inch))       
        for key in data.keys():
            duties=[]
            date='{} - {}'.format(data[key]['startDate'],data[key]['endDate'])
            locale='{}, {} {}'.format(data[key]['city'],data[key]['state'],data[key]['zip'])
            companyString='{} - {}'.format(data[key]['employer'],locale)

            tbl_data=[
                    [Paragraph(date,self.styling.document.normalDate),Paragraph(companyString,self.styling.document.bold)],
                    [Paragraph('',self.styling.document.normal),Paragraph(data[key]['title'],self.styling.document.italic)]
                        ]
            
            for d in [i for i in data[key]['duties'].split('\n') if i != '']:
                duties.append(Paragraph(d,self.styling.document.normal))
                
            duties=ListFlowable(duties,bulletType='bullet',leftIndent=10) 
            tbl_data.append([Paragraph('',self.styling.document.normal),duties])
            
            tbl=Table(tbl_data,colWidths=[(0.1*inch)*34,None])
            self.status('len of table',len(tbl_data))
            tbl.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'RIGHT'),
                                    ('VALIGN',(0,0),(-1,-1),'TOP'),

                           ]))

            self.story.append(tbl)

    def education(self):
        data=self.data['education']
        self.spacer()
        self.status('Education',data)
        self.story.append(Paragraph('Education',self.styling.document.header2))
        self.story.append(Spacer(1,0.1*inch))
        for key in data.keys():
            date='{} - {}'.format(data[key]['startDate'],data[key]['endDate'])
            locale='{}, {} {}'.format(data[key]['city'],data[key]['state'],data[key]['zip'])
            schoolString='{} - {}'.format(data[key]['school'],locale)
            tbl_data=[
                    [Paragraph(date,self.styling.document.normalDate),Paragraph(schoolString,self.styling.document.bold)],
                    [Paragraph('',self.styling.document.normal),Paragraph(data[key]['degree'],self.styling.document.italic)],
                        ]
            tbl=Table(tbl_data,colWidths=[(0.1*inch)*34,None])
            tbl.setStyle(self.styling.document.defaultTable)
            self.story.append(tbl)

    def certs(self):
        data=self.data['certifications']
        self.spacer()
        self.status('Certs',data)
        self.story.append(Paragraph('Certifications and Licenses',self.styling.document.header2))
        self.story.append(Spacer(1,0.1*inch))
        for key in data.keys():
            date='{} - {}'.format(data[key]['startDate'],data[key]['endDate'])
            #locale='{}, {} {}'.format(data[key]['city'],data[key]['state'],data[key]['zip'])
            tbl_data=[
                    [Paragraph(date,self.styling.document.normalDate),Paragraph(data[key]['name'],self.styling.document.bold)],
                        ]
            tbl=Table(tbl_data,colWidths=[(0.1*inch)*34,None])
            tbl.setStyle(self.styling.document.defaultTable)
            self.story.append(tbl)

    def awards(self):
        data=self.data['additional_info_awards']
        print(data)
    
    def hobbies(self):
        data=self.data['additional_info_hobbies']

    def activities(self):
        data=self.data['additional_info_activities']

    def additional_info(self):
        data=self.data['additional_info']

    def additional_info_other(self):
        data={}
        for key in self.data.keys():
            if key.startswith('additional_info'):
                key_sub=key.replace('additional_info','')
                if key_sub not in ['','_activities','_hobbies','_awards']:
                    data[key]=self.data[key]
        for key in data.keys():
            self.status('additional info other: {}'.format(key),data[key])

    def links(self):
        data=self.data['links']


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
        self.doc_init()
        self.header()
        self.objective()
        self.skills()
        self.certs()
        self.workHistory()
        self.education()

        self.awards()
        self.hobbies()
        self.activities()
        self.additional_info()       
        self.additional_info_other()
        self.links()
        self.build()

if __name__ == '__main__':
    res=resumeGen()
    res.tasks()
