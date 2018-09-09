# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/addition_info.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_additional_info(object):
    def setupUi(self, additional_info):
        additional_info.setObjectName("additional_info")
        additional_info.resize(800, 600)
        additional_info.setMinimumSize(QtCore.QSize(400, 100))
        self.gridLayout_2 = QtWidgets.QGridLayout(additional_info)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(additional_info)
        self.groupBox.setMinimumSize(QtCore.QSize(400, 250))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ai_type_edit = QtWidgets.QLineEdit(self.groupBox)
        self.ai_type_edit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.ai_type_edit.setObjectName("ai_type_edit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ai_type_edit)
        self.skip_type = QtWidgets.QCheckBox(self.groupBox)
        self.skip_type.setObjectName("skip_type")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.skip_type)
        self.ai_type = QtWidgets.QComboBox(self.groupBox)
        self.ai_type.setMaximumSize(QtCore.QSize(300, 16777215))
        self.ai_type.setObjectName("ai_type")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.ai_type)
        self.line = QtWidgets.QTextEdit(self.groupBox)
        self.line.setMaximumSize(QtCore.QSize(400, 200))
        self.line.setObjectName("line")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(additional_info)
        QtCore.QMetaObject.connectSlotsByName(additional_info)

    def retranslateUi(self, additional_info):
        _translate = QtCore.QCoreApplication.translate
        additional_info.setWindowTitle(_translate("additional_info", "ResumeBuilder"))
        self.groupBox.setTitle(_translate("additional_info", "Additional Information"))
        self.pushButton.setText(_translate("additional_info", "Remove"))
        self.pushButton_2.setText(_translate("additional_info", "Clear"))
        self.label.setText(_translate("additional_info", "Additional Info."))
        self.skip_type.setText(_translate("additional_info", "Skip Type"))

