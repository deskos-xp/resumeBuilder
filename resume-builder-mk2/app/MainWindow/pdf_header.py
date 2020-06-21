from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_CENTER,TA_JUSTIFY
from reportlab.platypus import Spacer,HRFlowable

class genHeader:
    def __init__(self,contact):
        self.contact=contact
        self.styles=getSampleStyleSheet()
        #self.centered:ParagraphStyle=self.styles.get('Heading1')
        self.centered=ParagraphStyle(name="Heading1_Centered",parent=self.styles.get("Heading1"),alignment=TA_CENTER)
        self.centered_info=ParagraphStyle(name="ci1",parent=self.styles.get("Italic"),alignment=TA_CENTER)
        
    def generate(self) -> list:
        flowables=list()
        flowables.append(
            Paragraph(
                "{f}{m}{l}".format(
                    **dict(
                        f=self.contact.get("first_name"),
                        m=" {}".format(self.contact.get('middle_name')),
                        l=" {}".format(self.contact.get("last_name"))
                    )
                ),
                self.centered
                
            )
        )
        contact=dict()
        if self.contact.get("phone_type"):
            contact['phone_type']=' ('+self.contact['phone_type']+')'
        if self.contact.get("email"):
            contact['email']=" - "+self.contact['email']
        flowables.append(Paragraph("{phone_number}{phone_type}{email}".format(**dict(
                    phone_number=self.contact.get('phone_number'),
                    phone_type=contact.get("phone_type"),
                    email=contact.get("email")
                    )
                ),
                self.centered_info
                )
            )
        address="{street_number} {street_name}, {city}, {state} {ZIP}".format(
                **dict(
                    street_number=self.contact.get("street_number"),
                    street_name=self.contact.get("street_name"),
                    city=self.contact.get("city"),
                    state=self.contact.get("state"),
                    ZIP=self.contact.get("ZIP")
                    ))
        flowables.append(Paragraph(address,self.centered_info))
        flowables.append(HRFlowable(width="98%"))
                    
        return flowables


