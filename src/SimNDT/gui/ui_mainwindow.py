# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Dec  4 20:19:06 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(742, 566)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(3000, 3000))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuConfiguration = QtGui.QMenu(self.menubar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        self.menuNew_Simulation_Scenario = QtGui.QMenu(self.menuConfiguration)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuNew_Simulation_Scenario.setIcon(icon)
        self.menuNew_Simulation_Scenario.setObjectName("menuNew_Simulation_Scenario")
        self.menuAdd_Microstructure = QtGui.QMenu(self.menuNew_Simulation_Scenario)
        self.menuAdd_Microstructure.setObjectName("menuAdd_Microstructure")
        self.menuInspection_Setup = QtGui.QMenu(self.menuConfiguration)
        self.menuInspection_Setup.setObjectName("menuInspection_Setup")
        self.menuPlotting_Tools = QtGui.QMenu(self.menubar)
        self.menuPlotting_Tools.setObjectName("menuPlotting_Tools")
        self.menuSingle_Launch_Inspections = QtGui.QMenu(self.menuPlotting_Tools)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/singleLaunch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSingle_Launch_Inspections.setIcon(icon1)
        self.menuSingle_Launch_Inspections.setObjectName("menuSingle_Launch_Inspections")
        self.menuLinear_Scan_Inspections = QtGui.QMenu(self.menuPlotting_Tools)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/linearScan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuLinear_Scan_Inspections.setIcon(icon2)
        self.menuLinear_Scan_Inspections.setObjectName("menuLinear_Scan_Inspections")
        self.menuTomography_Inspections = QtGui.QMenu(self.menuPlotting_Tools)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/tomoSetup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuTomography_Inspections.setIcon(icon3)
        self.menuTomography_Inspections.setObjectName("menuTomography_Inspections")
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMaterials_Setup = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/material.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMaterials_Setup.setIcon(icon4)
        self.actionMaterials_Setup.setObjectName("actionMaterials_Setup")
        self.actionBoundaty_Conditions_Setup = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/boundary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBoundaty_Conditions_Setup.setIcon(icon5)
        self.actionBoundaty_Conditions_Setup.setObjectName("actionBoundaty_Conditions_Setup")
        self.actionSimulation_Setup = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/simModel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSimulation_Setup.setIcon(icon6)
        self.actionSimulation_Setup.setObjectName("actionSimulation_Setup")
        self.actionRun_Simulation = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/runGL.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun_Simulation.setIcon(icon7)
        self.actionRun_Simulation.setObjectName("actionRun_Simulation")
        self.actionCreate_Video_from_Images = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/snapshots.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_Video_from_Images.setIcon(icon8)
        self.actionCreate_Video_from_Images.setObjectName("actionCreate_Video_from_Images")
        self.actionNew_Geometry_Model = QtGui.QAction(MainWindow)
        self.actionNew_Geometry_Model.setIcon(icon)
        self.actionNew_Geometry_Model.setObjectName("actionNew_Geometry_Model")
        self.actionAdd_Ellipse = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/ellipse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Ellipse.setIcon(icon9)
        self.actionAdd_Ellipse.setObjectName("actionAdd_Ellipse")
        self.actionAdd_Rectangle = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Rectangle.setIcon(icon10)
        self.actionAdd_Rectangle.setObjectName("actionAdd_Rectangle")
        self.actionLoad_Scenario_From_Image = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/loadImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad_Scenario_From_Image.setIcon(icon11)
        self.actionLoad_Scenario_From_Image.setObjectName("actionLoad_Scenario_From_Image")
        self.actionPreview_Labeled_Scenario = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/previewImage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreview_Labeled_Scenario.setIcon(icon12)
        self.actionPreview_Labeled_Scenario.setObjectName("actionPreview_Labeled_Scenario")
        self.actionSingle_Launch_Inspection = QtGui.QAction(MainWindow)
        self.actionSingle_Launch_Inspection.setCheckable(True)
        self.actionSingle_Launch_Inspection.setIcon(icon1)
        self.actionSingle_Launch_Inspection.setObjectName("actionSingle_Launch_Inspection")
        self.actionLinear_Scan_Inspections = QtGui.QAction(MainWindow)
        self.actionLinear_Scan_Inspections.setCheckable(True)
        self.actionLinear_Scan_Inspections.setIcon(icon2)
        self.actionLinear_Scan_Inspections.setObjectName("actionLinear_Scan_Inspections")
        self.actionTomography_Inspections = QtGui.QAction(MainWindow)
        self.actionTomography_Inspections.setCheckable(True)
        self.actionTomography_Inspections.setIcon(icon3)
        self.actionTomography_Inspections.setObjectName("actionTomography_Inspections")
        self.actionRotate_The_Scenario_90_Clockwise = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/rotate90H.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRotate_The_Scenario_90_Clockwise.setIcon(icon13)
        self.actionRotate_The_Scenario_90_Clockwise.setObjectName("actionRotate_The_Scenario_90_Clockwise")
        self.actionRotate_The_Scenario_90_Counter_Clockwise = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/rotate90A.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRotate_The_Scenario_90_Counter_Clockwise.setIcon(icon14)
        self.actionRotate_The_Scenario_90_Counter_Clockwise.setObjectName("actionRotate_The_Scenario_90_Counter_Clockwise")
        self.actionCheck_Simulation_Setup = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/check3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCheck_Simulation_Setup.setIcon(icon15)
        self.actionCheck_Simulation_Setup.setObjectName("actionCheck_Simulation_Setup")
        self.actionPlot_Receiver_Signals_SingleLaunch = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/signal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot_Receiver_Signals_SingleLaunch.setIcon(icon16)
        self.actionPlot_Receiver_Signals_SingleLaunch.setObjectName("actionPlot_Receiver_Signals_SingleLaunch")
        self.actionPlot_Receiver_Signals_Spectra = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/fft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot_Receiver_Signals_Spectra.setIcon(icon17)
        self.actionPlot_Receiver_Signals_Spectra.setObjectName("actionPlot_Receiver_Signals_Spectra")
        self.actionPlot_Receivers_Signals_LinearScan = QtGui.QAction(MainWindow)
        self.actionPlot_Receivers_Signals_LinearScan.setIcon(icon16)
        self.actionPlot_Receivers_Signals_LinearScan.setObjectName("actionPlot_Receivers_Signals_LinearScan")
        self.actionPlot_Receivers_Signals_Tomography = QtGui.QAction(MainWindow)
        self.actionPlot_Receivers_Signals_Tomography.setIcon(icon16)
        self.actionPlot_Receivers_Signals_Tomography.setObjectName("actionPlot_Receivers_Signals_Tomography")
        self.actionAdd_Two_Phase_Concrete_Microstructure = QtGui.QAction(MainWindow)
        self.actionAdd_Two_Phase_Concrete_Microstructure.setObjectName("actionAdd_Two_Phase_Concrete_Microstructure")
        self.actionAdd_Three_Phase_Concrete_Microstructure = QtGui.QAction(MainWindow)
        self.actionAdd_Three_Phase_Concrete_Microstructure.setObjectName("actionAdd_Three_Phase_Concrete_Microstructure")
        self.actionTwo_Phase_Model_Dry_Case = QtGui.QAction(MainWindow)
        self.actionTwo_Phase_Model_Dry_Case.setObjectName("actionTwo_Phase_Model_Dry_Case")
        self.actionThree_Phase_Model_Dry_Case = QtGui.QAction(MainWindow)
        self.actionThree_Phase_Model_Dry_Case.setObjectName("actionThree_Phase_Model_Dry_Case")
        self.actionTwo_Phase_Model_Immersion_Case = QtGui.QAction(MainWindow)
        self.actionTwo_Phase_Model_Immersion_Case.setObjectName("actionTwo_Phase_Model_Immersion_Case")
        self.actionThree_Phase_Model_Immersion_Case = QtGui.QAction(MainWindow)
        self.actionThree_Phase_Model_Immersion_Case.setObjectName("actionThree_Phase_Model_Immersion_Case")
        self.menuAdd_Microstructure.addAction(self.actionTwo_Phase_Model_Dry_Case)
        self.menuAdd_Microstructure.addAction(self.actionThree_Phase_Model_Dry_Case)
        self.menuAdd_Microstructure.addSeparator()
        self.menuAdd_Microstructure.addAction(self.actionTwo_Phase_Model_Immersion_Case)
        self.menuAdd_Microstructure.addAction(self.actionThree_Phase_Model_Immersion_Case)
        self.menuNew_Simulation_Scenario.addAction(self.actionNew_Geometry_Model)
        self.menuNew_Simulation_Scenario.addSeparator()
        self.menuNew_Simulation_Scenario.addAction(self.actionAdd_Ellipse)
        self.menuNew_Simulation_Scenario.addAction(self.actionAdd_Rectangle)
        self.menuNew_Simulation_Scenario.addSeparator()
        self.menuNew_Simulation_Scenario.addAction(self.menuAdd_Microstructure.menuAction())
        self.menuNew_Simulation_Scenario.addSeparator()
        self.menuNew_Simulation_Scenario.addAction(self.actionLoad_Scenario_From_Image)
        self.menuNew_Simulation_Scenario.addAction(self.actionPreview_Labeled_Scenario)
        self.menuNew_Simulation_Scenario.addSeparator()
        self.menuInspection_Setup.addAction(self.actionSingle_Launch_Inspection)
        self.menuInspection_Setup.addAction(self.actionLinear_Scan_Inspections)
        self.menuInspection_Setup.addAction(self.actionTomography_Inspections)
        self.menuConfiguration.addAction(self.menuNew_Simulation_Scenario.menuAction())
        self.menuConfiguration.addAction(self.actionMaterials_Setup)
        self.menuConfiguration.addAction(self.actionBoundaty_Conditions_Setup)
        self.menuConfiguration.addAction(self.menuInspection_Setup.menuAction())
        self.menuConfiguration.addAction(self.actionSimulation_Setup)
        self.menuConfiguration.addAction(self.actionCheck_Simulation_Setup)
        self.menuConfiguration.addSeparator()
        self.menuConfiguration.addAction(self.actionRun_Simulation)
        self.menuConfiguration.addSeparator()
        self.menuConfiguration.addSeparator()
        self.menuSingle_Launch_Inspections.addAction(self.actionPlot_Receiver_Signals_SingleLaunch)
        self.menuSingle_Launch_Inspections.addAction(self.actionPlot_Receiver_Signals_Spectra)
        self.menuLinear_Scan_Inspections.addAction(self.actionPlot_Receivers_Signals_LinearScan)
        self.menuTomography_Inspections.addAction(self.actionPlot_Receivers_Signals_Tomography)
        self.menuPlotting_Tools.addAction(self.menuSingle_Launch_Inspections.menuAction())
        self.menuPlotting_Tools.addAction(self.menuLinear_Scan_Inspections.menuAction())
        self.menuPlotting_Tools.addAction(self.menuTomography_Inspections.menuAction())
        self.menuPlotting_Tools.addSeparator()
        self.menuTools.addAction(self.actionCreate_Video_from_Images)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuPlotting_Tools.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SimNDT", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConfiguration.setTitle(QtGui.QApplication.translate("MainWindow", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNew_Simulation_Scenario.setToolTip(QtGui.QApplication.translate("MainWindow", "New Scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNew_Simulation_Scenario.setStatusTip(QtGui.QApplication.translate("MainWindow", "New Scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNew_Simulation_Scenario.setTitle(QtGui.QApplication.translate("MainWindow", "New Simulation Scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdd_Microstructure.setTitle(QtGui.QApplication.translate("MainWindow", "Add Concrete Microstructure Model", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInspection_Setup.setTitle(QtGui.QApplication.translate("MainWindow", "Inspection Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlotting_Tools.setTitle(QtGui.QApplication.translate("MainWindow", "Plotting Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSingle_Launch_Inspections.setTitle(QtGui.QApplication.translate("MainWindow", "Single Launch Inspections", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLinear_Scan_Inspections.setTitle(QtGui.QApplication.translate("MainWindow", "Linear Scan Inspections", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTomography_Inspections.setTitle(QtGui.QApplication.translate("MainWindow", "Tomography Inspections", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMaterials_Setup.setText(QtGui.QApplication.translate("MainWindow", "Materials Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMaterials_Setup.setStatusTip(QtGui.QApplication.translate("MainWindow", "Materials Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBoundaty_Conditions_Setup.setText(QtGui.QApplication.translate("MainWindow", "Boundary Conditions Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBoundaty_Conditions_Setup.setStatusTip(QtGui.QApplication.translate("MainWindow", "Boundary Conditions Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSimulation_Setup.setText(QtGui.QApplication.translate("MainWindow", "Simulation Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_Simulation.setText(QtGui.QApplication.translate("MainWindow", "Run Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_Simulation.setStatusTip(QtGui.QApplication.translate("MainWindow", "Run_Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_Simulation.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+Alt+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_Video_from_Images.setText(QtGui.QApplication.translate("MainWindow", "Create Video from Images", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_Video_from_Images.setStatusTip(QtGui.QApplication.translate("MainWindow", "Create Video from Images", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Geometry_Model.setText(QtGui.QApplication.translate("MainWindow", "New Geometry Model", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Geometry_Model.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+Alt+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Ellipse.setText(QtGui.QApplication.translate("MainWindow", "Add Ellipse", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Ellipse.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add Ellipse", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Ellipse.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+Alt+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Rectangle.setText(QtGui.QApplication.translate("MainWindow", "Add Rectangle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Rectangle.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add Rectangle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Rectangle.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+Alt+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Scenario_From_Image.setText(QtGui.QApplication.translate("MainWindow", "Load Scenario From Image", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Scenario_From_Image.setStatusTip(QtGui.QApplication.translate("MainWindow", "Load Scenario From Image", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_Scenario_From_Image.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+Alt+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview_Labeled_Scenario.setText(QtGui.QApplication.translate("MainWindow", "Preview Labeled Scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview_Labeled_Scenario.setStatusTip(QtGui.QApplication.translate("MainWindow", "Preview Labeled Scenario", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreview_Labeled_Scenario.setShortcut(QtGui.QApplication.translate("MainWindow", "Meta+Alt+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSingle_Launch_Inspection.setText(QtGui.QApplication.translate("MainWindow", "Single Launch Inspection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSingle_Launch_Inspection.setStatusTip(QtGui.QApplication.translate("MainWindow", "Single Launch Inspection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLinear_Scan_Inspections.setText(QtGui.QApplication.translate("MainWindow", "Linear Scan Inspections", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTomography_Inspections.setText(QtGui.QApplication.translate("MainWindow", "Tomography Inspections", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRotate_The_Scenario_90_Clockwise.setText(QtGui.QApplication.translate("MainWindow", "Rotate The Scenario 90º Clockwise", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRotate_The_Scenario_90_Clockwise.setToolTip(QtGui.QApplication.translate("MainWindow", "Rotate The Scenario 90º Clockwise", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRotate_The_Scenario_90_Counter_Clockwise.setText(QtGui.QApplication.translate("MainWindow", "Rotate The Scenario 90º Counter Clockwise", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRotate_The_Scenario_90_Counter_Clockwise.setToolTip(QtGui.QApplication.translate("MainWindow", "Rotate The Scenario 90º Counter Clockwise", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_Simulation_Setup.setText(QtGui.QApplication.translate("MainWindow", "Check Simulation Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlot_Receiver_Signals_SingleLaunch.setText(QtGui.QApplication.translate("MainWindow", "Plot Receiver Signals", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlot_Receiver_Signals_Spectra.setText(QtGui.QApplication.translate("MainWindow", "Plot Receiver Spectra", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlot_Receivers_Signals_LinearScan.setText(QtGui.QApplication.translate("MainWindow", "Plot Receivers Signals", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlot_Receivers_Signals_Tomography.setText(QtGui.QApplication.translate("MainWindow", "Plot Receivers Signals", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Two_Phase_Concrete_Microstructure.setText(QtGui.QApplication.translate("MainWindow", "Add Two-Phase Concrete Microstructure", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_Three_Phase_Concrete_Microstructure.setText(QtGui.QApplication.translate("MainWindow", "Add Three-Phase Concrete Microstructure", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTwo_Phase_Model_Dry_Case.setText(QtGui.QApplication.translate("MainWindow", "Two-Phase Model (Dry Case)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionThree_Phase_Model_Dry_Case.setText(QtGui.QApplication.translate("MainWindow", "Three-Phase Model (Dry Case)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTwo_Phase_Model_Immersion_Case.setText(QtGui.QApplication.translate("MainWindow", "Two-Phase Model (Immersion Case)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionThree_Phase_Model_Immersion_Case.setText(QtGui.QApplication.translate("MainWindow", "Three-Phase Model (Immersion Case)", None, QtGui.QApplication.UnicodeUTF8))


