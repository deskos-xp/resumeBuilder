from PyQt5 import QtGui,QtWidgets,QtCore
import links_widget
import time

class links:
    def link_set_tab_orders(self):
        tabChains0=[
                [self.pushButton_29,self.pushButton_30],
                [self.pushButton_30,self.pushButton_31],
                [self.pushButton_31,self.pushButton_32],
                ]
        for p1,p2 in tabChains0:
            QtWidgets.QWidget().setTabOrder(p1,p2)

        if self.groupBox_link != None:
            for num,key in enumerate(self.groupBox_link.keys()):
                w=self.groupBox_link[key][1]
                tabChains=[
                        [w.pushButton,w.pushButton_2],
                        [w.pushButton_2,w.link],
                        ]
                for p1,p2 in tabChains:
                    QtWidgets.QWidget().setTabOrder(p1,p2)

    def link_invalidUntilFilled(self,widget):
        self.setInvalidFields(widget.link)
        widget.link.textChanged.connect(lambda:self.invalidUntilFilled('le',widget.link))

    def link_submit(self):
        data={}
        if self.groupBox_link != None:
            for group in self.groupBox_link.keys():
                data[group]={}
                e=self.groupBox_link[group][1]
                data[group]['link']=e.link.text()
        self.link_data=data
        print(data)
    
    def link_clear_actions(self,widget):
        widget.link.setText('')
        self.validateFields()

    def link_clear_button(self,widget):
        widget.pushButton_2.clicked.connect(lambda:self.link_clear_actions(widget))

    def link_remove(self,widget1,link_counter):
        self.groupBox_link[str(link_counter)][0].hide()
        self.gridLayout_33.removeWidget(self.groupBox_link[str(link_counter)][0])
        self.groupBox_link[str(link_counter)][0].deleteLater()
        self.groupBox_link.pop(str(link_counter))
        if len(self.groupBox_link.keys()) < 1:
            self.link_counter=0
            self.pushButton_32.setEnabled(True)
            self.adjust_next()

        for num,group in enumerate(self.groupBox_link.keys()):
            self.groupBox_link[group][0].hide()
            self.gridLayout_33.removeWidget(self.groupBox_link[group][0])
            self.gridLayout_33.addWidget(self.groupBox_link[group][0],num+1,0,1,1)
            self.groupBox_link[group][0].show()
    
    def newLinkObj(self,link_counter):
        widget=links_widget.Ui_links()
        widget.setupUi(self)
        widget1=widget.groupBox
        widget1.setTitle('Link {}'.format('{}:{}:{}'.format(str(time.localtime().tm_hour),str(time.localtime().tm_min),str(time.localtime().tm_sec))))
        #connect remove button
        widget.pushButton.clicked.connect(lambda:self.link_remove(widget1,link_counter))
        #set clear button
        self.link_clear_button(widget)
        #set invalid fields
        self.link_invalidUntilFilled(widget)

        return widget1,widget

    def newLink(self):
        if self.groupBox_link == None:
            self.link_counter=0
            self.groupBox_link={}
        self.groupBox_link[str(self.link_counter)]=self.newLinkObj(self.link_counter)
        self.gridLayout_33.addWidget(self.groupBox_link[str(self.link_counter)][0],self.link_counter+1,0,1,1)
        self.link_counter+=1
        self.link_set_tab_orders()
        self.validateFields()
        print(self.link_counter)

    def link_buttons_connect(self):
        self.pushButton_30.clicked.connect(self.newLink)
        self.pushButton_31.clicked.connect(self.link_submit)
        self.link_set_tab_orders()

