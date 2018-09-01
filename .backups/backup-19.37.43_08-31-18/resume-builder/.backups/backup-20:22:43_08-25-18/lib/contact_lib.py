#! /usr/bin/env python3
from PyQt5 import QtGui,QtWidgets,QtCore
import contact_widget
import checkers_lib

class contact:
    master=None

    def contact_combobox(self,widget):
        for state in self.states:
            widget.comboBox.addItem(state)

    def contact_submit(self,widget):
        contact={}
        contact['fname']=widget.lineEdit.text()
        contact['lname']=widget.lineEdit_2.text()
        contact['mname']=widget.lineEdit_4.text()
        contact['email']=widget.lineEdit_5.text()
        contact['phone']=widget.lineEdit_3.text()
        contact['street']=widget.lineEdit_6.text()
        contact['zip']=widget.lineEdit_7.text()
        contact['city']=widget.lineEdit_8.text()
        contact['state']=str(widget.comboBox.currentText())
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
                    [w.lineEdit,w.lineEdit_4],
                    [w.lineEdit_4,w.lineEdit_2],
                    [w.lineEdit_2,w.lineEdit_5],
                    [w.lineEdit_5,w.lineEdit_3],
                    [w.lineEdit_3,w.lineEdit_6],
                    [w.lineEdit_6,w.lineEdit_8],
                    [w.lineEdit_8,w.comboBox],
                    [w.comboBox,w.lineEdit_7],
                    ]
        for p1,p2 in tabChains:
            self.setTabOrder(p1,p2)
    
    def contact_clear(self,widget):
        widget.lineEdit.setText('')
        widget.lineEdit_2.setText('')
        widget.lineEdit_3.setText('')
        widget.lineEdit_4.setText('')
        widget.lineEdit_5.setText('')
        widget.lineEdit_6.setText('')
        widget.lineEdit_7.setText('')
        widget.lineEdit_8.setText('')
        widget.comboBox.setCurrentText('Set Your State')


    def contact_proper_phone(self,widget):
        if len(widget.lineEdit_3.text()) > 0:
            phone=self.phoneStripper(widget.lineEdit_3.text())
            if len(phone) in [7,10,11]:
                self.statusBar().showMessage('')
                self.setValidFields(widget.lineEdit_3)
                self.setValidFields(widget.lineEdit_5)
            else:
                self.statusBar().showMessage('Bad Phone Number!')
                self.setInvalidFields(widget.lineEdit_3)
                if len(widget.lineEdit_5.text()) < 1:
                    self.setInvalidFields(widget.lineEdit_5)
                else:
                    self.setValidFields(widget.lineEdit_5)
        else:
            self.statusBar().showMessage('Bad Phone Number!')
            if len(widget.lineEdit_5.text()) < 1:
                self.setInvalidFields(widget.lineEdit_3)
            else:
                self.setValidFields(widget.lineEdit_3)

    def contact_phone_check(self,widget):
        widget.lineEdit_3.setMaxLength(16)
        self.setInvalidFields(widget.lineEdit_3)
        widget.lineEdit_3.textChanged.connect(lambda:self.contact_proper_phone(widget))


    def contact_invalidUntilFilled_email(self,qtypew,widget):
        phone=self.phoneStripper(widget.lineEdit_3.text())
        if len(widget.lineEdit_5.text()) > 0:
            email=checkers_lib.checkers_email()
            verify=email.correct_email(widget.lineEdit_5.text())
            if verify[1] == True:
                self.statusBar().showMessage('')
                self.setValidFields(widget.lineEdit_3)
                self.setValidFields(widget.lineEdit_5)
            else:
                if len(phone) not in [7,10,11]:
                    self.setInvalidFields(widget.lineEdit_3)
                self.setInvalidFields(widget.lineEdit_5)
                self.statusBar().showMessage('Bad Email Address!')
        else:
            self.statusBar().showMessage('Bad Email Address!')
            if len(phone) not in [7,10,11]:
                self.setInvalidFields(widget.lineEdit_3)

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


    def contact_invalidUntilFilled(self,widget): 
        self.setInvalidFields(widget.lineEdit)
        widget.lineEdit.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lineEdit))

        self.setInvalidFields(widget.lineEdit_2)
        self.setInvalidFields(widget.lineEdit_4)
        self.setInvalidFields(widget.lineEdit_5)
        self.setInvalidFields(widget.lineEdit_6)
        self.setInvalidFields(widget.lineEdit_7)
        self.setInvalidFields(widget.lineEdit_8)
        
        widget.lineEdit_2.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lineEdit_2))
        widget.lineEdit_4.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lineEdit_4))
        widget.lineEdit_5.textChanged.connect(lambda:self.contact_invalidUntilFilled_email('le',widget))
        widget.lineEdit_6.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lineEdit_6))
        widget.lineEdit_7.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lineEdit_7))
        widget.lineEdit_8.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lineEdit_8))


