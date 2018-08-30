#! /usr/bin/python3
from PyQt5 import QtGui,QtWidgets,QtCore
import school_widget
import time
class school:
    master=None
    def school_invalidUntilFilled(self,widget):
        self.setInvalidFields(widget.name)
        widget.name.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.name))
        
        self.setInvalidFields(widget.dateString)
        widget.dateString.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.dateString))
        
        self.setInvalidFields(widget.degree)
        widget.degree.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.degree))

        self.setInvalidFields(widget.city)
        widget.city.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.city))

        self.setInvalidFields(widget.zip)
        widget.zip.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.zip))

        self.setInvalidFields(widget.school_type_edit)
        widget.school_type_edit.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.school_type_edit))
        widget.state.currentIndexChanged.connect(self.validateFields)
        widget.school_type.currentIndexChanged.connect(self.validateFields)

    def school_set_tab_orders(self):
        tabChains0=[
                [self.pushButton_8,self.pushButton_9],
                [self.pushButton_9,self.pushButton_10],
                [self.pushButton_10,self.pushButton_11],
                ]
        for p1,p2 in tabChains0:
            QtWidgets.QWidget.setTabOrder(p1,p2)

        if self.groupBox_school != None:
            for key in self.groupBox_school.keys():
                w=self.groupBox_school[key][1]
                tabChains=[
                        [w.pushButton,w.pushButton_2],
                        [w.pushButton_2,w.name],
                        [w.name,w.startDate],
                        [w.startDate,w.checkBox],
                        [w.checkBox,w.endDate],
                        [w.endDate,w.degree],
                        [w.degree,w.city],
                        [w.city,w.state],
                        [w.state,w.zip],
                        [w.zip,w.school_type],
                        [w.school_type,w.school_type_edit],
                        ]
                for p1,p2 in tabChains:
                    QtWidgets.QWidget.setTabOrder(p1,p2)

    def school_setStates(self,widget):
        for state in self.states:
            widget.state.addItem(state)
    def school_typeEdit_change(self,widget):
        widget.school_type_edit.setText(widget.school_type.currentText())

    def school_setTypes(self,widget):
        for t in ['Basic School Types','High School','2 Year College', '4 Year College','Trade School','Other']:
            widget.school_type.addItem(t)
        widget.school_type.currentTextChanged.connect(lambda:self.school_typeEdit_change(widget))

    def school_clear_dates(self,widget):
        date=QtCore.QDate()
        date.setDate(2000,1,1)
        widget.startDate.setDate(date)
        widget.endDate.setDate(date)

    def school_clear_actions(self,widget):
        self.school_clear_dates(widget)
        widget.dateString.setText('')
        widget.checkBox.setChecked(False)
        widget.name.setText('')
        widget.degree.setText('')
        widget.zip.setText('')
        widget.city.setText('')
        widget.state.setCurrentText('Set Your State')
        widget.school_type.setCurrentText('Basic School Types')
        widget.school_type_edit.setText('')
        self.validateFields()

    def school_clear_button(self,widget):
        widget.pushButton_2.clicked.connect(lambda:self.school_clear_actions(widget))

    def school_dates_callback(self,widget,school_counter):
        widget.dateString.setText(widget.startDate.date().toString()+" to "+widget.endDate.date().toString())

    def school_dates(self,widget,school_counter):
        widget.startDate.dateChanged.connect(lambda:self.school_dates_callback(widget,school_counter))
        widget.endDate.dateChanged.connect(lambda:self.school_dates_callback(widget,school_counter))

    def school_date_present(self,widget):
        if widget.checkBox.isChecked():
            widget.endDate.setEnabled(False)
            widget.dateString.setText(widget.startDate.date().toString()+" to Present")
        else:
            widget.endDate.setEnabled(True)
            widget.dateString.setText(widget.startDate.date().toString()+" to "+widget.endDate.date().toString())

    def school_remove(self,widget,counter):
        self.groupBox_school[str(counter)][0].hide()
        self.gridLayout_13.removeWidget(self.groupBox_school[str(counter)][0])
        self.groupBox_school[str(counter)][0].deleteLater()
        self.groupBox_school.pop(str(counter))
        if len(self.groupBox_school.keys()) < 1:
            self.school_counter=0
            self.pushButton_11.setEnable(True)

        for num,group in enumerate(self.groupBox_school.keys()):
            self.groupBox_school[group][0].hide()
            self.gridLayout_13.removeWidget(self.groupBox_school[group][0])
            self.gridLayout_13.addWidget(self.groupBox_school[group][0],num+1,0,1,1)
            self.groupBox_school[group][0].show()
    
    def school_dateString(self,widget):
        widget.dateString.setReadOnly(True)

    def newSchoolObj(self,school_counter):
        widget=school_widget.Ui_school()
        print(school_counter)
        widget.setupUi(self)
        widget1=widget.groupBox
        widget1.setTitle('School {}'.format('{}:{}:{}'.format(str(time.localtime().tm_hour),str(time.localtime().tm_min),str(time.localtime().tm_sec))))
        self.school_dateString(widget)
        #set remove button
        widget.pushButton.clicked.connect(lambda:self.school_remove(widget,school_counter))
        widget.checkBox.stateChanged.connect(lambda:self.school_date_present(widget))
        #set school dates to proper slots
        self.school_dates(widget,school_counter)
        #connect the clear button
        self.school_clear_button(widget)
        #add states
        self.school_setStates(widget)
        #add types
        self.school_setTypes(widget)
        #set invalid fields
        self.school_invalidUntilFilled(widget)
        return widget1,widget

    def newSchool(self):
        if self.groupBox_school == None:
            self.school_counter=0
            self.groupBox_school={}
        self.groupBox_school[str(self.school_counter)]=self.newSchoolObj(self.school_counter)
        self.gridLayout_13.addWidget(self.groupBox_school[str(self.school_counter)][0],self.school_counter+1,0,1,1)
        self.school_counter+=1
        self.school_set_tab_orders()
        self.validateFields()
        print(self.school_counter)

    def school_submit(self):
        data={}
        if self.groupBox_school != None:
            for group in self.groupBox_school.keys():
                data[group]={}
                e=self.groupBox_school[group][1]
                data[group]['name']=e.name.text()
                data[group]['degree']=e.degree.text()
                data[group]['date']=e.dateString.text()
                data[group]['state']=e.state.currentText()
                data[group]['zip']=e.zip.text()
                data[group]['city']=e.city.text()
                data[group]['type']=e.school_type_edit.text()
        self.school_data=data
        print(data)

    def school_buttons_connect(self):
        self.pushButton_9.clicked.connect(self.newSchool)
        self.pushButton_10.clicked.connect(self.school_submit)
        self.school_set_tab_orders()
