from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_CENTER,TA_JUSTIFY
from reportlab.platypus import Spacer,HRFlowable
from ...MainWindow.pdf_header import genHeader
class generator:
    def __init__(self,contact,references,path):
        self.contact=contact
        self.references=references
        self.path=path
        print(path,contact,references)
        self.doc=SimpleDocTemplate(path)
        self.styles=getSampleStyleSheet()
        
        employer_title="{employer} ({title})"
        name="{fname} {mname} {lname}"
        phone="{number} {type}"
        email="{email}"
        street="{number} {name}"
        locale="{city}, {state} {ZIP}" 

        flowables=[]
        flowables.extend(genHeader(self.contact).generate())
                
        for i in self.references:
            if i.get('first_name') and i.get('last_name'):
                l_name=name.format(**dict(fname=i.get("first_name"),lname=i.get("last_name"),mname=i.get("middle_name")))
                flowables.append(Paragraph(l_name,self.styles['Heading3']))

            if i.get('employer') and i.get('title'):
                l_employer_title=employer_title.format(**dict(employer=i.get("employer"),title=i.get("title")))
                flowables.append(Paragraph(l_employer_title,self.styles['Heading4']))

            if i.get('phone_number'):
                if i.get("phone_type") != "":
                    l_phone=phone.format(**dict(number=i.get("phone_number"),type="({t})".format(**dict(t=i.get("phone_type")))))
                else:
                    l_phone=phone.format(**dict(number=i.get("phone_number"),type=i.get("phone_type")))

                flowables.append(Paragraph(l_phone,self.styles['Italic']))

            if i.get('email'):
                l_email=email.format(**dict(email=i.get("email")))
                flowables.append(Paragraph(l_email,self.styles['Normal']))

            if i.get('street_number') and i.get('street_name'):
                l_street=street.format(**dict(number=i.get("street_number"),name=i.get("street_name")))
                flowables.append(Paragraph(l_street,ParagraphStyle('N8',parent=self.styles['Normal'],fontSize=8)))

            if i.get('city') and i.get('state') and i.get('ZIP'):
                l_locale=locale.format(**dict(city=i.get("city"),state=i.get("state"),ZIP=i.get("ZIP")))
                flowables.append(Paragraph(l_locale,ParagraphStyle('N8',parent=self.styles['Normal'],fontSize=8)))

            
            flowables.append(Spacer(1,16))

        print(self.styles.list())
        self.generate(flowables)
        

    def generate(self,flowables):
        self.doc.build(flowables)
