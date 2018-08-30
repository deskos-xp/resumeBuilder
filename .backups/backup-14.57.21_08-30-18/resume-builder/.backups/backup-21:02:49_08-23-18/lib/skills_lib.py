from PyQt5 import QtGui,QtWidgets,QtCore
import skills_widget
import time

class skills:
    dates={}
    def skill_invalidUntilFilled(self,widget):
        self.setInvalidFields(widget.name)
        widget.name.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.name))
        self.setInvalidFields(widget.dateString)
        widget.dateString.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.dateString))

    def skill_set_tab_orders(self):
        for key in self.groupBox_skill.keys():
            w=self.groupBox_skill[key][1]
            tabChains=[
                [w.name,w.years],
                [w.years,w.months],
                [w.months,w.gthan],
                [w.gthan,w.lthan],
                [w.lthan,w.eqto]
                    ]
            for p1,p2 in tabChains:
                QtWidgets.QWidget().setTabOrder(p1,p2)
    def skill_submit(self):
        data={}
        if self.groupBox_skill != None:
            for group in self.groupBox_skill.keys():
                data[group]={}
                e=self.groupBox_skill[group][1]
                data[group]['name']=e.name.text()
                data[group]['date']=e.dateString.text()
        self.skill_data=data
        print(data)

    def skill_clear_actions(self,widget):
        widget.name.setText('')
        widget.dateString.setText('')
        widget.years.setValue(0)
        widget.months.setValue(0)
        widget.gthan.setChecked(False)
        widget.lthan.setChecked(False)
        widget.eqto.setChecked(True)

    def skill_clear(self,widget):
        widget.pushButton_2.clicked.connect(lambda:self.skill_clear_actions(widget))

    def skill_remove(self,widget1,counter):
        self.groupBox_skill[str(counter)][0].hide()
        self.gridLayout_21.removeWidget(self.groupBox_skill[str(counter)][0])
        self.groupBox_skill[str(counter)][0].deleteLater()
        self.groupBox_skill.pop(str(counter))
        if len(self.groupBox_skill.keys()) < 1:
            self.skill_counter=0

        for num,group in enumerate(self.groupBox_skill.keys()):
            self.groupBox_skill[group][0].hide()
            self.gridLayout_21.removeWidget(self.groupBox_skill[group][0])
            self.gridLayout_21.addWidget(self.groupBox_skill[group][0],num+1,0,1,1)
            self.groupBox_skill[group][0].show()

    def skill_dates_grade(self,widget):
        if widget.lthan.isChecked():
            return '-'
        if widget.gthan.isChecked():
            return '+'
        if widget.eqto.isChecked():
            return ''

    def skill_dates_callBack(self,widget,counter):
        self.dates[str(counter)]={}
        self.dates[str(counter)]['year']=widget.years.value()
        self.dates[str(counter)]['month']=widget.months.value()
        xpString=''
        xp='Experience'

        grade=self.skill_dates_grade(widget)
        if grade == None:
            grade=''
        
        month='Months'
        year='Years'

        if self.dates[str(counter)]['month'] == 1:
            month='Month'
        elif self.dates[str(counter)]['month'] > 1:
            month='Months'
        if self.dates[str(counter)]['year'] == 1:
            year='Year'
        elif self.dates[str(counter)]['year'] > 1:
            year='Years'

        if self.dates[str(counter)]['year'] > 0:
            xpString='{}{} {} {}'.format(grade,self.dates[str(counter)]['year'],year,xp)

        if self.dates[str(counter)]['month'] > 0:
            xpString='{}{} {} {}'.format(grade,self.dates[str(counter)]['month'],month,xp)

        if self.dates[str(counter)]['month'] > 0 and self.dates[str(counter)]['year'] > 0:
            xpString='{}{} {} and {} {} {}'.format(grade,self.dates[str(counter)]['year'],year,self.dates[str(counter)]['month'],month,xp)
        print('{} year {} month {}'.format(grade,self.dates[str(counter)]['year'],self.dates[str(counter)]['month']))
        widget.dateString.setText(xpString)

    def skill_dates(self,widget,counter):
        widget.years.valueChanged.connect(lambda:self.skill_dates_callBack(widget,counter))
        widget.months.valueChanged.connect(lambda:self.skill_dates_callBack(widget,counter))
        widget.lthan.toggled.connect(lambda:self.skill_dates_callBack(widget,counter))
        widget.gthan.toggled.connect(lambda:self.skill_dates_callBack(widget,counter))
        widget.eqto.toggled.connect(lambda:self.skill_dates_callBack(widget,counter))

    def skill_dateString(self,widget):
        widget.dateString.setReadOnly(True)

    def newSkillObj(self,skill_counter):
        widget=skills_widget.Ui_skills()
        widget.setupUi(self)
        widget1=widget.groupBox
        widget1.setTitle('Skill {}'.format('{}:{}:{}'.format(str(time.localtime().tm_hour),str(time.localtime().tm_min),str(time.localtime().tm_sec))))
        #set datestring to readonly
        self.skill_dateString(widget)
        #connect remove button
        widget.pushButton.clicked.connect(lambda:self.skill_remove(widget1,skill_counter))
        #connect dates
        self.skill_dates(widget,skill_counter)
        #connect clear button
        self.skill_clear(widget)
        #set invalid fields
        self.skill_invalidUntilFilled(widget)
        return widget1,widget

    def newSkill(self):
        if self.groupBox_skill == None:
            self.skill_counter=0
            self.groupBox_skill={}
        self.groupBox_skill[str(self.skill_counter)]=self.newSkillObj(self.skill_counter)
        self.gridLayout_21.addWidget(self.groupBox_skill[str(self.skill_counter)][0],self.skill_counter+1,0,1,1)
        self.skill_counter+=1
        self.skill_set_tab_orders()
        print(self.skill_counter)

    def skill_buttons_connect(self):
        self.pushButton_17.clicked.connect(self.newSkill)
        self.pushButton_18.clicked.connect(self.skill_submit)
