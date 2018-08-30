from PyQt5 import QtGui,QtWidgets,QtCore
import employer_widget
import time
class emp:
    emp_date={}
    def emp_setInvalidUntilFilled(self,widget):
        self.setInvalidFields(widget.lineEdit_16)
        widget.lineEdit_16.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lineEdit_16))
        
        self.setInvalidFields(widget.lineEdit_9)
        widget.lineEdit_9.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lineEdit_9))

        self.setInvalidFields(widget.dateString)
        widget.dateString.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.dateString))
        self.setInvalidFields(widget.textEdit)
        widget.textEdit.textChanged.connect(lambda:self.invalidUntilFilled('te',widget.textEdit))
        self.setInvalidFields(widget.lineEdit_15)
        widget.lineEdit_15.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lineEdit_15))
        self.setInvalidFields(widget.lineEdit_14)
        widget.lineEdit_14.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.lineEdit_14))

    def emp_set_tab_orders(self):
        tabChains0=[
                    [self.pushButton_5,self.pushButton_3],
                    [self.pushButton_3,self.pushButton_6],
                    [self.pushButton_6,self.pushButton_4],
                    ]
        for p1,p2 in tabChains0:
            QtWidgets.QWidget().setTabOrder(p1,p2)

        if self.groupBox_emp != None:
            for num,key in enumerate(self.groupBox_emp.keys()):
                w=self.groupBox_emp[key][1]
            
                tabChains=[
                        [w.pushButton,w.pushButton_2],
                        [w.pushButton_2,w.lineEdit_16],
                        [w.lineEdit_16,w.lineEdit_9],
                        [w.lineEdit_9,w.startDate],
                        [w.startDate,w.checkBox],
                        [w.checkBox,w.endDate],
                        [w.endDate,w.textEdit],
                        [w.textEdit,w.lineEdit_15],
                        [w.lineEdit_15,w.comboBox_2],
                        [w.comboBox_2,w.lineEdit_14],
                        ]
                for p1,p2 in tabChains:
                    QtWidgets.QWidget().setTabOrder(p1,p2)

    def emp_clear_dates(self,widget):
        #widget.startDate.setDate()
        date=QtCore.QDate()
        date.setDate(2000,1,1)
        widget.startDate.setDate(date)
        widget.endDate.setDate(date)

    def emp_setState(self,widget):
        for state in self.states:
            widget.comboBox_2.addItem(state)

    def emp_clear_actions(self,widget):
        self.emp_clear_dates(widget)
        widget.checkBox.setChecked(False)
        widget.lineEdit_16.setText('')
        widget.lineEdit_9.setText('')
        widget.dateString.setText('')
        widget.textEdit.setPlainText('')
        widget.comboBox_2.setCurrentText('Set Your State')
        widget.lineEdit_14.setText('')
        widget.lineEdit_15.setText('')

    def emp_clear_button(self,widget):
        widget.pushButton_2.clicked.connect(lambda:self.emp_clear_actions(widget))

    def emp_date_present(self,widget):
        if widget.checkBox.isChecked():
            widget.endDate.setEnabled(False)
            widget.dateString.setText(widget.startDate.date().toString()+" to Present")
        else:
            widget.endDate.setEnabled(True)
            widget.dateString.setText(widget.startDate.date().toString()+" to "+widget.endDate.date().toString())

    def emp_dates_callback(self,widget,emp_counter):
        widget.dateString.setText(widget.startDate.date().toString()+' to '+widget.endDate.date().toString())

    def emp_dates(self,widget,emp_counter):
        widget.startDate.dateChanged.connect(lambda: self.emp_dates_callback(widget,emp_counter))
        widget.endDate.dateChanged.connect(lambda: self.emp_dates_callback(widget,emp_counter))


    def emp_remove(self,widget1,counter):
       self.groupBox_emp[str(counter)][0].hide()
       self.gridLayout_9.removeWidget(self.groupBox_emp[str(counter)][0])
       self.groupBox_emp[str(counter)][0].deleteLater()
       self.groupBox_emp.pop(str(counter))
       if len(self.groupBox_emp.keys()) < 1:
           self.emp_counter=0

       for num,group in enumerate(self.groupBox_emp.keys()):
           self.groupBox_emp[group][0].hide()
           self.gridLayout_9.removeWidget(self.groupBox_emp[group][0])
           self.gridLayout_9.addWidget(self.groupBox_emp[group][0],num+1,0,1,1)
           self.groupBox_emp[group][0].show()

    def emp_dateString(self,widget):
        widget.dateString.setReadOnly(True)

    def newEmployerObj(self,emp_counter):
        widget=employer_widget.Ui_employerWidget()
        widget.setupUi(self)
        widget1=widget.groupBox_2
        widget1.setTitle('Employer {}'.format('{}:{}:{}'.format(str(time.localtime().tm_hour),str(time.localtime().tm_min),str(time.localtime().tm_sec))))
        widget.checkBox.stateChanged.connect(lambda:self.emp_date_present(widget))
        widget.pushButton.clicked.connect(lambda:self.emp_remove(widget1,emp_counter))
        #
        self.emp_clear_button(widget)
        #
        self.emp_setState(widget)
        #
        self.emp_dateString(widget)
        #
        self.emp_dates(widget,emp_counter)
        #set invalid fields
        self.emp_setInvalidUntilFilled(widget)
        return widget1,widget

    def emp_submit(self):
        data={}
        if self.groupBox_emp != None:
            for group in self.groupBox_emp.keys():
                data[group]={}
                e=self.groupBox_emp[group][1]
                data[group]['name']=e.lineEdit_16.text()
                data[group]['title']=e.lineEdit_9.text()
                data[group]['date']=e.dateString.text()
                data[group]['duties']=e.textEdit.toPlainText()
                data[group]['state']=str(e.comboBox_2.currentText())
                data[group]['zip']=e.lineEdit_14.text()
                data[group]['city']=e.lineEdit_15.text()
        self.employer_data=data
        print(data)

    def newEmployer(self):
        if self.groupBox_emp == None:
            self.emp_counter=0
            self.groupBox_emp={}
        self.groupBox_emp[str(self.emp_counter)]=self.newEmployerObj(self.emp_counter)
        self.gridLayout_9.addWidget(self.groupBox_emp[str(self.emp_counter)][0],self.emp_counter+1,0,1,1)
        self.emp_counter+=1
        self.emp_set_tab_orders()
        print(self.emp_counter)

    def emp_buttons_connect(self):
        self.pushButton_3.clicked.connect(self.newEmployer)
        self.pushButton_6.clicked.connect(self.emp_submit)
        self.emp_set_tab_orders()

