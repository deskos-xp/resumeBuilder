# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_employerWidget(object):
    def setupUi(self, employerWidget):
        employerWidget.setObjectName("employerWidget")
        employerWidget.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(employerWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(employerWidget)
        self.groupBox_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(400, 420))
        self.groupBox_2.setMaximumSize(QtCore.QSize(400, 420))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setMaximumSize(QtCore.QSize(200, 35))
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_16.setMaximumSize(QtCore.QSize(200, 35))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_16)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setMaximumSize(QtCore.QSize(200, 35))
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_9.setMaximumSize(QtCore.QSize(200, 35))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setMaximumSize(QtCore.QSize(200, 35))
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setMaximumSize(QtCore.QSize(200, 35))
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.formLayout_4.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_15.setMaximumSize(QtCore.QSize(200, 35))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.formLayout_4.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_15)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setMaximumSize(QtCore.QSize(200, 35))
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout_4.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setMinimumSize(QtCore.QSize(150, 80))
        self.textEdit.setObjectName("textEdit")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.endDate = QtWidgets.QDateEdit(self.groupBox_2)
        self.endDate.setEnabled(True)
        self.endDate.setCalendarPopup(True)
        self.endDate.setObjectName("endDate")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.endDate)
        self.startDate = QtWidgets.QDateEdit(self.groupBox_2)
        self.startDate.setCalendarPopup(True)
        self.startDate.setObjectName("startDate")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.startDate)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setMaximumSize(QtCore.QSize(200, 35))
        self.label_16.setObjectName("label_16")
        self.formLayout_4.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_14.setMaximumSize(QtCore.QSize(200, 35))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.formLayout_4.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.dateString = QtWidgets.QLineEdit(self.groupBox_2)
        self.dateString.setObjectName("dateString")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.dateString)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout_4)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.retranslateUi(employerWidget)
        QtCore.QMetaObject.connectSlotsByName(employerWidget)

    def retranslateUi(self, employerWidget):
        _translate = QtCore.QCoreApplication.translate
        employerWidget.setWindowTitle(_translate("employerWidget", "ResumeBuilder"))
        self.groupBox_2.setTitle(_translate("employerWidget", "Employer"))
        self.label_10.setText(_translate("employerWidget", "Employer"))
        self.label_11.setText(_translate("employerWidget", "Title"))
        self.label_12.setText(_translate("employerWidget", "Start Date"))
        self.label_13.setText(_translate("employerWidget", "Duties"))
        self.label_17.setText(_translate("employerWidget", "City"))
        self.label_18.setText(_translate("employerWidget", "State"))
        self.endDate.setDisplayFormat(_translate("employerWidget", "M/d/yyyy"))
        self.startDate.setDisplayFormat(_translate("employerWidget", "M/d/yyyy"))
        self.label.setText(_translate("employerWidget", "End Date"))
        self.checkBox.setText(_translate("employerWidget", "Present"))
        self.label_16.setText(_translate("employerWidget", "ZIP"))
        self.pushButton.setText(_translate("employerWidget", "Remove"))
        self.pushButton_2.setText(_translate("employerWidget", "Clear"))

