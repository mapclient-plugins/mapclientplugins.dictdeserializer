# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.identifer_label = QLabel(self.configGroupBox)
        self.identifer_label.setObjectName(u"identifer_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.identifer_label)

        self.identifier_lineEdit = QLineEdit(self.configGroupBox)
        self.identifier_lineEdit.setObjectName(u"identifier_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.identifier_lineEdit)

        self.input_label = QLabel(self.configGroupBox)
        self.input_label.setObjectName(u"input_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.input_label)

        self.frame = QFrame(self.configGroupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_lineEdit = QLineEdit(self.frame)
        self.input_lineEdit.setObjectName(u"input_lineEdit")

        self.horizontalLayout.addWidget(self.input_lineEdit)

        self.inputLocation_pushButton = QPushButton(self.frame)
        self.inputLocation_pushButton.setObjectName(u"inputLocation_pushButton")

        self.horizontalLayout.addWidget(self.inputLocation_pushButton)


        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.frame)


        self.gridLayout.addWidget(self.configGroupBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Step", None))
        self.configGroupBox.setTitle("")
        self.identifer_label.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.input_label.setText(QCoreApplication.translate("ConfigureDialog", u"input:  ", None))
        self.inputLocation_pushButton.setText(QCoreApplication.translate("ConfigureDialog", u"...", None))
    # retranslateUi

