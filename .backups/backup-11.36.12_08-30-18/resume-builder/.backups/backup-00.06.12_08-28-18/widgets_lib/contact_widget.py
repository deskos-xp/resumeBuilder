# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/contact.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_contact(object):
    def setupUi(self, contact):
        contact.setObjectName("contact")
        contact.resize(800, 600)
        contact.setMinimumSize(QtCore.QSize(800, 600))
        self.gridLayout_2 = QtWidgets.QGridLayout(contact)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(contact)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(500, 500))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(200, 35))
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.fname = QtWidgets.QLineEdit(self.groupBox)
        self.fname.setMaximumSize(QtCore.QSize(200, 35))
        self.fname.setObjectName("fname")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fname)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(200, 35))
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.mname = QtWidgets.QLineEdit(self.groupBox)
        self.mname.setMaximumSize(QtCore.QSize(200, 35))
        self.mname.setObjectName("mname")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mname)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(200, 35))
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lname = QtWidgets.QLineEdit(self.groupBox)
        self.lname.setMaximumSize(QtCore.QSize(200, 35))
        self.lname.setObjectName("lname")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lname)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(200, 35))
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.email = QtWidgets.QLineEdit(self.groupBox)
        self.email.setMaximumSize(QtCore.QSize(200, 35))
        self.email.setObjectName("email")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.email)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMaximumSize(QtCore.QSize(200, 35))
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.phone = QtWidgets.QLineEdit(self.groupBox)
        self.phone.setMaximumSize(QtCore.QSize(200, 35))
        self.phone.setObjectName("phone")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.phone)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setMaximumSize(QtCore.QSize(200, 35))
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.street = QtWidgets.QLineEdit(self.groupBox)
        self.street.setMaximumSize(QtCore.QSize(200, 35))
        self.street.setObjectName("street")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.street)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.city = QtWidgets.QLineEdit(self.groupBox)
        self.city.setMaximumSize(QtCore.QSize(200, 35))
        self.city.setObjectName("city")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.city)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.state = QtWidgets.QComboBox(self.groupBox)
        self.state.setMaximumSize(QtCore.QSize(200, 35))
        self.state.setObjectName("state")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.state)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setMaximumSize(QtCore.QSize(200, 35))
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.zip = QtWidgets.QLineEdit(self.groupBox)
        self.zip.setMaximumSize(QtCore.QSize(200, 35))
        self.zip.setObjectName("zip")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.zip)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.formLayout_2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 2)

        self.retranslateUi(contact)
        QtCore.QMetaObject.connectSlotsByName(contact)

    def retranslateUi(self, contact):
        _translate = QtCore.QCoreApplication.translate
        contact.setWindowTitle(_translate("contact", "ResumeBuilder"))
        self.groupBox.setTitle(_translate("contact", "Contact Information"))
        self.label.setText(_translate("contact", "First Name"))
        self.label_2.setText(_translate("contact", "Middle Name or Initial"))
        self.label_3.setText(_translate("contact", "Last Name"))
        self.label_4.setText(_translate("contact", "Email"))
        self.label_5.setText(_translate("contact", "Phone Number"))
        self.label_6.setText(_translate("contact", "Street Address"))
        self.label_8.setText(_translate("contact", "City"))
        self.label_9.setText(_translate("contact", "State"))
        self.label_7.setText(_translate("contact", "ZIP"))
