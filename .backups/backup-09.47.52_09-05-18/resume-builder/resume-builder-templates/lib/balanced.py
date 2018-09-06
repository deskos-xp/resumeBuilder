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
            self.mkHeaderEmail()
            self.mkHeaderPhone()
            self.mkHeaderAddress()

        def mkHeaderPhone(self):
            self.headerPhone=ParagraphStyle(
                    'phone',
                    fontName='TimesI',
                    fontSize=14,
                    leading=14,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=0,
                    spaceAfter=0,
                    bulletFontName='TimesI',
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

        def mkHeaderEmail(self):
            self.headerEmail=ParagraphStyle(
                    'email',
                    fontName='ArialBI',
                    fontSize=14,
                    leading=14,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=3,
                    spaceAfter=3,
                    bulletFontName='ArialBI',
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
                    fontName='Times',
                    fontSize=14,
                    leading=14,
                    leftIndent=0,
                    rightIndent=0,
                    firstLineIndent=0,
                    alignment=TA_LEFT,
                    spaceBefore=0,
                    spaceAfter=0,
                    bulletFontName='Times',
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
            self.mkHeader2()

        def mkTextNormal(self):
            self.normal=ParagraphStyle(
                    'normal',
                    fontName='Times',
                    fontSize=12,
                    leading=12,
                    leftIndent=15,
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

        def mkHeader2(self):
            self.header2=ParagraphStyle(
                    'header2',
                    fontName='TimesB',
                    fontSize=14,
                    leading=14,
                    leftIndent=5,
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
        print(data)
        name='{0} {1} {2}'.format(data['fname'],data['mname'],data['lname']) 
        #print(type(self.styling.headerName))
        
        self.story.append(Paragraph(name,self.styling.head.headerName))
        
        self.story.append(Paragraph(data['email'],self.styling.head.headerEmail))
        
        self.story.append(Paragraph('+{} ({}) {}-{} ({})'.format(data['phone_international'],data['phone_region'],data['phone_local'][:3],data['phone_local'][3:],data['phoneType']),self.styling.head.headerPhone))
        self.story.append(Paragraph('{}'.format(data['street']),self.styling.head.headerAddress))
        self.story.append(Paragraph('{}, {} {}'.format(data['city'],data['state'],data['zip']),self.styling.head.headerAddress))
        self.spacer()
    
    def spacer(self):
        self.story.append(flowables.Spacer(1,0.075*inch))
        self.story.append(flowables.HRFlowable(width=letter[0]))
        self.story.append(flowables.Spacer(1,0.05*inch))

    def objective(self):
        data=self.data['objective']
        for key in data.keys():
            self.story.append(Paragraph(data[key],self.styling.objective.objective))
        self.spacer()

    def skills(self):
        data=self.data['skills']
        self.story.append(Paragraph('Skills',self.styling.document.header2))
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
            skillString='{}{} ({})'.format(self.styling.document.bullet,skill,dateString)
            self.story.append(Paragraph(skillString,self.styling.document.normal))
        print(data)

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

        self.build()

if __name__ == '__main__':
    res=resumeGen()
    res.tasks()
