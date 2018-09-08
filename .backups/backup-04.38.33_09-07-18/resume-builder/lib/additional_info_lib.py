from PyQt5 import QtGui,QtWidgets,QtCore
import additional_info_widget
import time

class ai:
    def ai_set_tab_orders(self):
        tabChains0=[
                [self.pushButton_20,self.pushButton_21],
                [self.pushButton_21,self.pushButton_22],
                [self.pushButton_22,self.pushButton_23],
                ]
        for p1,p2 in tabChains0:
            QtWidgets.QWidget().setTabOrder(p1,p2)

        if self.groupBox_ai != None:
            for num,key in enumerate(self.groupBox_ai.keys()):
                w=self.groupBox_ai[key][1]
                tabChains=[
                        [w.pushButton,w.pushButton_2],
                        [w.pushButton_2,w.line],
                        [w.line,w.skip_type],
                        [w.skip_type,w.ai_type],
                        [w.ai_type,w.ai_type_edit],
                        ]
                for p1,p2 in tabChains:
                    QtWidgets.QWidget().setTabOrder(p1,p2)

    def ai_invalidUntilFilled(self,widget):
        self.setInvalidFields(widget.line)
        self.setInvalidFields(widget.ai_type_edit)
        widget.line.textChanged.connect(lambda:self.invalidUntilFilled('te',widget.line))
        widget.ai_type_edit.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.ai_type_edit))

    def ai_skip_type_callback(self,widget):
        if widget.skip_type.isChecked() == True:
            widget.ai_type_edit.setText('Disabled')
            self.setValidFields(widget.ai_type_edit)
            widget.ai_type_edit.setEnabled(False)
            widget.ai_type.setEnabled(False)
            print(widget.ai_type_edit.text())
        else:
            if widget.ai_type.currentText() not in ['Type','Other']:
                widget.ai_type_edit.setText(widget.ai_type.currentText())
                self.setValidFields(widget.ai_type_edit)
            elif widget.ai_type.currentText() in ['Other']:
                widget.ai_type_edit.setEnabled(True)
                widget.ai_type_edit.setText('')
            elif widget.ai_type.currentText() in ['Type']:
                widget.ai_type_edit.setEnabled(False)
                widget.ai_type_edit.setText(widget.ai_type.currentText())
            
            if widget.ai_type.currentText() in ['Type','Other']:
                self.setInvalidFields(widget.ai_type_edit)
            widget.ai_type.setEnabled(True)


    def ai_skip_type(self,widget):
        widget.skip_type.toggled.connect(lambda:self.ai_skip_type_callback(widget))

    def ai_type_callback(self,widget):
        text=widget.ai_type.currentText()
        if text == 'Other':
            widget.ai_type_edit.setEnabled(True)
            widget.ai_type_edit.setText('')
        else:
            widget.ai_type_edit.setText(widget.ai_type.currentText())
            widget.ai_type_edit.setEnabled(False)

        if text in ['Other','Type']:
            self.setInvalidFields(widget.ai_type_edit)

    def ai_set_types(self,widget):
        for t in self.aiTypes:
            widget.ai_type.addItem(t)
        widget.ai_type.currentIndexChanged.connect(lambda:self.ai_type_callback(widget))
        widget.ai_type_edit.setText(widget.ai_type.currentText())
        widget.ai_type_edit.setEnabled(False)
        self.setInvalidFields(widget.ai_type_edit)

    def stripBadText(self,text):
        for char in ['\t']:
            text=text.replace(char,'')
        return text

    def ai_submit(self):
        data={}
        if self.groupBox_ai != None:
            for group in self.groupBox_ai.keys():
                data[group]={}
                e=self.groupBox_ai[group][1]
                text=e.line.toPlainText()
                data[group]['line']=self.stripBadText(text)
                data[group]['type']=e.ai_type_edit.text()
        self.ai_data=data
        print(data)

    def ai_clear_actions(self,widget):
        widget.line.setPlainText('')
        widget.skip_type.setChecked(False)
        widget.ai_type.setCurrentText('Type')
        self.validateFields()

    def ai_clear_button(self,widget):
        widget.pushButton_2.clicked.connect(lambda:self.ai_clear_actions(widget))

    def ai_remove(self,widget1,ai_counter):
        self.groupBox_ai[str(ai_counter)][0].hide()
        self.gridLayout_25.removeWidget(self.groupBox_ai[str(ai_counter)][0])
        self.groupBox_ai[str(ai_counter)][0].deleteLater()
        self.groupBox_ai.pop(str(ai_counter))
        if len(self.groupBox_ai.keys()) < 1:
            self.ai_counter=0
            self.pushButton_23.setEnabled(True)
            self.adjust_next()

        for num,group in enumerate(self.groupBox_ai.keys()):
            self.groupBox_ai[group][0].hide()
            self.gridLayout_25.removeWidget(self.groupBox_ai[group][0])
            self.gridLayout_25.addWidget(self.groupBox_ai[group][0],num+1,0,1,1)
            self.groupBox_ai[group][0].show()


    def newAiObj(self,ai_counter):
        widget=additional_info_widget.Ui_additional_info()
        widget.setupUi(self)
        widget1=widget.groupBox
        widget1.setTitle('Additional Info. {}'.format('{}:{}:{}'.format(str(time.localtime().tm_hour),str(time.localtime().tm_min),str(time.localtime().tm_sec))))
        #set the remove button
        widget.pushButton.clicked.connect(lambda:self.ai_remove(widget1,ai_counter))
        #set the clear button
        self.ai_clear_button(widget)
        #set invalid fields
        self.ai_invalidUntilFilled(widget)
        #set ai Type
        self.ai_skip_type(widget)
        self.ai_set_types(widget)

        return widget1,widget

    def newAi(self):
        if self.groupBox_ai == None:
            self.ai_counter=0
            self.groupBox_ai={}
        self.groupBox_ai[str(self.ai_counter)]=self.newAiObj(self.ai_counter)
        self.gridLayout_25.addWidget(self.groupBox_ai[str(self.ai_counter)][0],self.ai_counter+1,0,1,1)
        self.ai_counter+=1
        self.ai_set_tab_orders()
        self.validateFields()
        print(self.ai_counter)

    def ai_buttons_connect(self):
        self.pushButton_21.clicked.connect(self.newAi)
        self.pushButton_22.clicked.connect(self.ai_submit)
        self.ai_set_tab_orders()
