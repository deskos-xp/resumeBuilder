# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skills.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_skills(object):
    def setupUi(self, skills):
        skills.setObjectName("skills")
        skills.resize(800, 600)
        skills.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout_2 = QtWidgets.QGridLayout(skills)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(skills)
        self.groupBox.setMinimumSize(QtCore.QSize(400, 300))
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name = QtWidgets.QLineEdit(self.groupBox)
        self.name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.name.setObjectName("name")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.dateString = QtWidgets.QLineEdit(self.groupBox)
        self.dateString.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dateString.setObjectName("dateString")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateString)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.years = QtWidgets.QSpinBox(self.groupBox)
        self.years.setMaximumSize(QtCore.QSize(300, 16777215))
        self.years.setObjectName("years")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.years)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.months = QtWidgets.QSpinBox(self.groupBox)
        self.months.setMaximumSize(QtCore.QSize(300, 16777215))
        self.months.setObjectName("months")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.months)
        self.gthan = QtWidgets.QRadioButton(self.groupBox)
        self.gthan.setObjectName("gthan")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.gthan)
        self.lthan = QtWidgets.QRadioButton(self.groupBox)
        self.lthan.setObjectName("lthan")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lthan)
        self.eqto = QtWidgets.QRadioButton(self.groupBox)
        self.eqto.setChecked(True)
        self.eqto.setObjectName("eqto")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.eqto)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(skills)
        QtCore.QMetaObject.connectSlotsByName(skills)

    def retranslateUi(self, skills):
        _translate = QtCore.QCoreApplication.translate
        skills.setWindowTitle(_translate("skills", "ResumeBuilder"))
        self.groupBox.setTitle(_translate("skills", "Skill"))
        self.pushButton.setText(_translate("skills", "Remove"))
        self.pushButton_2.setText(_translate("skills", "Clear"))
        self.label.setText(_translate("skills", "Skill"))
        self.label_2.setText(_translate("skills", "Amount"))
        self.label_3.setText(_translate("skills", "Years"))
        self.label_4.setText(_translate("skills", "Months"))
        self.gthan.setText(_translate("skills", "Greater Than, or Greater Than or Equal To"))
        self.lthan.setText(_translate("skills", "Less Than, or Less Than or Equal To"))
        self.eqto.setText(_translate("skills", "Equal To"))

