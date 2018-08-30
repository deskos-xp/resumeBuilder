from PyQt5 import QtGui,QtWidgets,QtCore
import references_widget
import time
class ref:
    def ref_invalidUntilFilled_email(self,qtype,widget):
        if len(widget.email.text()) > 0:
            self.setValidFields(widget.phone)
        else:
            self.setInvalidFields(widget.phone)

        self.invalidUntilFilled(qtype,widget.email)

    def ref_phone_proper(self,widget):
        if len(widget.phone.text()) > 0:
            phone=''.join([i for i in widget.phone.text() if i in ['1','2','3','4','5','6','7','8','9','0']])
            if len(phone) in [7,10,11]:
                self.setValidFields(widget.email)
                widget.references_invalid_phone.hide()
                self.setValidFields(widget.phone)
            else:
                widget.references_invalid_phone.show()
                self.setInvalidFields(widget.phone)
                self.setInvalidFields(widget.email)
        else:
            self.setInvalidFields(widget.email)
            widget.references_invalid_phone.show()
            if len(widget.email.text()) < 1:
                self.setInvalidFields(widget.phone)
            else:
                self.setValidFields(widget.phone)

    def ref_phone_check(self,widget):
        widget.phone.setMaxLength(16)
        self.setInvalidFields(widget.phone)
        widget.phone.textChanged.connect(lambda:self.ref_phone_proper(widget))
    def ref_invalidUntilFilled(self,widget):
        self.setInvalidFields(widget.employer)
        self.setInvalidFields(widget.title)
        self.setInvalidFields(widget.fname)
        #self.setInvalidFields(widget.mname)
        self.setInvalidFields(widget.lname)
        #self.setInvalidFields(widget.phone)
        self.setInvalidFields(widget.email)
        self.setInvalidFields(widget.street)
        self.setInvalidFields(widget.city)
        self.setInvalidFields(widget.zip)

        widget.employer.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.employer))
        widget.title.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.title))
        widget.fname.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.fname))
        #widget.mname.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.mname))
        widget.lname.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lname))
        #widget.phone.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.phone))
        widget.email.textChanged.connect(lambda:self.ref_invalidUntilFilled_email('le',widget))
        widget.street.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.street))
        widget.city.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.city))
        widget.zip.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.zip))

    def ref_set_tab_orders(self):
        for num,key in enumerate(self.groupBox_ref.keys()):
            w=self.groupBox_ref[key][1]
            tabChains=[
                [w.employer,w.title],
                [w.title,w.fname],
                [w.fname,w.mname],
                [w.mname,w.lname],
                [w.lname,w.phone],
                [w.phone,w.phoneType],
                [w.phoneType,w.email],
                [w.email,w.street],
                [w.street,w.city],
                [w.city,w.state],
                [w.state,w.zip],
                ]

            for p1,p2 in tabChains:
                QtWidgets.QWidget().setTabOrder(p1,p2)

    def ref_setPhoneTypes(self,widget):
        for item in ['Phone Type','Home','Work','Cell']:
            widget.phoneType.addItem(item)

    def ref_submit(self):
        data={}
        if self.groupBox_ref != None:
            for group in self.groupBox_ref.keys():
                data[group]={}
                e=self.groupBox_ref[group][1]
                data[group]['employer']=e.employer.text()
                data[group]['title']=e.title.text()
                data[group]['fname']=e.fname.text()
                data[group]['mname']=e.mname.text()
                data[group]['lname']=e.lname.text()
                data[group]['phone']=e.phone.text()
                data[group]['email']=e.email.text()
                data[group]['street']=e.street.text()
                data[group]['city']=e.city.text()
                data[group]['state']=e.state.currentText()
                data[group]['zip']=e.zip.text()
                data[group]['type']=e.phoneType.currentText()
        self.ref_data=data
        print(data)

    def ref_clear_actions(self,widget):
        widget.state.setCurrentText('Set Your State')
        widget.employer.setText('')
        widget.fname.setText('')
        widget.mname.setText('')
        widget.lname.setText('')
        widget.title.setText('')
        widget.phone.setText('')
        widget.email.setText('')
        widget.street.setText('')
        widget.city.setText('')
        widget.zip.setText('')
        widget.phoneType.setCurrentText('Phone Type')

    def ref_clear_button(self,widget):
        widget.pushButton_2.clicked.connect(lambda:self.ref_clear_actions(widget))

    def ref_setState(self,widget):
        for state in self.states:
            widget.state.addItem(state)

    def ref_remove(self,widget1,counter):
        self.groupBox_ref[str(counter)][0].hide()
        self.gridLayout_29.removeWidget(self.groupBox_ref[str(counter)][0])
        self.groupBox_ref.pop(str(counter))
        if len(self.groupBox_ref.keys()) < 1:
            self.ref_counter=0
        for num,group in enumerate(self.groupBox_ref.keys()):
            self.groupBox_ref[group][0].hide()
            self.gridLayout_29.removeWidget(self.groupBox_ref[group][0])
            self.gridLayout_29.addWidget(self.groupBox_ref[group][0],num+1,0,1,1)
            self.groupBox_ref[group][0].show()

    def newRefObj(self,ref_counter):
        widget=references_widget.Ui_references()
        widget.setupUi(self)
        widget1=widget.groupBox
        widget1.setTitle('Reference {}'.format('{}:{}:{}'.format(str(time.localtime().tm_hour),str(time.localtime().tm_min),str(time.localtime().tm_sec))))

        #set states in combobox
        self.ref_setState(widget)
        #set remove button
        widget.pushButton.clicked.connect(lambda:self.ref_remove(widget1,ref_counter))
        #set clear button
        self.ref_clear_button(widget)
        #set phone types
        self.ref_setPhoneTypes(widget)
        #set tab orders
        self.ref_phone_check(widget)
        #set invalid fields
        self.ref_invalidUntilFilled(widget)
        return widget1,widget

    def newRef(self):
        if self.groupBox_ref == None:
            self.ref_counter=0
            self.groupBox_ref={}
        self.groupBox_ref[str(self.ref_counter)]=self.newRefObj(self.ref_counter)
        self.gridLayout_29.addWidget(self.groupBox_ref[str(self.ref_counter)][0],self.ref_counter+1,0,1,1)
        self.ref_counter+=1
        self.ref_set_tab_orders()
        print(self.ref_counter)

    def ref_buttons_connect(self):
        self.pushButton_25.clicked.connect(self.newRef)
        self.pushButton_26.clicked.connect(self.ref_submit)
