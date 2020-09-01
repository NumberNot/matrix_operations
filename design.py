# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 220, 771, 331))
        self.tableView.setObjectName("tableView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 771, 180))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.line_file_pick = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_file_pick.setObjectName("line_file_pick")
        self.gridLayout.addWidget(self.line_file_pick, 0, 0, 1, 1)
        self.Button_pick_file = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Button_pick_file.setAutoDefault(True)
        self.Button_pick_file.setDefault(False)
        self.Button_pick_file.setFlat(False)
        self.Button_pick_file.setObjectName("Button_pick_file")
        self.gridLayout.addWidget(self.Button_pick_file, 0, 2, 1, 1)
        self.Button_save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Button_save.setObjectName("Button_save")
        self.gridLayout.addWidget(self.Button_save, 1, 2, 1, 1)
        self.line_file_save = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_file_save.setObjectName("line_file_save")
        self.gridLayout.addWidget(self.line_file_save, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_check_before = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_check_before.setObjectName("l_check_before")
        self.horizontalLayout_2.addWidget(self.l_check_before)
        self.l_check_before_result = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_check_before_result.setObjectName("l_check_before_result")
        self.horizontalLayout_2.addWidget(self.l_check_before_result)
        self.l_check_after = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_check_after.setObjectName("l_check_after")
        self.horizontalLayout_2.addWidget(self.l_check_after)
        self.l_check_after_result = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.l_check_after_result.setObjectName("l_check_after_result")
        self.horizontalLayout_2.addWidget(self.l_check_after_result)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.Button_check = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Button_check.setObjectName("Button_check")
        self.gridLayout.addWidget(self.Button_check, 2, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radio_auto = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radio_auto.setChecked(True)
        self.radio_auto.setObjectName("radio_auto")
        self.gridLayout_2.addWidget(self.radio_auto, 0, 0, 1, 1)
        self.radio_31 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radio_31.setObjectName("radio_31")
        self.gridLayout_2.addWidget(self.radio_31, 2, 0, 1, 1)
        self.radio_select = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radio_select.setObjectName("radio_select")
        self.gridLayout_2.addWidget(self.radio_select, 3, 0, 1, 1)
        self.radio_30 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radio_30.setObjectName("radio_30")
        self.gridLayout_2.addWidget(self.radio_30, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setMinimum(25)
        self.spinBox.setMaximum(35)
        self.spinBox.setProperty("value", 30)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transmute"))
        self.Button_pick_file.setText(_translate("MainWindow", "Pick File"))
        self.Button_save.setText(_translate("MainWindow", "Save to..."))
        self.l_check_before.setText(_translate("MainWindow", "Check Sum before"))
        self.l_check_before_result.setText(_translate("MainWindow", "0.0"))
        self.l_check_after.setText(_translate("MainWindow", "Check Sum after"))
        self.l_check_after_result.setText(_translate("MainWindow", "0.0"))
        self.Button_check.setText(_translate("MainWindow", "Check"))
        self.radio_auto.setText(_translate("MainWindow", "Auto"))
        self.radio_31.setText(_translate("MainWindow", "31"))
        self.radio_select.setText(_translate("MainWindow", "-->"))
        self.radio_30.setText(_translate("MainWindow", "30"))
