# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'links.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_links(object):
    def setupUi(self, links):
        links.setObjectName("links")
        links.resize(800, 600)
        self.gridLayout_2 = QtWidgets.QGridLayout(links)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(links)
        self.groupBox.setMinimumSize(QtCore.QSize(400, 100))
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.link = QtWidgets.QLineEdit(self.groupBox)
        self.link.setObjectName("link")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.link)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(links)
        QtCore.QMetaObject.connectSlotsByName(links)

    def retranslateUi(self, links):
        _translate = QtCore.QCoreApplication.translate
        links.setWindowTitle(_translate("links", "ResumeBuilder"))
        self.groupBox.setTitle(_translate("links", "Web Link"))
        self.pushButton_2.setText(_translate("links", "Clear"))
        self.pushButton.setText(_translate("links", "Remove"))
        self.label.setText(_translate("links", "Link"))

