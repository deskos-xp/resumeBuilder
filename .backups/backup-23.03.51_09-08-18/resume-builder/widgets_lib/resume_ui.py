# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/resumeBuilder.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/png/resume-builder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.contact_tab = QtWidgets.QWidget()
        self.contact_tab.setObjectName("contact_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.contact_tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.contact_tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 752, 441))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_40 = QtWidgets.QGridLayout()
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.pushButton_2 = QtWidgets.QPushButton(self.contact_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_40.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.contact_tab)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_40.addWidget(self.pushButton_7, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.contact_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_40.addWidget(self.pushButton, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_40, 0, 0, 1, 1)
        self.tabWidget.addTab(self.contact_tab, "")
        self.employment_tab = QtWidgets.QWidget()
        self.employment_tab.setMinimumSize(QtCore.QSize(0, 0))
        self.employment_tab.setObjectName("employment_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.employment_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.employment_tab)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_36 = QtWidgets.QGridLayout()
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.pushButton_3 = QtWidgets.QPushButton(self.employment_tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_36.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.employment_tab)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_36.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.employment_tab)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_36.addWidget(self.pushButton_6, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.employment_tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_36.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_36, 0, 0, 1, 1)
        self.tabWidget.addTab(self.employment_tab, "")
        self.education_tab = QtWidgets.QWidget()
        self.education_tab.setObjectName("education_tab")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.education_tab)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.education_tab)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_11.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 1, 0, 1, 1)
        self.gridLayout_35 = QtWidgets.QGridLayout()
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.pushButton_8 = QtWidgets.QPushButton(self.education_tab)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_35.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.education_tab)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_35.addWidget(self.pushButton_10, 0, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.education_tab)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_35.addWidget(self.pushButton_9, 0, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.education_tab)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_35.addWidget(self.pushButton_11, 0, 3, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_35, 0, 0, 1, 1)
        self.tabWidget.addTab(self.education_tab, "")
        self.cert_tab = QtWidgets.QWidget()
        self.cert_tab.setObjectName("cert_tab")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.cert_tab)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.cert_tab)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_18.addLayout(self.gridLayout_17, 0, 0, 1, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_15.addWidget(self.scrollArea_4, 0, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.gridLayout_34 = QtWidgets.QGridLayout()
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.pushButton_12 = QtWidgets.QPushButton(self.cert_tab)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_34.addWidget(self.pushButton_12, 0, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.cert_tab)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_34.addWidget(self.pushButton_13, 0, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.cert_tab)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_34.addWidget(self.pushButton_14, 0, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.cert_tab)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_34.addWidget(self.pushButton_15, 0, 3, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_34, 0, 0, 1, 1)
        self.tabWidget.addTab(self.cert_tab, "")
        self.skills_tab = QtWidgets.QWidget()
        self.skills_tab.setObjectName("skills_tab")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.skills_tab)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.skills_tab)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_22.addLayout(self.gridLayout_21, 0, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_19.addWidget(self.scrollArea_5, 0, 0, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_19, 1, 0, 1, 1)
        self.gridLayout_37 = QtWidgets.QGridLayout()
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.pushButton_17 = QtWidgets.QPushButton(self.skills_tab)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_37.addWidget(self.pushButton_17, 0, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.skills_tab)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_37.addWidget(self.pushButton_16, 0, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.skills_tab)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_37.addWidget(self.pushButton_18, 0, 2, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.skills_tab)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_37.addWidget(self.pushButton_19, 0, 3, 1, 1)
        self.gridLayout_20.addLayout(self.gridLayout_37, 0, 0, 1, 1)
        self.tabWidget.addTab(self.skills_tab, "")
        self.links_tab = QtWidgets.QWidget()
        self.links_tab.setObjectName("links_tab")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.links_tab)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.gridLayout_31 = QtWidgets.QGridLayout()
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.links_tab)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.gridLayout_33 = QtWidgets.QGridLayout()
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.gridLayout_41.addLayout(self.gridLayout_33, 0, 0, 1, 1)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.gridLayout_31.addWidget(self.scrollArea_8, 0, 0, 1, 1)
        self.gridLayout_32.addLayout(self.gridLayout_31, 1, 0, 1, 1)
        self.gridLayout_42 = QtWidgets.QGridLayout()
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.pushButton_29 = QtWidgets.QPushButton(self.links_tab)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_42.addWidget(self.pushButton_29, 0, 0, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.links_tab)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_42.addWidget(self.pushButton_30, 0, 1, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.links_tab)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_42.addWidget(self.pushButton_31, 0, 2, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.links_tab)
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_42.addWidget(self.pushButton_32, 0, 3, 1, 1)
        self.gridLayout_32.addLayout(self.gridLayout_42, 0, 0, 1, 1)
        self.tabWidget.addTab(self.links_tab, "")
        self.additional_info_tab = QtWidgets.QWidget()
        self.additional_info_tab.setObjectName("additional_info_tab")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.additional_info_tab)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.additional_info_tab)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.gridLayout_26.addLayout(self.gridLayout_25, 0, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_23.addWidget(self.scrollArea_6, 0, 0, 1, 1)
        self.gridLayout_24.addLayout(self.gridLayout_23, 1, 0, 1, 1)
        self.gridLayout_38 = QtWidgets.QGridLayout()
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.pushButton_22 = QtWidgets.QPushButton(self.additional_info_tab)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_38.addWidget(self.pushButton_22, 0, 2, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.additional_info_tab)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_38.addWidget(self.pushButton_21, 0, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.additional_info_tab)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_38.addWidget(self.pushButton_20, 0, 0, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.additional_info_tab)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_38.addWidget(self.pushButton_23, 0, 3, 1, 1)
        self.gridLayout_24.addLayout(self.gridLayout_38, 0, 0, 1, 1)
        self.tabWidget.addTab(self.additional_info_tab, "")
        self.references_tab = QtWidgets.QWidget()
        self.references_tab.setObjectName("references_tab")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.references_tab)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.references_tab)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.gridLayout_29 = QtWidgets.QGridLayout()
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.gridLayout_30.addLayout(self.gridLayout_29, 0, 0, 1, 1)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.gridLayout_27.addWidget(self.scrollArea_7, 0, 0, 1, 1)
        self.gridLayout_28.addLayout(self.gridLayout_27, 1, 0, 1, 1)
        self.gridLayout_39 = QtWidgets.QGridLayout()
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.pushButton_26 = QtWidgets.QPushButton(self.references_tab)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_39.addWidget(self.pushButton_26, 0, 2, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.references_tab)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_39.addWidget(self.pushButton_25, 0, 1, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.references_tab)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_39.addWidget(self.pushButton_24, 0, 0, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.references_tab)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_39.addWidget(self.pushButton_27, 0, 3, 1, 1)
        self.gridLayout_28.addLayout(self.gridLayout_39, 0, 0, 1, 1)
        self.tabWidget.addTab(self.references_tab, "")
        self.gen_tab = QtWidgets.QWidget()
        self.gen_tab.setObjectName("gen_tab")
        self.gridLayout_44 = QtWidgets.QGridLayout(self.gen_tab)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.gridLayout_43 = QtWidgets.QGridLayout()
        self.gridLayout_43.setObjectName("gridLayout_43")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_43.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.gen_tab)
        self.pushButton_28.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_43.addWidget(self.pushButton_28, 1, 2, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.gen_tab)
        self.pushButton_37.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_43.addWidget(self.pushButton_37, 1, 3, 1, 1)
        self.pushButton_33 = QtWidgets.QPushButton(self.gen_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy)
        self.pushButton_33.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout_43.addWidget(self.pushButton_33, 1, 1, 1, 1)
        self.pushButton_35 = QtWidgets.QPushButton(self.gen_tab)
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_43.addWidget(self.pushButton_35, 2, 2, 1, 1)
        self.pushButton_34 = QtWidgets.QPushButton(self.gen_tab)
        self.pushButton_34.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout_43.addWidget(self.pushButton_34, 2, 3, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.gen_tab)
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout_43.addWidget(self.pushButton_38, 2, 1, 1, 1)
        self.gridLayout_44.addLayout(self.gridLayout_43, 1, 1, 1, 1)
        self.gridLayout_45 = QtWidgets.QGridLayout()
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.pushButton_36 = QtWidgets.QPushButton(self.gen_tab)
        self.pushButton_36.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout_45.addWidget(self.pushButton_36, 0, 0, 1, 1)
        self.save = QtWidgets.QLineEdit(self.gen_tab)
        self.save.setObjectName("save")
        self.gridLayout_45.addWidget(self.save, 0, 1, 1, 1)
        self.gridLayout_44.addLayout(self.gridLayout_45, 0, 1, 1, 1)
        self.tabWidget.addTab(self.gen_tab, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuimport = QtWidgets.QMenu(self.menuFile)
        self.menuimport.setObjectName("menuimport")
        self.menuProgress = QtWidgets.QMenu(self.menubar)
        self.menuProgress.setObjectName("menuProgress")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPrevious = QtWidgets.QAction(MainWindow)
        self.actionPrevious.setObjectName("actionPrevious")
        self.actionNext = QtWidgets.QAction(MainWindow)
        self.actionNext.setObjectName("actionNext")
        self.actionImport_References = QtWidgets.QAction(MainWindow)
        self.actionImport_References.setObjectName("actionImport_References")
        self.actionImport_Resume = QtWidgets.QAction(MainWindow)
        self.actionImport_Resume.setObjectName("actionImport_Resume")
        self.actionImport_json = QtWidgets.QAction(MainWindow)
        self.actionImport_json.setObjectName("actionImport_json")
        self.menuimport.addAction(self.actionImport_References)
        self.menuimport.addAction(self.actionImport_Resume)
        self.menuimport.addAction(self.actionImport_json)
        self.menuFile.addAction(self.menuimport.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuProgress.addAction(self.actionPrevious)
        self.menuProgress.addAction(self.actionNext)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProgress.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ResumeBuilder"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.pushButton_7.setText(_translate("MainWindow", "Submit"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contact_tab), _translate("MainWindow", "Contact"))
        self.pushButton_3.setText(_translate("MainWindow", "New"))
        self.pushButton_5.setText(_translate("MainWindow", "Previous"))
        self.pushButton_6.setText(_translate("MainWindow", "Submit"))
        self.pushButton_4.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.employment_tab), _translate("MainWindow", "Employment"))
        self.pushButton_8.setText(_translate("MainWindow", "Previous"))
        self.pushButton_10.setText(_translate("MainWindow", "Submit"))
        self.pushButton_9.setText(_translate("MainWindow", "New"))
        self.pushButton_11.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.education_tab), _translate("MainWindow", "Education"))
        self.pushButton_12.setText(_translate("MainWindow", "Previous"))
        self.pushButton_13.setText(_translate("MainWindow", "New"))
        self.pushButton_14.setText(_translate("MainWindow", "Submit"))
        self.pushButton_15.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cert_tab), _translate("MainWindow", "Certifications"))
        self.pushButton_17.setText(_translate("MainWindow", "New"))
        self.pushButton_16.setText(_translate("MainWindow", "Previous"))
        self.pushButton_18.setText(_translate("MainWindow", "Submit"))
        self.pushButton_19.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.skills_tab), _translate("MainWindow", "Skills"))
        self.pushButton_29.setText(_translate("MainWindow", "Previous"))
        self.pushButton_30.setText(_translate("MainWindow", "New"))
        self.pushButton_31.setText(_translate("MainWindow", "Submit"))
        self.pushButton_32.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.links_tab), _translate("MainWindow", "Links"))
        self.pushButton_22.setText(_translate("MainWindow", "Submit"))
        self.pushButton_21.setText(_translate("MainWindow", "New"))
        self.pushButton_20.setText(_translate("MainWindow", "Previous"))
        self.pushButton_23.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.additional_info_tab), _translate("MainWindow", "Additional Information"))
        self.pushButton_26.setText(_translate("MainWindow", "Submit"))
        self.pushButton_25.setText(_translate("MainWindow", "New"))
        self.pushButton_24.setText(_translate("MainWindow", "Previous"))
        self.pushButton_27.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.references_tab), _translate("MainWindow", "References"))
        self.pushButton_28.setText(_translate("MainWindow", "Generate XML - References"))
        self.pushButton_37.setText(_translate("MainWindow", "Generate XML - Resume"))
        self.pushButton_33.setText(_translate("MainWindow", "Generate JSON"))
        self.pushButton_35.setText(_translate("MainWindow", "Generate PDF - References"))
        self.pushButton_34.setText(_translate("MainWindow", "Generate PDF - Resume"))
        self.pushButton_38.setText(_translate("MainWindow", "Exit"))
        self.pushButton_36.setText(_translate("MainWindow", "Previous"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gen_tab), _translate("MainWindow", "Gen"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuimport.setTitle(_translate("MainWindow", "&Import"))
        self.menuProgress.setTitle(_translate("MainWindow", "Pro&gress"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPrevious.setText(_translate("MainWindow", "&Previous"))
        self.actionPrevious.setShortcut(_translate("MainWindow", "Alt+P"))
        self.actionNext.setText(_translate("MainWindow", "&Next"))
        self.actionNext.setShortcut(_translate("MainWindow", "Alt+N"))
        self.actionImport_References.setText(_translate("MainWindow", "Import Ref&erences XML"))
        self.actionImport_Resume.setText(_translate("MainWindow", "Import &Resume XML"))
        self.actionImport_json.setText(_translate("MainWindow", "Import &Json"))

