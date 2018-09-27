# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapclientplugins\dictdeserializerstep\qt\configuredialog.ui'
#
# Created: Thu Sep 27 12:05:49 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QtGui.QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.configGroupBox = QtGui.QGroupBox(ConfigureDialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.identifer_label = QtGui.QLabel(self.configGroupBox)
        self.identifer_label.setObjectName("identifer_label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.identifer_label)
        self.identifier_lineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.identifier_lineEdit.setObjectName("identifier_lineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.identifier_lineEdit)
        self.input_label = QtGui.QLabel(self.configGroupBox)
        self.input_label.setObjectName("input_label")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.input_label)
        self.frame = QtGui.QFrame(self.configGroupBox)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_lineEdit = QtGui.QLineEdit(self.frame)
        self.input_lineEdit.setObjectName("input_lineEdit")
        self.horizontalLayout.addWidget(self.input_lineEdit)
        self.inputLocation_pushButton = QtGui.QPushButton(self.frame)
        self.inputLocation_pushButton.setObjectName("inputLocation_pushButton")
        self.horizontalLayout.addWidget(self.inputLocation_pushButton)
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.frame)
        self.gridLayout.addWidget(self.configGroupBox, 1, 0, 1, 1)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "Configure Step", None, QtGui.QApplication.UnicodeUTF8))
        self.identifer_label.setText(QtGui.QApplication.translate("ConfigureDialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.input_label.setText(QtGui.QApplication.translate("ConfigureDialog", "input:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.inputLocation_pushButton.setText(QtGui.QApplication.translate("ConfigureDialog", "...", None, QtGui.QApplication.UnicodeUTF8))

