# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(996, 702)
        Form.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 6, 18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget_2.setStyleSheet("font: 10pt \"微软雅黑\";\n"
"background-color: rgb(240, 240, 240);")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(31, -95, 65, 25))
        self.label_16.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_16.setObjectName("label_16")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 10, 311, 93))
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_4.setContentsMargins(18, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Si = QtWidgets.QRadioButton(self.groupBox_7)
        self.Si.setChecked(True)
        self.Si.setObjectName("Si")
        self.gridLayout_3.addWidget(self.Si, 0, 0, 1, 1)
        self.Ge = QtWidgets.QRadioButton(self.groupBox_7)
        self.Ge.setObjectName("Ge")
        self.gridLayout_3.addWidget(self.Ge, 0, 1, 1, 1)
        self.GaAs = QtWidgets.QRadioButton(self.groupBox_7)
        self.GaAs.setObjectName("GaAs")
        self.gridLayout_3.addWidget(self.GaAs, 1, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 110, 321, 131))
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_2.setContentsMargins(18, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_10)
        self.label_9.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.ni = QtWidgets.QLineEdit(self.groupBox_10)
        self.ni.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ni.setObjectName("ni")
        self.gridLayout_2.addWidget(self.ni, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_10)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_10)
        self.label_20.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 1, 0, 1, 1)
        self.Eg = QtWidgets.QLineEdit(self.groupBox_10)
        self.Eg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Eg.setObjectName("Eg")
        self.gridLayout_2.addWidget(self.Eg, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_10)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 1, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_10)
        self.label_19.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)
        self.es = QtWidgets.QLineEdit(self.groupBox_10)
        self.es.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.es.setObjectName("es")
        self.gridLayout_2.addWidget(self.es, 2, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_10)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 2, 2, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 10, 311, 91))
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_8)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.Nd = QtWidgets.QLineEdit(self.groupBox_8)
        self.Nd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Nd.setObjectName("Nd")
        self.gridLayout_4.addWidget(self.Nd, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_8)
        self.label_21.setStyleSheet("")
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 0, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox_8)
        self.label_34.setStyleSheet("")
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 1, 0, 1, 1)
        self.Na = QtWidgets.QLineEdit(self.groupBox_8)
        self.Na.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Na.setObjectName("Na")
        self.gridLayout_4.addWidget(self.Na, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_8)
        self.label_24.setStyleSheet("")
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 1, 2, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 100, 311, 141))
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_18 = QtWidgets.QLabel(self.groupBox_9)
        self.label_18.setStyleSheet("")
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 1)
        self.Dn = QtWidgets.QLineEdit(self.groupBox_9)
        self.Dn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Dn.setObjectName("Dn")
        self.gridLayout_5.addWidget(self.Dn, 0, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_9)
        self.label_35.setStyleSheet("")
        self.label_35.setObjectName("label_35")
        self.gridLayout_5.addWidget(self.label_35, 1, 0, 1, 1)
        self.Dp = QtWidgets.QLineEdit(self.groupBox_9)
        self.Dp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Dp.setObjectName("Dp")
        self.gridLayout_5.addWidget(self.Dp, 1, 1, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox_9)
        self.label_36.setStyleSheet("")
        self.label_36.setObjectName("label_36")
        self.gridLayout_5.addWidget(self.label_36, 2, 0, 1, 1)
        self.tn0 = QtWidgets.QLineEdit(self.groupBox_9)
        self.tn0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tn0.setObjectName("tn0")
        self.gridLayout_5.addWidget(self.tn0, 2, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.groupBox_9)
        self.label_37.setStyleSheet("")
        self.label_37.setObjectName("label_37")
        self.gridLayout_5.addWidget(self.label_37, 3, 0, 1, 1)
        self.tp0 = QtWidgets.QLineEdit(self.groupBox_9)
        self.tp0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tp0.setObjectName("tp0")
        self.gridLayout_5.addWidget(self.tp0, 3, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 10, 321, 131))
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_6.setContentsMargins(12, -1, 13, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_39 = QtWidgets.QLabel(self.groupBox_11)
        self.label_39.setStyleSheet("")
        self.label_39.setObjectName("label_39")
        self.gridLayout_6.addWidget(self.label_39, 0, 0, 1, 1)
        self.LLp = QtWidgets.QLineEdit(self.groupBox_11)
        self.LLp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LLp.setObjectName("LLp")
        self.gridLayout_6.addWidget(self.LLp, 0, 1, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.groupBox_11)
        self.label_43.setStyleSheet("")
        self.label_43.setObjectName("label_43")
        self.gridLayout_6.addWidget(self.label_43, 0, 2, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.groupBox_11)
        self.label_40.setStyleSheet("")
        self.label_40.setObjectName("label_40")
        self.gridLayout_6.addWidget(self.label_40, 1, 0, 1, 1)
        self.LLn = QtWidgets.QLineEdit(self.groupBox_11)
        self.LLn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LLn.setObjectName("LLn")
        self.gridLayout_6.addWidget(self.LLn, 1, 1, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.groupBox_11)
        self.label_44.setStyleSheet("")
        self.label_44.setObjectName("label_44")
        self.gridLayout_6.addWidget(self.label_44, 1, 2, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.groupBox_11)
        self.label_41.setStyleSheet("")
        self.label_41.setObjectName("label_41")
        self.gridLayout_6.addWidget(self.label_41, 2, 0, 1, 1)
        self.Va = QtWidgets.QLineEdit(self.groupBox_11)
        self.Va.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Va.setObjectName("Va")
        self.gridLayout_6.addWidget(self.Va, 2, 1, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.groupBox_11)
        self.label_45.setStyleSheet("")
        self.label_45.setObjectName("label_45")
        self.gridLayout_6.addWidget(self.label_45, 2, 2, 1, 1)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_6.setGeometry(QtCore.QRect(9, 9, 311, 211))
        self.groupBox_6.setStyleSheet("font: 75 10pt \"微软雅黑\";\n"
"border-color: rgb(255, 170, 0);")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setContentsMargins(28, -1, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Ge_2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.Ge_2.setChecked(True)
        self.Ge_2.setObjectName("Ge_2")
        self.verticalLayout_8.addWidget(self.Ge_2)
        self.Ge_3 = QtWidgets.QRadioButton(self.groupBox_6)
        self.Ge_3.setObjectName("Ge_3")
        self.verticalLayout_8.addWidget(self.Ge_3)
        self.Ge_4 = QtWidgets.QRadioButton(self.groupBox_6)
        self.Ge_4.setObjectName("Ge_4")
        self.verticalLayout_8.addWidget(self.Ge_4)
        self.Ge_5 = QtWidgets.QRadioButton(self.groupBox_6)
        self.Ge_5.setObjectName("Ge_5")
        self.verticalLayout_8.addWidget(self.Ge_5)
        self.Ge_6 = QtWidgets.QRadioButton(self.groupBox_6)
        self.Ge_6.setObjectName("Ge_6")
        self.verticalLayout_8.addWidget(self.Ge_6)
        self.Ge_7 = QtWidgets.QRadioButton(self.groupBox_6)
        self.Ge_7.setObjectName("Ge_7")
        self.verticalLayout_8.addWidget(self.Ge_7)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.verticalLayout_7.addWidget(self.tabWidget_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.np0 = QtWidgets.QLineEdit(self.groupBox)
        self.np0.setObjectName("np0")
        self.gridLayout.addWidget(self.np0, 4, 1, 1, 1)
        self.Emax = QtWidgets.QLineEdit(self.groupBox)
        self.Emax.setObjectName("Emax")
        self.gridLayout.addWidget(self.Emax, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.Emax1 = QtWidgets.QLabel(self.groupBox)
        self.Emax1.setObjectName("Emax1")
        self.gridLayout.addWidget(self.Emax1, 2, 0, 1, 1)
        self.pn0 = QtWidgets.QLineEdit(self.groupBox)
        self.pn0.setObjectName("pn0")
        self.gridLayout.addWidget(self.pn0, 3, 1, 1, 1)
        self.Vbi = QtWidgets.QLineEdit(self.groupBox)
        self.Vbi.setObjectName("Vbi")
        self.gridLayout.addWidget(self.Vbi, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.Xp = QtWidgets.QLineEdit(self.groupBox)
        self.Xp.setObjectName("Xp")
        self.gridLayout.addWidget(self.Xp, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.Xn = QtWidgets.QLineEdit(self.groupBox)
        self.Xn.setObjectName("Xn")
        self.gridLayout.addWidget(self.Xn, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 6)
        self.gridLayout.setColumnStretch(2, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 6, -1, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("image: url(:/pn/pic/logo.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(2, 6)
        self.verticalLayout.setStretch(3, 2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 17)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(40, 40, 341, 191))
        self.label_25.setStyleSheet("\n"
"image: url(:/pn/pic/BJT1.png);")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 181, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_1.setGeometry(QtCore.QRect(40, 90, 181, 41))
        self.pushButton_1.setObjectName("pushButton_1")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(240, 90, 181, 45))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_1.setObjectName("radioButton_1")
        self.horizontalLayout_2.addWidget(self.radioButton_1)
        self.runButton = QtWidgets.QPushButton(self.groupBox_4)
        self.runButton.setGeometry(QtCore.QRect(440, 30, 131, 91))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.runButton.setFont(font)
        self.runButton.setStyleSheet("font: 75 16pt \"微软雅黑\";\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.runButton.setObjectName("runButton")
        self.exit = QtWidgets.QPushButton(self.groupBox_4)
        self.exit.setGeometry(QtCore.QRect(240, 30, 181, 41))
        self.exit.setObjectName("exit")
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.verticalLayout_6.setStretch(0, 15)
        self.verticalLayout_6.setStretch(1, 5)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 5)

        self.retranslateUi(Form)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "半导体器件仿真平台-BJT"))
        self.groupBox_2.setTitle(_translate("Form", "参数设置"))
        self.label_16.setText(_translate("Form", "  Xn： "))
        self.groupBox_7.setTitle(_translate("Form", "材料"))
        self.Si.setText(_translate("Form", "硅（Si）"))
        self.Ge.setText(_translate("Form", "锗（Ge）"))
        self.GaAs.setText(_translate("Form", "砷化镓（GaAs）"))
        self.groupBox_10.setTitle(_translate("Form", "材料参数"))
        self.label_9.setText(_translate("Form", " ni： "))
        self.ni.setText(_translate("Form", "1.5 * (10 ** 10)"))
        self.ni.setPlaceholderText(_translate("Form", "  本征载流子浓度"))
        self.label_17.setText(_translate("Form", "  /cm^-3 "))
        self.label_20.setText(_translate("Form", " Eg： "))
        self.Eg.setText(_translate("Form", "1.12"))
        self.Eg.setPlaceholderText(_translate("Form", "  禁带宽度"))
        self.label_22.setText(_translate("Form", "  eV"))
        self.label_19.setText(_translate("Form", "介电常数： "))
        self.es.setText(_translate("Form", "11.7 * 8.85 * 10 ** (-14)"))
        self.es.setPlaceholderText(_translate("Form", "  介电常数"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Form", "materials"))
        self.groupBox_8.setTitle(_translate("Form", "掺杂浓度"))
        self.label.setText(_translate("Form", "Nd："))
        self.Nd.setText(_translate("Form", "2 * (10 ** 16)"))
        self.label_21.setText(_translate("Form", "  /cm^-3 "))
        self.label_34.setText(_translate("Form", "Na："))
        self.Na.setText(_translate("Form", "2 * (10 ** 16)"))
        self.label_24.setText(_translate("Form", "  /cm^-3 "))
        self.groupBox_9.setTitle(_translate("Form", "材料参数"))
        self.label_18.setText(_translate("Form", "Dn: "))
        self.Dn.setText(_translate("Form", "25"))
        self.label_35.setText(_translate("Form", "Dp: "))
        self.Dp.setText(_translate("Form", "10"))
        self.label_36.setText(_translate("Form", "tn0: "))
        self.tn0.setText(_translate("Form", "1 * (10 ** (-7))"))
        self.label_37.setText(_translate("Form", "tp0: "))
        self.tp0.setText(_translate("Form", "5 * (10 ** (-7))"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "doping"))
        self.groupBox_11.setTitle(_translate("Form", "结构参数"))
        self.label_39.setText(_translate("Form", "P-type length："))
        self.LLp.setText(_translate("Form", "0.5 * 10 ** (-4)"))
        self.label_43.setText(_translate("Form", "CM"))
        self.label_40.setText(_translate("Form", "N-type length："))
        self.LLn.setText(_translate("Form", "0.5 * 10 ** (-4)"))
        self.label_44.setText(_translate("Form", "CM"))
        self.label_41.setText(_translate("Form", "反偏电压："))
        self.Va.setText(_translate("Form", "-0.3"))
        self.label_45.setText(_translate("Form", "V"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Form", "structure"))
        self.groupBox_6.setTitle(_translate("Form", "仿真项目"))
        self.Ge_2.setText(_translate("Form", "Qp 均匀掺杂pn结空间电荷区电势"))
        self.Ge_3.setText(_translate("Form", "Ep 均匀掺杂pn结空间电荷区电场"))
        self.Ge_4.setText(_translate("Form", "Pp 突变pn结空间电荷密度"))
        self.Ge_5.setText(_translate("Form", "IV pn结二极管的理想I-V特性"))
        self.Ge_6.setText(_translate("Form", "ND pn结内部能带图"))
        self.Ge_7.setText(_translate("Form", "正偏条件下pn结内部的稳态少子浓度"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("Form", "Item_Sim"))
        self.pushButton_2.setText(_translate("Form", "快速运算"))
        self.groupBox.setTitle(_translate("Form", "输出结果"))
        self.label_11.setText(_translate("Form", "  CM"))
        self.label_14.setText(_translate("Form", "  /cm^-3 "))
        self.label_13.setText(_translate("Form", "  /cm^-3 "))
        self.label_12.setText(_translate("Form", "  V/CM"))
        self.label_15.setText(_translate("Form", "   V"))
        self.label_10.setText(_translate("Form", "  CM"))
        self.label_3.setText(_translate("Form", "  Xn： "))
        self.np0.setPlaceholderText(_translate("Form", "  p区少子浓度"))
        self.Emax.setPlaceholderText(_translate("Form", "  空间电荷区最大场强"))
        self.label_8.setText(_translate("Form", "  Vbi :"))
        self.label_6.setText(_translate("Form", "  Np0 :"))
        self.Emax1.setText(_translate("Form", "  Emax："))
        self.pn0.setPlaceholderText(_translate("Form", "  n区少子浓度"))
        self.Vbi.setPlaceholderText(_translate("Form", "  内建电场"))
        self.label_7.setText(_translate("Form", "  Pn0："))
        self.Xp.setPlaceholderText(_translate("Form", "  p区空间电荷区宽度"))
        self.label_4.setText(_translate("Form", "  Xp："))
        self.Xn.setPlaceholderText(_translate("Form", "  n区空间电荷区宽度"))
        self.groupBox_3.setTitle(_translate("Form", "主程序"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "仿真结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "器件文档"))
        self.groupBox_4.setTitle(_translate("Form", "功能按钮"))
        self.pushButton.setText(_translate("Form", "清空画布"))
        self.pushButton_1.setText(_translate("Form", "保存图像"))
        self.radioButton.setText(_translate("Form", "100dpi"))
        self.radioButton_1.setText(_translate("Form", "300dpi"))
        self.runButton.setText(_translate("Form", "开始仿真"))
        self.exit.setText(_translate("Form", "退出系统"))

import PN_rc
