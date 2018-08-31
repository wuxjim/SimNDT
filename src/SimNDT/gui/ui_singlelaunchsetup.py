# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\singlelaunchsetup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_singleLaunchSetupDialog(object):
    def setupUi(self, singleLaunchSetupDialog):
        singleLaunchSetupDialog.setObjectName("singleLaunchSetupDialog")
        singleLaunchSetupDialog.resize(300, 470)
        singleLaunchSetupDialog.setMinimumSize(QtCore.QSize(300, 470))
        singleLaunchSetupDialog.setMaximumSize(QtCore.QSize(300, 470))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/singleLaunch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        singleLaunchSetupDialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(singleLaunchSetupDialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 430, 230, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(singleLaunchSetupDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 271, 80))
        self.groupBox.setObjectName("groupBox")
        self.transmissionRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.transmissionRadioButton.setGeometry(QtCore.QRect(20, 30, 161, 18))
        self.transmissionRadioButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.transmissionRadioButton.setObjectName("transmissionRadioButton")
        self.pulseEchoRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.pulseEchoRadioButton.setGeometry(QtCore.QRect(20, 50, 97, 18))
        self.pulseEchoRadioButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pulseEchoRadioButton.setObjectName("pulseEchoRadioButton")
        self.groupBox_2 = QtWidgets.QGroupBox(singleLaunchSetupDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 271, 323))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.transducerLocationLabel = QtWidgets.QLabel(self.groupBox_2)
        self.transducerLocationLabel.setObjectName("transducerLocationLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.transducerLocationLabel)
        self.locationComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.locationComboBox.setMinimumSize(QtCore.QSize(80, 0))
        self.locationComboBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.locationComboBox.setObjectName("locationComboBox")
        self.locationComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.locationComboBox)
        self.pointSourceCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.pointSourceCheckBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pointSourceCheckBox.setToolTip("")
        self.pointSourceCheckBox.setObjectName("pointSourceCheckBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pointSourceCheckBox)
        self.transducerSizeLabel = QtWidgets.QLabel(self.groupBox_2)
        self.transducerSizeLabel.setObjectName("transducerSizeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.transducerSizeLabel)
        self.transducerSizeLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.transducerSizeLineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.transducerSizeLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.transducerSizeLineEdit.setObjectName("transducerSizeLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.transducerSizeLineEdit)
        self.centerOffsetLabel = QtWidgets.QLabel(self.groupBox_2)
        self.centerOffsetLabel.setObjectName("centerOffsetLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.centerOffsetLabel)
        self.centerOffsetLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.centerOffsetLineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.centerOffsetLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.centerOffsetLineEdit.setObjectName("centerOffsetLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.centerOffsetLineEdit)
        self.borderOffsetLabel = QtWidgets.QLabel(self.groupBox_2)
        self.borderOffsetLabel.setObjectName("borderOffsetLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.borderOffsetLabel)
        self.borderOffsetLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.borderOffsetLineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.borderOffsetLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.borderOffsetLineEdit.setObjectName("borderOffsetLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.borderOffsetLineEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.previewPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.previewPushButton.setMinimumSize(QtCore.QSize(0, 41))
        self.previewPushButton.setMaximumSize(QtCore.QSize(16777215, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/previewImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previewPushButton.setIcon(icon1)
        self.previewPushButton.setIconSize(QtCore.QSize(24, 24))
        self.previewPushButton.setObjectName("previewPushButton")
        self.verticalLayout.addWidget(self.previewPushButton)
        self.advancedParametersSetupPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.advancedParametersSetupPushButton.setMinimumSize(QtCore.QSize(0, 41))
        self.advancedParametersSetupPushButton.setMaximumSize(QtCore.QSize(16777215, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/simModel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.advancedParametersSetupPushButton.setIcon(icon2)
        self.advancedParametersSetupPushButton.setIconSize(QtCore.QSize(24, 24))
        self.advancedParametersSetupPushButton.setObjectName("advancedParametersSetupPushButton")
        self.verticalLayout.addWidget(self.advancedParametersSetupPushButton)
        self.signalSetupPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.signalSetupPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.signalSetupPushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/signal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signalSetupPushButton.setIcon(icon3)
        self.signalSetupPushButton.setIconSize(QtCore.QSize(24, 24))
        self.signalSetupPushButton.setCheckable(False)
        self.signalSetupPushButton.setDefault(False)
        self.signalSetupPushButton.setFlat(False)
        self.signalSetupPushButton.setObjectName("signalSetupPushButton")
        self.verticalLayout.addWidget(self.signalSetupPushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(singleLaunchSetupDialog)
        self.buttonBox.accepted.connect(singleLaunchSetupDialog.accept)
        self.buttonBox.rejected.connect(singleLaunchSetupDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(singleLaunchSetupDialog)

    def retranslateUi(self, singleLaunchSetupDialog):
        _translate = QtCore.QCoreApplication.translate
        singleLaunchSetupDialog.setWindowTitle(_translate("singleLaunchSetupDialog", "Single Launch Setup"))
        self.groupBox.setTitle(_translate("singleLaunchSetupDialog", "Inspection Method"))
        self.transmissionRadioButton.setText(_translate("singleLaunchSetupDialog", "Through Transmission"))
        self.pulseEchoRadioButton.setText(_translate("singleLaunchSetupDialog", "Pulse Echo"))
        self.groupBox_2.setTitle(_translate("singleLaunchSetupDialog", "Transducer Setup"))
        self.transducerLocationLabel.setText(_translate("singleLaunchSetupDialog", "Transducer Location"))
        self.locationComboBox.setItemText(0, _translate("singleLaunchSetupDialog", "Top"))
        self.pointSourceCheckBox.setText(_translate("singleLaunchSetupDialog", "Point Source"))
        self.transducerSizeLabel.setText(_translate("singleLaunchSetupDialog", "Transducer Size (mm)"))
        self.centerOffsetLabel.setToolTip(_translate("singleLaunchSetupDialog", "<html><head/><body><p>Offset measured from the center of the Scenario along the x-axis. Positive values indicate offsets toward the right while negatives values indicate offsets toward the left.</p></body></html>"))
        self.centerOffsetLabel.setText(_translate("singleLaunchSetupDialog", "Center Offset (mm)"))
        self.centerOffsetLineEdit.setToolTip(_translate("singleLaunchSetupDialog", "<html><head/><body><p>Offset measured from the center of the Scenario along the x-axis. Positive values indicate offsets toward the right while negatives values indicate offsets toward the left.</p></body></html>"))
        self.borderOffsetLabel.setToolTip(_translate("singleLaunchSetupDialog", "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt;\">Border Offset is measured taking into account the top border as origin. Only positive values are allowed that indicates offsets towards below.</span><br/><img src=\":/helperBorderOffset.png\"/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p></body></html>"))
        self.borderOffsetLabel.setText(_translate("singleLaunchSetupDialog", "Border Offset (mm)"))
        self.borderOffsetLineEdit.setToolTip(_translate("singleLaunchSetupDialog", "<html><head/><body><p align=\"justify\"><span style=\" font-size:14pt;\">Border Offset is measured taking into account the top border as origin. Only positive values are allowed that indicates offsets towards below.</span><br/><img src=\":/helperBorderOffset.png\"/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p></body></html>"))
        self.previewPushButton.setText(_translate("singleLaunchSetupDialog", "Preview Transducer Setup"))
        self.advancedParametersSetupPushButton.setText(_translate("singleLaunchSetupDialog", "Advanced Parameters Setup"))
        self.signalSetupPushButton.setText(_translate("singleLaunchSetupDialog", "Signal Parameters"))

import SimNDT.gui.resources_rc

