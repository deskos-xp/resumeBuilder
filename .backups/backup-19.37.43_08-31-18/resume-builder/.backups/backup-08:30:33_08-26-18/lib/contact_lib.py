#! /usr/bin/env python3
from PyQt5 import QtGui,QtWidgets,QtCore
import contact_widget
import checkers_lib

class contact:
    master=None

    def contact_combobox(self,widget):
        for state in self.states:
            widget.state.addItem(state)

    def contact_submit(self,widget):
        contact={}
        contact['fname']=widget.fname.text()
        contact['lname']=widget.lname.text()
        contact['mname']=widget.mname.text()
        contact['email']=widget.email.text()
        contact['phone']=widget.phone.text()
        contact['street']=widget.street.text()
        contact['zip']=widget.zip.text()
        contact['city']=widget.city.text()
        contact['state']=str(widget.state.currentText())
        count=0
        contactCount=0
        for key in contact.keys():
            if contact[key] == '':
                if key in ['email','phone']:
                    if contact[key]=='':
                        contactCount+=1
                    if contactCount > 1:
                        count+=1
                else:
                    if key != 'mname':
                        count+=1
        if count == 0:
            self.contact_data=contact
        else:
            self.contact_data={}
        print(self.contact_data)
        
    
    def contact_set_tab_orders(self):
        tabChains0=[
                [self.pushButton_2,self.pushButton_7],
                [self.pushButton_7,self.pushButton],
               ]
        for p1,p2 in tabChains0:
            QtWidgets.QWidget.setTabOrder(p1,p2)

        if self.groupBox_contact != None:
            for num,key in enumerate(self.groupBox_contact.keys()):
                w=self.groupBox_contact[key][1]

                tabChains=[
                    [w.fname,w.mname],
                    [w.mname,w.lname],
                    [w.lname,w.email],
                    [w.email,w.phone],
                    [w.phone,w.street],
                    [w.street,w.city],
                    [w.city,w.state],
                    [w.state,w.zip],
                    ]
        for p1,p2 in tabChains:
            self.setTabOrder(p1,p2)
    
    def contact_clear(self,widget):
        widget.fname.setText('')
        widget.lname.setText('')
        widget.phone.setText('')
        widget.mname.setText('')
        widget.email.setText('')
        widget.street.setText('')
        widget.zip.setText('')
        widget.city.setText('')
        widget.state.setCurrentText('Set Your State')
        self.validateFields()

    def contact_proper_phone(self,widget):
        if len(widget.phone.text()) > 0:
            phone=self.phoneStripper(widget.phone.text())
            if len(phone) in [7,10,11]:
                self.statusBar().showMessage('')
                self.setValidFields(widget.phone)
                self.setValidFields(widget.email)
            else:
                self.statusBar().showMessage('Bad Phone Number!')
                self.setInvalidFields(widget.phone)
                if len(widget.email.text()) < 1:
                    self.setInvalidFields(widget.email)
                else:
                    self.setValidFields(widget.email)
        else:
            self.statusBar().showMessage('Bad Phone Number!')
            if len(widget.email.text()) < 1:
                self.setInvalidFields(widget.phone)
            else:
                self.setValidFields(widget.phone)

    def contact_phone_check(self,widget):
        widget.phone.setMaxLength(16)
        self.setInvalidFields(widget.phone)
        widget.phone.textChanged.connect(lambda:self.contact_proper_phone(widget))


    def contact_invalidUntilFilled_email(self,qtypew,widget):
        phone=self.phoneStripper(widget.phone.text())
        if len(widget.email.text()) > 0:
            email=checkers_lib.checkers_email()
            verify=email.correct_email(widget.email.text())
            if verify[1] == True:
                self.statusBar().showMessage('')
                if len(phone) in [0,7,10,11]:
                    self.setValidFields(widget.phone)
                else:
                    self.setInvalidFields(widget.phone)
                self.setValidFields(widget.email)
            else:
                if len(phone) not in [7,10,11]:
                    self.setInvalidFields(widget.phone)
                self.setInvalidFields(widget.email)
                self.statusBar().showMessage('Bad Email Address!')
        else:
            self.statusBar().showMessage('Bad Email Address!')
            if len(phone) not in [7,10,11]:
                self.setInvalidFields(widget.phone)
            else:
                self.setValidFields(widget.email)
                

    def contact_buttons_connect(self,widget):
        self.pushButton.clicked.connect(lambda:self.nextCallBack(widget))
        self.pushButton_2.clicked.connect(lambda:self.contact_clear(widget))
        self.pushButton_7.clicked.connect(lambda:self.contact_submit(widget))


    def newContactObj(self,counter):
        widget=contact_widget.Ui_contact()
        widget.setupUi(self)
        widget1=widget.groupBox
        self.contact_combobox(widget)
        self.contact_clear(widget)
        self.contact_phone_check(widget)
        self.contact_invalidUntilFilled(widget)
        self.contact_buttons_connect(widget)
        return widget1,widget

    def newContact(self):
        if self.groupBox_contact == None:
            self.contact_counter=0
            self.groupBox_contact={}
        self.groupBox_contact[str(self.contact_counter)]=self.newContactObj(self.contact_counter)
        self.gridLayout.addWidget(self.groupBox_contact[str(self.contact_counter)][0],0,0,1,1)
        self.contact_set_tab_orders()
        self.contact_submit(self.groupBox_contact[str(self.contact_counter)][1])
        self.validateFields()

    def contact_invalidUntilFilled(self,widget): 
        self.setInvalidFields(widget.fname)
        widget.fname.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.fname))

        self.setInvalidFields(widget.lname)
        #self.setInvalidFields(widget.mname)
        self.setInvalidFields(widget.email)
        self.setInvalidFields(widget.street)
        self.setInvalidFields(widget.zip)
        self.setInvalidFields(widget.city)
        
        widget.lname.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lname))
        #widget.mname.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.mname))
        widget.email.textChanged.connect(lambda:self.contact_invalidUntilFilled_email('le',widget))
        widget.street.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.street))
        widget.zip.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.zip))
        widget.city.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.city))
        widget.state.currentIndexChanged.connect(self.validateFields)


