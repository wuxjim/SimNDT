# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\materialsetup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_materialSetupDialog(object):
    def setupUi(self, materialSetupDialog):
        materialSetupDialog.setObjectName("materialSetupDialog")
        materialSetupDialog.resize(310, 520)
        materialSetupDialog.setMinimumSize(QtCore.QSize(310, 520))
        materialSetupDialog.setMaximumSize(QtCore.QSize(310, 520))
        materialSetupDialog.setFocusPolicy(QtCore.Qt.TabFocus)
        materialSetupDialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/material.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        materialSetupDialog.setWindowIcon(icon)
        self.firstFrame = QtWidgets.QFrame(materialSetupDialog)
        self.firstFrame.setGeometry(QtCore.QRect(10, 20, 291, 80))
        self.firstFrame.setFocusPolicy(QtCore.Qt.TabFocus)
        self.firstFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.firstFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.firstFrame.setObjectName("firstFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.firstFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.addMaterialPushButton = QtWidgets.QPushButton(self.firstFrame)
        self.addMaterialPushButton.setMaximumSize(QtCore.QSize(140, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addMaterialPushButton.setIcon(icon1)
        self.addMaterialPushButton.setObjectName("addMaterialPushButton")
        self.gridLayout_3.addWidget(self.addMaterialPushButton, 0, 0, 1, 1)
        self.deleteMaterialPushButton = QtWidgets.QPushButton(self.firstFrame)
        self.deleteMaterialPushButton.setMaximumSize(QtCore.QSize(140, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteMaterialPushButton.setIcon(icon2)
        self.deleteMaterialPushButton.setObjectName("deleteMaterialPushButton")
        self.gridLayout_3.addWidget(self.deleteMaterialPushButton, 0, 1, 1, 1)
        self.materialLibraryPushButton = QtWidgets.QPushButton(self.firstFrame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.materialLibraryPushButton.setIcon(icon3)
        self.materialLibraryPushButton.setObjectName("materialLibraryPushButton")
        self.gridLayout_3.addWidget(self.materialLibraryPushButton, 1, 0, 1, 2)
        self.secondFrame = QtWidgets.QFrame(materialSetupDialog)
        self.secondFrame.setGeometry(QtCore.QRect(10, 110, 291, 71))
        self.secondFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.secondFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.secondFrame.setObjectName("secondFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.secondFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.materialNumberlabel = QtWidgets.QLabel(self.secondFrame)
        self.materialNumberlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.materialNumberlabel.setObjectName("materialNumberlabel")
        self.gridLayout_2.addWidget(self.materialNumberlabel, 0, 0, 1, 1)
        self.materialNameLineEdit = QtWidgets.QLineEdit(self.secondFrame)
        self.materialNameLineEdit.setMinimumSize(QtCore.QSize(120, 0))
        self.materialNameLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.materialNameLineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.materialNameLineEdit.setObjectName("materialNameLineEdit")
        self.gridLayout_2.addWidget(self.materialNameLineEdit, 0, 1, 1, 1)
        self.previousPushButton = QtWidgets.QPushButton(self.secondFrame)
        self.previousPushButton.setMinimumSize(QtCore.QSize(130, 0))
        self.previousPushButton.setMaximumSize(QtCore.QSize(130, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousPushButton.setIcon(icon4)
        self.previousPushButton.setObjectName("previousPushButton")
        self.gridLayout_2.addWidget(self.previousPushButton, 1, 0, 1, 1)
        self.nextPushButton = QtWidgets.QPushButton(self.secondFrame)
        self.nextPushButton.setMinimumSize(QtCore.QSize(130, 0))
        self.nextPushButton.setMaximumSize(QtCore.QSize(130, 16777215))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextPushButton.setIcon(icon5)
        self.nextPushButton.setObjectName("nextPushButton")
        self.gridLayout_2.addWidget(self.nextPushButton, 1, 1, 1, 1)
        self.materialNumberlabel.raise_()
        self.previousPushButton.raise_()
        self.nextPushButton.raise_()
        self.materialNameLineEdit.raise_()
        self.propertiesFrame = QtWidgets.QFrame(materialSetupDialog)
        self.propertiesFrame.setGeometry(QtCore.QRect(10, 190, 290, 271))
        self.propertiesFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.propertiesFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.propertiesFrame.setObjectName("propertiesFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.propertiesFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.applyPushButton = QtWidgets.QPushButton(self.propertiesFrame)
        self.applyPushButton.setMinimumSize(QtCore.QSize(200, 32))
        self.applyPushButton.setMaximumSize(QtCore.QSize(200, 32))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/done.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.applyPushButton.setIcon(icon6)
        self.applyPushButton.setObjectName("applyPushButton")
        self.gridLayout.addWidget(self.applyPushButton, 3, 0, 1, 1)
        self.infoLabel = QtWidgets.QLabel(self.propertiesFrame)
        self.infoLabel.setObjectName("infoLabel")
        self.gridLayout.addWidget(self.infoLabel, 0, 1, 1, 1)
        self.dampimgCheckBox = QtWidgets.QCheckBox(self.propertiesFrame)
        self.dampimgCheckBox.setFocusPolicy(QtCore.Qt.TabFocus)
        self.dampimgCheckBox.setObjectName("dampimgCheckBox")
        self.gridLayout.addWidget(self.dampimgCheckBox, 1, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setObjectName("formLayout_2")
        self.etavLabel = QtWidgets.QLabel(self.propertiesFrame)
        self.etavLabel.setObjectName("etavLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.etavLabel)
        self.etavLineEdit = QtWidgets.QLineEdit(self.propertiesFrame)
        self.etavLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.etavLineEdit.setObjectName("etavLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.etavLineEdit)
        self.etasLabel = QtWidgets.QLabel(self.propertiesFrame)
        self.etasLabel.setObjectName("etasLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.etasLabel)
        self.etasLineEdit = QtWidgets.QLineEdit(self.propertiesFrame)
        self.etasLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.etasLineEdit.setObjectName("etasLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.etasLineEdit)
        self.gridLayout.addLayout(self.formLayout_2, 2, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.rhoLabel = QtWidgets.QLabel(self.propertiesFrame)
        self.rhoLabel.setObjectName("rhoLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rhoLabel)
        self.rhoLineEdit = QtWidgets.QLineEdit(self.propertiesFrame)
        self.rhoLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.rhoLineEdit.setObjectName("rhoLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rhoLineEdit)
        self.lambdaLabel = QtWidgets.QLabel(self.propertiesFrame)
        self.lambdaLabel.setObjectName("lambdaLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lambdaLabel)
        self.lambdaLineEdit = QtWidgets.QLineEdit(self.propertiesFrame)
        self.lambdaLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lambdaLineEdit.setObjectName("lambdaLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lambdaLineEdit)
        self.muLabel = QtWidgets.QLabel(self.propertiesFrame)
        self.muLabel.setObjectName("muLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.muLabel)
        self.muLineEdit = QtWidgets.QLineEdit(self.propertiesFrame)
        self.muLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.muLineEdit.setObjectName("muLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.muLineEdit)
        self.labelLabel = QtWidgets.QLabel(self.propertiesFrame)
        self.labelLabel.setObjectName("labelLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelLabel)
        self.labelSpinBox = QtWidgets.QSpinBox(self.propertiesFrame)
        self.labelSpinBox.setMaximum(240)
        self.labelSpinBox.setSingleStep(40)
        self.labelSpinBox.setObjectName("labelSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelSpinBox)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.okPushButton = QtWidgets.QPushButton(materialSetupDialog)
        self.okPushButton.setGeometry(QtCore.QRect(100, 470, 100, 32))
        self.okPushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.okPushButton.setObjectName("okPushButton")
        self.cancelPushButton = QtWidgets.QPushButton(materialSetupDialog)
        self.cancelPushButton.setGeometry(QtCore.QRect(200, 470, 100, 32))
        self.cancelPushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cancelPushButton.setObjectName("cancelPushButton")

        self.retranslateUi(materialSetupDialog)
        QtCore.QMetaObject.connectSlotsByName(materialSetupDialog)
        materialSetupDialog.setTabOrder(self.addMaterialPushButton, self.okPushButton)
        materialSetupDialog.setTabOrder(self.okPushButton, self.cancelPushButton)
        materialSetupDialog.setTabOrder(self.cancelPushButton, self.applyPushButton)
        materialSetupDialog.setTabOrder(self.applyPushButton, self.deleteMaterialPushButton)
        materialSetupDialog.setTabOrder(self.deleteMaterialPushButton, self.materialLibraryPushButton)
        materialSetupDialog.setTabOrder(self.materialLibraryPushButton, self.previousPushButton)
        materialSetupDialog.setTabOrder(self.previousPushButton, self.nextPushButton)
        materialSetupDialog.setTabOrder(self.nextPushButton, self.materialNameLineEdit)

    def retranslateUi(self, materialSetupDialog):
        _translate = QtCore.QCoreApplication.translate
        materialSetupDialog.setWindowTitle(_translate("materialSetupDialog", "Material Setup"))
        materialSetupDialog.setToolTip(_translate("materialSetupDialog", "Material Setup"))
        materialSetupDialog.setStatusTip(_translate("materialSetupDialog", "Material Setup"))
        self.addMaterialPushButton.setText(_translate("materialSetupDialog", "Add Material"))
        self.deleteMaterialPushButton.setText(_translate("materialSetupDialog", "Delete Material"))
        self.materialLibraryPushButton.setText(_translate("materialSetupDialog", "Material Library"))
        self.materialNumberlabel.setText(_translate("materialSetupDialog", "Material #"))
        self.materialNameLineEdit.setPlaceholderText(_translate("materialSetupDialog", "Material Name"))
        self.previousPushButton.setText(_translate("materialSetupDialog", "Previous"))
        self.nextPushButton.setText(_translate("materialSetupDialog", "Next"))
        self.applyPushButton.setText(_translate("materialSetupDialog", "Apply"))
        self.infoLabel.setText(_translate("materialSetupDialog", "TextLabel"))
        self.dampimgCheckBox.setText(_translate("materialSetupDialog", "Damping"))
        self.etavLabel.setText(_translate("materialSetupDialog", "etav"))
        self.etasLabel.setText(_translate("materialSetupDialog", "etas"))
        self.rhoLabel.setText(_translate("materialSetupDialog", "rho"))
        self.lambdaLabel.setText(_translate("materialSetupDialog", "lambda"))
        self.muLabel.setText(_translate("materialSetupDialog", "mu"))
        self.labelLabel.setText(_translate("materialSetupDialog", "Label"))
        self.okPushButton.setText(_translate("materialSetupDialog", "OK"))
        self.cancelPushButton.setText(_translate("materialSetupDialog", "Cancel"))

import SimNDT.gui.resources_rc

