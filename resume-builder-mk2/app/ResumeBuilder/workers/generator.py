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
        self.hc2=ParagraphStyle('HC2',self.styles['Heading2'],alignment=TA_CENTER)
        self.hr=HRFlowable(width='98%')
        self.flowables=[]
        self.flowables.extend(genHeader(contact).generate())
        self.handleEmployment()
        self.handleEducation()
        self.handleCertification()
        self.handleSkills()
        self.handleAdditionalInfo()
        self.handleLinks()
        print(self.path)

        self.doc.build(self.flowables)


    def handleSkills(self):
        lSkill=self.data.get("skills")
        if len(lSkill) > 0:
            self.flowables.append(Paragraph("Skills",self.hc2))
            self.flowables.append(self.hr)
        for s in lSkill:
            self.flowables.append(Paragraph(s.get("name"),self.styles.get('Heading3')))
            if s.get("years_experience") and s.get("months_experience"):
                
                line="{years} Year(s) - {months} Month(s)".format(**dict(years=s.get("years_experience"),months=s.get("months_experience")))
                #self.flowables.append(Paragraph(line,self.styles.get('Italic')))

            elif s.get("years_experience"):
                line="{years} Year(s)".format(**dict(years=s.get("years_experience")))
                #self.flowables.append(Paragraph(line,self.styles.get('Italic')))

            elif s.get("months_experience"):
                line="{months} Month(s)".format(**dict(months=s.get("months_experience")))
                #self.flowables.append(Paragraph(line,self.styles.get('Italic')))


            self.flowables.append(Paragraph(line,self.styles.get('Italic')))
            for ll in s.get("comment").split("\n"):
                if ll:
                    comment="{l}".format(**dict(l=ll))
                    self.flowables.append(Paragraph(comment,self.ulx,bulletText=" - "))
    
    def handleEmployment(self):
        lEmployment=self.data.get("employment")
        if len(lEmployment) > 0:
            self.flowables.append(Paragraph("Employment",self.hc2))
            self.flowables.append(self.hr)
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
            self.flowables.append(self.hr)

    def handleEducation(self):
        lEducation = self.data.get("education")
        if len(lEducation) > 0:
            self.flowables.append(Paragraph("Education",self.hc2))
            self.flowables.append(self.hr)
        for e in lEducation:
            schoolDegree="{degree} ({school})"
            dateline="{start} - {end}"
            locale="{city}, {state} {ZIP}"
            
            lsd=schoolDegree.format(**dict(degree=e.get("degree"),school=e.get("school")))
            dl=dateline.format(**dict(start=e.get("start_date"),end=e.get("end_date")))
            locale_l=locale.format(**dict(city=e.get("city"),state=e.get("state"),ZIP=e.get("ZIP")))

            self.flowables.append(Paragraph(lsd,self.styles['Heading3']))
            self.flowables.append(Paragraph(dl,self.styles['Normal']))
            self.flowables.append(Paragraph(locale_l,self.styles['Italic']))

        if len(lEducation) > 0:
            self.flowables.append(self.hr)

    def handleCertification(self):
        lCertification=self.data.get("certification")
        if len(lCertification) > 0:
            self.flowables.append(Paragraph("Certification",self.hc2))
            self.flowables.append(self.hr)

        for cert in lCertification:
            name_l="{name}".format(**dict(name=cert.get("certification_name")))
            date_l="{start} - {end}".format(**dict(start=cert.get("date_acquired"),end=cert.get("date_expires")))
            self.flowables.append(Paragraph(name_l,self.styles['Heading3']))
            self.flowables.append(Paragraph(date_l,self.styles['Normal']))
        if len(lCertification) > 0:
            self.flowables.append(self.hr)

    def handleLinks(self):
        links=self.data.get("links")
        if len(links) > 0:
            self.flowables.append(Paragraph("Links",self.hc2))
            self.flowables.append(self.hr)

        for link in links:
            self.flowables.append(Paragraph(link.get('link'),self.styles['Normal'],bulletText=" - "))

        if len(links) > 0:
            self.flowables.append(self.hr)

    def handleAdditionalInfo(self):
        lAdditionalInfo=self.data.get("additionalInfo")
        if len(lAdditionalInfo) > 0:
            self.flowables.append(Paragraph("Additional Info.",self.hc2))
            self.flowables.append(self.hr)

        for ai in lAdditionalInfo:
            t="{t}".format(**dict(t=ai.get("type")))
            if len(t) > 0:
                t=t[0].upper()+t[1:].lower()
            self.flowables.append(Paragraph(t,self.styles['Heading3']))
            for line in ai.get("additional_info").split("\n"):
                self.flowables.append(Paragraph(line,self.ulx,bulletText=" - "))

        if len(lAdditionalInfo) > 0:
            self.flowables.append(self.hr)

