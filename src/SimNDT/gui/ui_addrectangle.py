# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\addrectangle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addRectangleDialog(object):
    def setupUi(self, addRectangleDialog):
        addRectangleDialog.setObjectName("addRectangleDialog")
        addRectangleDialog.setWindowModality(QtCore.Qt.WindowModal)
        addRectangleDialog.resize(220, 258)
        addRectangleDialog.setMinimumSize(QtCore.QSize(220, 258))
        addRectangleDialog.setMaximumSize(QtCore.QSize(220, 258))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addRectangleDialog.setWindowIcon(icon)
        addRectangleDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        addRectangleDialog.setSizeGripEnabled(False)
        addRectangleDialog.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(addRectangleDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 220, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(addRectangleDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 181, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.centerXLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.centerXLabel.setObjectName("centerXLabel")
        self.gridLayout.addWidget(self.centerXLabel, 0, 0, 1, 1)
        self.centerXLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.centerXLineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.centerXLineEdit.setMaximumSize(QtCore.QSize(80, 21))
        self.centerXLineEdit.setObjectName("centerXLineEdit")
        self.gridLayout.addWidget(self.centerXLineEdit, 0, 1, 1, 1)
        self.centerYLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.centerYLabel.setObjectName("centerYLabel")
        self.gridLayout.addWidget(self.centerYLabel, 1, 0, 1, 1)
        self.centerYLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.centerYLineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.centerYLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.centerYLineEdit.setObjectName("centerYLineEdit")
        self.gridLayout.addWidget(self.centerYLineEdit, 1, 1, 1, 1)
        self.widthLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.widthLabel.setObjectName("widthLabel")
        self.gridLayout.addWidget(self.widthLabel, 2, 0, 1, 1)
        self.widthLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.widthLineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.widthLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.widthLineEdit.setObjectName("widthLineEdit")
        self.gridLayout.addWidget(self.widthLineEdit, 2, 1, 1, 1)
        self.heightLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.heightLabel.setObjectName("heightLabel")
        self.gridLayout.addWidget(self.heightLabel, 3, 0, 1, 1)
        self.heightLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.heightLineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.heightLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.heightLineEdit.setObjectName("heightLineEdit")
        self.gridLayout.addWidget(self.heightLineEdit, 3, 1, 1, 1)
        self.angleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.angleLabel.setObjectName("angleLabel")
        self.gridLayout.addWidget(self.angleLabel, 4, 0, 1, 1)
        self.angleLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.angleLineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.angleLineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.angleLineEdit.setObjectName("angleLineEdit")
        self.gridLayout.addWidget(self.angleLineEdit, 4, 1, 1, 1)
        self.labelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelLabel.setObjectName("labelLabel")
        self.gridLayout.addWidget(self.labelLabel, 5, 0, 1, 1)
        self.labelSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.labelSpinBox.setMaximum(240)
        self.labelSpinBox.setSingleStep(40)
        self.labelSpinBox.setObjectName("labelSpinBox")
        self.gridLayout.addWidget(self.labelSpinBox, 5, 1, 1, 1)

        self.retranslateUi(addRectangleDialog)
        self.buttonBox.accepted.connect(addRectangleDialog.accept)
        self.buttonBox.rejected.connect(addRectangleDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addRectangleDialog)

    def retranslateUi(self, addRectangleDialog):
        _translate = QtCore.QCoreApplication.translate
        addRectangleDialog.setWindowTitle(_translate("addRectangleDialog", "Add Rectangle"))
        addRectangleDialog.setToolTip(_translate("addRectangleDialog", "Add Rectangle"))
        addRectangleDialog.setStatusTip(_translate("addRectangleDialog", "Add Rectangle"))
        self.centerXLabel.setText(_translate("addRectangleDialog", "Center X (mm)"))
        self.centerXLineEdit.setToolTip(_translate("addRectangleDialog", "Center X"))
        self.centerXLineEdit.setStatusTip(_translate("addRectangleDialog", "Center X"))
        self.centerYLabel.setText(_translate("addRectangleDialog", "Center Y (mm)"))
        self.centerYLineEdit.setToolTip(_translate("addRectangleDialog", "Center Y"))
        self.centerYLineEdit.setStatusTip(_translate("addRectangleDialog", "Center Y"))
        self.widthLabel.setText(_translate("addRectangleDialog", "Width (mm)"))
        self.widthLineEdit.setToolTip(_translate("addRectangleDialog", "Width"))
        self.widthLineEdit.setStatusTip(_translate("addRectangleDialog", "Width"))
        self.heightLabel.setToolTip(_translate("addRectangleDialog", "Add Rectangle"))
        self.heightLabel.setStatusTip(_translate("addRectangleDialog", "Add Rectangle"))
        self.heightLabel.setText(_translate("addRectangleDialog", "Height (mm)"))
        self.heightLineEdit.setToolTip(_translate("addRectangleDialog", "Height"))
        self.heightLineEdit.setStatusTip(_translate("addRectangleDialog", "Height"))
        self.angleLabel.setText(_translate("addRectangleDialog", "Angle"))
        self.angleLineEdit.setToolTip(_translate("addRectangleDialog", "Angle"))
        self.angleLineEdit.setStatusTip(_translate("addRectangleDialog", "Angle"))
        self.labelLabel.setText(_translate("addRectangleDialog", "Label"))
        self.labelSpinBox.setToolTip(_translate("addRectangleDialog", "Label"))
        self.labelSpinBox.setStatusTip(_translate("addRectangleDialog", "Label"))

import SimNDT.gui.resources_rc

