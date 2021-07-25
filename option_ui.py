# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(576, 650)
        Form.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("\n"
                                  "#widget{\n"
                                  "border-image: url(:/kaishi/pic/bgpic.png);\n"
                                  "}\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("widget")
        self.pushButton_mos = QtWidgets.QPushButton(self.widget)
        self.pushButton_mos.setGeometry(QtCore.QRect(320, 190, 161, 121))
        self.pushButton_mos.setStyleSheet("font: 75 italic 16pt \"汉仪力量黑简\";\n"
                                          "color: rgb(85, 85, 127);")
        self.pushButton_mos.setObjectName("pushButton_mos")
        self.pushButton_bjt = QtWidgets.QPushButton(self.widget)
        self.pushButton_bjt.setGeometry(QtCore.QRect(100, 370, 161, 121))
        self.pushButton_bjt.setStyleSheet("font: 75 italic 16pt \"汉仪力量黑简\";\n"
                                          "color: rgb(85, 85, 127);")
        self.pushButton_bjt.setObjectName("pushButton_bjt")
        self.pushButton_quit = QtWidgets.QPushButton(self.widget)
        self.pushButton_quit.setGeometry(QtCore.QRect(320, 370, 161, 121))
        self.pushButton_quit.setStyleSheet("font: 75 italic 16pt \"汉仪力量黑简\";\n"
                                           "color: rgb(85, 85, 127);")
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.pushButton_pn = QtWidgets.QPushButton(self.widget)
        self.pushButton_pn.setGeometry(QtCore.QRect(100, 190, 161, 121))
        self.pushButton_pn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_pn.setStyleSheet("font: 75 italic 16pt \"汉仪力量黑简\";\n"
                                         "color: rgb(85, 85, 127);")
        self.pushButton_pn.setObjectName("pushButton_pn")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(200, 570, 161, 20))
        self.label_4.setStyleSheet("font: 10pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(50, 50, 281, 71))
        self.label.setStyleSheet("image: url(:/kaishi/pic/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(320, 70, 201, 51))
        self.label_2.setStyleSheet("font: 50 15pt \"汉仪力量黑简\";\n"
                                   "color: rgb(85, 85, 127);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "半导体器件仿真平台"))
        self.pushButton_mos.setText(_translate("Form", "MOSFET"))
        self.pushButton_bjt.setText(_translate("Form", "BJT"))
        self.pushButton_quit.setText(_translate("Form", "退出系统..."))
        self.pushButton_pn.setText(_translate("Form", "PN_Junction"))
        self.label_4.setText(_translate("Form", "2019. All Rights Reserved."))
        self.label_2.setText(_translate("Form", "半导体器件教学工具"))


import option_rc
