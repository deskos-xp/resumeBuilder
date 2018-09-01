#!/usr/bin/env python3
from PyQt5 import QtGui,QtWidgets,QtCore
import time,os,sys
import certifications_widget

class certs:
    def cert_invalidUntilFilled(self,widget):
        self.setInvalidFields(widget.name)
        widget.name.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.name))
        self.setInvalidFields(widget.dateString)
        widget.dateString.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.dateString))

    def cert_set_tab_orders(self):
        tabChains0=[
                [self.pushButton_12,self.pushButton_13],
                [self.pushButton_13,self.pushButton_14],
                [self.pushButton_14,self.pushButton_15],
                ]
        for p1,p2 in tabChains0:
            QtWidgets.QWidget().setTabOrder(p1,p2)

        if self.groupBox_cert != None:
            for key in self.groupBox_cert.keys():
                w=self.groupBox_cert[key][1]
                tabChains=[
                        [w.pushButton,w.pushButton_2],
                        [w.pushButton_2,w.name],
                        [w.name,w.startDate],
                        [w.startDate,w.endDate]
                        ]
                for p1,p2 in tabChains:
                    QtWidgets.QWidget().setTabOrder(p1,p2)

    def cert_submit(self):
        data={}
        if self.groupBox_cert != None:
            for group in self.groupBox_cert.keys():
                data[group]={}
                e=self.groupBox_cert[group][1]
                data[group]['name']=e.name.text()
                data[group]['date']=e.dateString.text()
        self.cert_data=data
        print(data)

    def cert_clear_dates(self,widget):
        date=QtCore.QDate()
        date.setDate(2000,1,1)
        widget.startDate.setDate(date)
        widget.endDate.setDate(date)

    def cert_clear_actions(self,widget):
        self.cert_clear_dates(widget)
        widget.name.setText('')
        widget.dateString.setText('')
        self.validateFields()

    def cert_clear_button(self,widget):
        widget.pushButton_2.clicked.connect(lambda:self.cert_clear_actions(widget))

    def cert_remove(self,widget,cert_counter):
        self.groupBox_cert[str(cert_counter)][0].hide()
        self.gridLayout_17.removeWidget(self.groupBox_cert[str(cert_counter)][0])
        self.groupBox_cert[str(cert_counter)][0].deleteLater()
        self.groupBox_cert.pop(str(cert_counter))
        if len(self.groupBox_cert.keys()) < 1:
            self.cert_counter=0
            self.pushButton_15.setEnabled(True)

        for num,group in enumerate(self.groupBox_cert.keys()):
            self.groupBox_cert[group][0].hide()
            self.gridLayout_17.removeWidget(self.groupBox_cert[group][0])
            self.gridLayout_17.addWidget(self.groupBox_cert[group][0],num+1,0,1,1)
            self.groupBox_cert[group][0].show()

    def cert_dates_callback(self,widget,cert_counter):
        widget.dateString.setText(widget.startDate.date().toString()+' to '+widget.endDate.date().toString())

    def cert_dates(self,widget,cert_counter):
        widget.startDate.dateChanged.connect(lambda:self.cert_dates_callback(widget,cert_counter))
        widget.endDate.dateChanged.connect(lambda:self.cert_dates_callback(widget,cert_counter))

    def cert_dateString(self,widget):
        widget.dateString.setReadOnly(True)

    def newCertObj(self,cert_counter):
        widget=certifications_widget.Ui_certs()
        widget.setupUi(self)
        widget1=widget.groupBox
        widget1.setTitle('Certification {}'.format('{}:{}:{}'.format(str(time.localtime().tm_hour),str(time.localtime().tm_min),str(time.localtime().tm_sec))))

        #set DateString to readonly
        self.cert_dateString(widget)
        #setup calender slots
        self.cert_dates(widget,cert_counter)
        #connect remove button
        widget.pushButton.clicked.connect(lambda:self.cert_remove(widget1,cert_counter))
        #connect the clear button
        self.cert_clear_button(widget)
        #set invalid fields
        self.cert_invalidUntilFilled(widget)
        return widget1,widget

    def newCert(self):
        if self.groupBox_cert == None:
            self.cert_counter=0
            self.groupBox_cert={}
        self.groupBox_cert[str(self.cert_counter)]=self.newCertObj(self.cert_counter)
        self.gridLayout_17.addWidget(self.groupBox_cert[str(self.cert_counter)][0],self.cert_counter+1,0,1,1)
        self.cert_counter+=1
        self.cert_set_tab_orders()
        self.validateFields()
        print(self.cert_counter)

    def cert_buttons_connect(self):
        self.pushButton_13.clicked.connect(self.newCert)
        self.pushButton_14.clicked.connect(self.cert_submit)
        self.cert_set_tab_orders()
