from ...MainWindow.pdf_header import genHeader
from reportlab.platypus import SimpleDocTemplate,Paragraph,HRFlowable,Spacer
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_CENTER
class generator:
    def __init__(self,data:dict,contact:dict,path:str):
        self.doc=SimpleDocTemplate(path)
        self.path=path
        self.data=data
        self.contact=contact
        #print(data,contact,path)
        self.styles=getSampleStyleSheet()

        self.ulx=ParagraphStyle('N8',self.styles['Normal'],fontSize=8)
        self.flowables=[]
        self.flowables.extend(genHeader(contact).generate())
        self.handleEmployment()
        self.handleEducation()
        self.handleCertification()
        self.handleAdditionalInfo()
        self.handleLinks()
        print(self.path)

        self.doc.build(self.flowables)



    def handleEmployment(self):
        lEmployment=self.data.get("employment")
        if len(lEmployment) > 0:
            self.flowables.append(Paragraph("Employment",ParagraphStyle('HC2',self.styles['Heading2'],alignment=TA_CENTER)))
            self.flowables.append(HRFlowable(width='98%'))
        for e in lEmployment:
            print(e)
            employer_line="{title} ({employer})".format(
                **dict(
                    title=e.get("job_title"),
                    employer=e.get("employer")
                )
            )
            date_line="{start} - {end}"
            if e.get("present"):
                date_line=date_line.format(**dict(start=e.get("start_date"),end="Present"))
            else:
                date_line=date_line.format(**dict(start=e.get("start_date"),end=e.get("end_date")))
            locale_line="{city}, {state} {ZIP}".format(
                **dict(
                    city=e.get("city"),
                    state=e.get("state"),
                    ZIP=e.get("ZIP")
                    )
                )
            self.flowables.append(Paragraph(employer_line,self.styles['Heading3']))
            self.flowables.append(Paragraph(date_line,self.styles['Normal']))
            self.flowables.append(Paragraph(locale_line,self.styles['Italic']))

            listed=list()
            for line in e.get("duties").split("\n"):
                if line != "":      
                    #print(line)
                    l="{l}".format(**dict(l=line))
                    print(l)
                    self.flowables.append(Paragraph(l,self.ulx,bulletText=" - "))
            #self.flowables.append(ListFlowable(listed))

        if len(lEmployment) > 0:
            self.flowables.append(HRFlowable(width='98%'))

                    


    def handleEducation(self):
        pass

    def handleCertification(self):
        pass

    def handleLinks(self):
        pass

    def handleAdditionalInfo(self):
        pass

