# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './../UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 895)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1081, 861))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Menu_1 = QtWidgets.QWidget()
        self.Menu_1.setObjectName("Menu_1")
        self.Menu_1_tableWidget = QtWidgets.QTableWidget(self.Menu_1)
        self.Menu_1_tableWidget.setGeometry(QtCore.QRect(30, 440, 1001, 341))
        self.Menu_1_tableWidget.setRowCount(10)
        self.Menu_1_tableWidget.setColumnCount(20)
        self.Menu_1_tableWidget.setObjectName("Menu_1_tableWidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Menu_1)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 160, 351, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Menu_1_radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.Menu_1_radioButton_2.setObjectName("Menu_1_radioButton_2")
        self.gridLayout_2.addWidget(self.Menu_1_radioButton_2, 2, 0, 1, 1)
        self.Menu_1_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Menu_1_pushButton.setObjectName("Menu_1_pushButton")
        self.gridLayout_2.addWidget(self.Menu_1_pushButton, 3, 0, 1, 1)
        self.Menu_1_radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.Menu_1_radioButton.setChecked(True)
        self.Menu_1_radioButton.setObjectName("Menu_1_radioButton")
        self.gridLayout_2.addWidget(self.Menu_1_radioButton, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.Menu_1)
        self.label.setGeometry(QtCore.QRect(42, 90, 741, 61))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.Menu_1, "")
        self.Menu_2 = QtWidgets.QWidget()
        self.Menu_2.setObjectName("Menu_2")
        self.frame = QtWidgets.QFrame(self.Menu_2)
        self.frame.setGeometry(QtCore.QRect(10, 20, 1041, 771))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 491, 258))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Menu_2_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Menu_2_label.setObjectName("Menu_2_label")
        self.verticalLayout.addWidget(self.Menu_2_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Menu_2_textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.Menu_2_textEdit.setObjectName("Menu_2_textEdit")
        self.verticalLayout.addWidget(self.Menu_2_textEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.Menu_2_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Menu_2_button.setObjectName("Menu_2_button")
        self.verticalLayout.addWidget(self.Menu_2_button)
        self.Menu_2_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Menu_2_label_2.setText("")
        self.Menu_2_label_2.setObjectName("Menu_2_label_2")
        self.verticalLayout.addWidget(self.Menu_2_label_2)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 399, 1001, 361))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Menu_2_tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget_3)
        self.Menu_2_tableWidget.setRowCount(10)
        self.Menu_2_tableWidget.setColumnCount(20)
        self.Menu_2_tableWidget.setObjectName("Menu_2_tableWidget")
        self.gridLayout_3.addWidget(self.Menu_2_tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Menu_2, "")
        self.Menu_3 = QtWidgets.QWidget()
        self.Menu_3.setObjectName("Menu_3")
        self.Menu_3_tableWidget = QtWidgets.QTableWidget(self.Menu_3)
        self.Menu_3_tableWidget.setGeometry(QtCore.QRect(40, 440, 1001, 341))
        self.Menu_3_tableWidget.setRowCount(10)
        self.Menu_3_tableWidget.setColumnCount(20)
        self.Menu_3_tableWidget.setObjectName("Menu_3_tableWidget")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.Menu_3)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(290, 80, 211, 91))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Menu_3_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.Menu_3_comboBox.setObjectName("Menu_3_comboBox")
        self.gridLayout_4.addWidget(self.Menu_3_comboBox, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.Menu_3)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 391, 41))
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.Menu_3)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(40, 80, 231, 91))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Menu_3_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.Menu_3_lineEdit.setObjectName("Menu_3_lineEdit")
        self.gridLayout_5.addWidget(self.Menu_3_lineEdit, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.Menu_3)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(530, 80, 311, 91))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)
        self.Menu_3_dateTimeEdit = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_6)
        self.Menu_3_dateTimeEdit.setObjectName("Menu_3_dateTimeEdit")
        self.gridLayout_6.addWidget(self.Menu_3_dateTimeEdit, 1, 0, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.Menu_3)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(40, 190, 271, 91))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Menu_3_checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget_7)
        self.Menu_3_checkBox.setObjectName("Menu_3_checkBox")
        self.gridLayout_7.addWidget(self.Menu_3_checkBox, 1, 0, 1, 1)
        self.Menu_3_label_error = QtWidgets.QLabel(self.Menu_3)
        self.Menu_3_label_error.setGeometry(QtCore.QRect(40, 370, 721, 51))
        self.Menu_3_label_error.setText("")
        self.Menu_3_label_error.setObjectName("Menu_3_label_error")
        self.Menu_3_pushButton = QtWidgets.QPushButton(self.Menu_3)
        self.Menu_3_pushButton.setGeometry(QtCore.QRect(40, 310, 241, 41))
        self.Menu_3_pushButton.setObjectName("Menu_3_pushButton")
        self.tabWidget.addTab(self.Menu_3, "")
        self.Menu_4 = QtWidgets.QWidget()
        self.Menu_4.setObjectName("Menu_4")
        self.Menu_3_tableWidget_2 = QtWidgets.QTableWidget(self.Menu_4)
        self.Menu_3_tableWidget_2.setGeometry(QtCore.QRect(30, 430, 1001, 341))
        self.Menu_3_tableWidget_2.setRowCount(10)
        self.Menu_3_tableWidget_2.setColumnCount(20)
        self.Menu_3_tableWidget_2.setObjectName("Menu_3_tableWidget_2")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.Menu_4)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(30, 80, 291, 81))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_8)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_8.addWidget(self.comboBox, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.Menu_4)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 841, 51))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.Menu_4, "")
        self.Menu_5 = QtWidgets.QWidget()
        self.Menu_5.setObjectName("Menu_5")
        self.tabWidget.addTab(self.Menu_5, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayoutWidget.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spin Bike Gardens"))
        self.Menu_1_radioButton_2.setText(_translate("MainWindow", "Duration"))
        self.Menu_1_pushButton.setText(_translate("MainWindow", "Find"))
        self.Menu_1_radioButton.setText(_translate("MainWindow", "Number of Users"))
        self.label.setText(_translate("MainWindow", "Find the buildings in which  bikes that are used the most based on "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Menu_1), _translate("MainWindow", "Menu_1"))
        self.Menu_2_label.setText(_translate("MainWindow", "Email of bike user of have booked a bike"))
        self.Menu_2_button.setText(_translate("MainWindow", "Find"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Menu_2), _translate("MainWindow", "Menu_2"))
        self.label_3.setText(_translate("MainWindow", "Select brand"))
        self.label_2.setText(_translate("MainWindow", "Add a New Bike"))
        self.label_4.setText(_translate("MainWindow", "Serial Number"))
        self.label_5.setText(_translate("MainWindow", "Last time battery changed"))
        self.Menu_3_checkBox.setText(_translate("MainWindow", "Has Data Collector"))
        self.Menu_3_pushButton.setText(_translate("MainWindow", "Add Bike"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Menu_3), _translate("MainWindow", "Menu_3"))
        self.label_6.setText(_translate("MainWindow", "Select cartaker/admin"))
        self.label_7.setText(_translate("MainWindow", "Show all the unresolved ticekets issued by  a caretaker/admin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Menu_4), _translate("MainWindow", "Menu_4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Menu_5), _translate("MainWindow", "Menu_5"))

