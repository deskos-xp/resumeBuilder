# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/certifications.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_certs(object):
    def setupUi(self, certs):
        certs.setObjectName("certs")
        certs.resize(800, 600)
        certs.setMinimumSize(QtCore.QSize(400, 420))
        self.gridLayout_2 = QtWidgets.QGridLayout(certs)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(certs)
        self.groupBox.setMinimumSize(QtCore.QSize(400, 200))
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name = QtWidgets.QLineEdit(self.groupBox)
        self.name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.name.setClearButtonEnabled(False)
        self.name.setObjectName("name")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.startDate = QtWidgets.QDateEdit(self.groupBox)
        self.startDate.setMaximumSize(QtCore.QSize(300, 16777215))
        self.startDate.setCalendarPopup(True)
        self.startDate.setObjectName("startDate")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.startDate)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.endDate = QtWidgets.QDateEdit(self.groupBox)
        self.endDate.setMaximumSize(QtCore.QSize(300, 16777215))
        self.endDate.setCalendarPopup(True)
        self.endDate.setObjectName("endDate")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.endDate)
        self.dateString = QtWidgets.QLineEdit(self.groupBox)
        self.dateString.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dateString.setObjectName("dateString")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateString)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(certs)
        QtCore.QMetaObject.connectSlotsByName(certs)

    def retranslateUi(self, certs):
        _translate = QtCore.QCoreApplication.translate
        certs.setWindowTitle(_translate("certs", "ResumeBuilder"))
        self.groupBox.setTitle(_translate("certs", "Certifications"))
        self.label.setText(_translate("certs", "Certification Name"))
        self.label_2.setText(_translate("certs", "Date Aquired"))
        self.startDate.setDisplayFormat(_translate("certs", "M/d/yyyy"))
        self.label_3.setText(_translate("certs", "Date Expires"))
        self.endDate.setDisplayFormat(_translate("certs", "M/d/yyyy"))
        self.pushButton.setText(_translate("certs", "Remove"))
        self.pushButton_2.setText(_translate("certs", "Clear"))

