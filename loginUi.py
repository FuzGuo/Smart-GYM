# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginUi3.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QStackedWidget, QWidget)
import res_rc
from login_db import DatabaseFactory
from Email import EmailVerificationSender
from main_window.NavigationWidget import Window


class Ui_Form(object):
    def __init__(self):
        self.user = None

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(703, 598)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 30, 571, 491))
        self.widget.setStyleSheet(u"QPushButton#pushButton{\n"
                                  "	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
                                  "	color:rgba(255, 255, 255, 210);\n"
                                  "	border-radius:5px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton:hover{\n"
                                  "	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton:pressed{\n"
                                  "	padding-left:5px;\n"
                                  "	padding-top:5px;\n"
                                  "	background-color:rgba(150, 123, 111, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
                                  "	background-color: rgba(0, 0, 0, 0);\n"
                                  "	color:rgba(85, 98, 112, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
                                  "	color: rgba(131, 96, 53, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
                                  "	padding-left:5px;\n"
                                  "	p"
                                  "adding-top:5px;\n"
                                  "	color:rgba(91, 88, 53, 255);\n"
                                  "}\n"
                                  "\n"
                                  "")

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 251, 430))
        self.label.setStyleSheet(u"border-image: url(:/images/background.jpg);\n"
                                 "border-top-left-radius: 50px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 30, 251, 430))
        self.label_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 80);\n"
                                   "border-top-left-radius: 50px;")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 80, 241, 130))
        self.label_6.setStyleSheet(u"background-color:rgba(0, 0, 0, 75);")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 80, 180, 40))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT Bold"])
        font.setPointSize(22)
        font.setBold(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color:rgba(255, 255, 255, 200);")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 145, 220, 50))
        font1 = QFont()
        font1.setFamilies([u"Arial Narrow"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color:rgba(255, 255, 255, 170);")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(290, 30, 241, 431))
        self.stackedWidget.setStyleSheet(u"background-color:rgba(255, 255, 255, 255);\n"
                                         "border-bottom-right-radius: 50px;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"border-bottom-right-radius: 50px;")
        self.label_19 = QLabel(self.page)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(80, 30, 100, 40))
        font2 = QFont()
        font2.setFamilies([u"Microsoft Tai Le"])
        font2.setPointSize(20)
        font2.setBold(False)
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.lineEdit_5 = QLineEdit(self.page)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(20, 100, 190, 40))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei"])
        font3.setPointSize(10)
        self.lineEdit_5.setFont(font3)
        self.lineEdit_5.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px;")
        self.lineEdit_6 = QLineEdit(self.page)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(20, 160, 190, 40))
        font4 = QFont()
        font4.setFamilies([u"Microsoft JhengHei"])
        font4.setPointSize(10)
        self.lineEdit_6.setFont(font4)
        self.lineEdit_6.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px;")
        self.lineEdit_6.setEchoMode(QLineEdit.Password)
        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 230, 190, 40))
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font5.setPointSize(11)
        font5.setBold(False)
        self.pushButton_3.setFont(font5)
        self.pushButton_3.setStyleSheet(
            u"color: white;             /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272 */\n"
            "background-color: rgb(54, 144, 138);   /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u9752\u8272 */\n"
            "border-radius: 10px;        /* \u8bbe\u7f6e\u8fb9\u6846\u5706\u89d2\u7684\u534a\u5f84\u4e3a10\u50cf\u7d20 */")
        self.pushButton_11 = QPushButton(self.page)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(65, 310, 101, 31))
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font6.setPointSize(8)
        font6.setBold(False)
        self.pushButton_11.setFont(font6)
        self.pushButton_11.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.pushButton_12 = QPushButton(self.page)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(25, 350, 191, 31))
        self.pushButton_12.setFont(font6)
        self.pushButton_12.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.pushButton_14 = QPushButton(self.page)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(181, 10, 21, 21))
        self.pushButton_14.setFont(font6)
        self.pushButton_14.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.pushButton_13 = QPushButton(self.page)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(200, 10, 21, 21))
        self.pushButton_13.setFont(font6)
        self.pushButton_13.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 270, 191, 21))
        font7 = QFont()
        font7.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font7.setPointSize(8)
        self.label_5.setFont(font7)
        self.label_5.setFocusPolicy(Qt.NoFocus)
        self.label_5.setStyleSheet(u"color:rgb(186, 0, 0)")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page)
        self.label_19.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.pushButton_3.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.label_5.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"border-bottom-right-radius: 50px;")
        self.label_22 = QLabel(self.page_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(70, 30, 100, 40))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.lineEdit_7 = QLineEdit(self.page_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(20, 110, 190, 31))
        self.lineEdit_7.setFont(font3)
        self.lineEdit_7.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px;")
        self.lineEdit_8 = QLineEdit(self.page_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(20, 150, 190, 31))
        self.lineEdit_8.setFont(font4)
        self.lineEdit_8.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px;")
        self.lineEdit_8.setEchoMode(QLineEdit.Password)
        self.lineEdit_9 = QLineEdit(self.page_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(20, 190, 190, 31))
        self.lineEdit_9.setFont(font4)
        self.lineEdit_9.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px;")
        self.lineEdit_9.setEchoMode(QLineEdit.Password)
        self.lineEdit_10 = QLineEdit(self.page_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(20, 230, 191, 31))
        self.lineEdit_10.setFont(font4)
        self.lineEdit_10.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
                                       "border:none;\n"
                                       "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                       "color:rgba(0, 0, 0, 240);\n"
                                       "padding-bottom:7px;")
        self.lineEdit_10.setEchoMode(QLineEdit.Normal)
        self.lineEdit_11 = QLineEdit(self.page_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(80, 270, 131, 31))
        self.lineEdit_11.setFont(font4)
        self.lineEdit_11.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
                                       "border:none;\n"
                                       "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                       "color:rgba(0, 0, 0, 240);\n"
                                       "padding-bottom:7px;")
        self.lineEdit_11.setEchoMode(QLineEdit.Normal)
        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 270, 51, 31))
        self.pushButton_4.setFont(font5)
        self.pushButton_4.setStyleSheet(
            u"color: white;             /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272 */\n"
            "background-color: rgb(54, 144, 138);   /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u9752\u8272 */\n"
            "border-radius: 10px;        /* \u8bbe\u7f6e\u8fb9\u6846\u5706\u89d2\u7684\u534a\u5f84\u4e3a10\u50cf\u7d20 */")
        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 320, 190, 31))
        self.pushButton_5.setFont(font5)
        self.pushButton_5.setStyleSheet(
            u"color: white;             /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272 */\n"
            "background-color: rgb(54, 144, 138);   /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u9752\u8272 */\n"
            "border-radius: 10px;        /* \u8bbe\u7f6e\u8fb9\u6846\u5706\u89d2\u7684\u534a\u5f84\u4e3a10\u50cf\u7d20 */")
        self.pushButton_10 = QPushButton(self.page_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(0, 380, 101, 31))
        self.pushButton_10.setFont(font6)
        self.pushButton_10.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.pushButton_15 = QPushButton(self.page_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(200, 10, 21, 21))
        self.pushButton_15.setFont(font6)
        self.pushButton_15.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.pushButton_16 = QPushButton(self.page_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(180, 10, 21, 21))
        self.pushButton_16.setFont(font6)
        self.pushButton_16.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 360, 191, 16))
        self.label_3.setFont(font7)
        self.label_3.setFocusPolicy(Qt.NoFocus)
        self.label_3.setStyleSheet(u"color:rgb(186, 0, 0)")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_23 = QLabel(self.page_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 30, 201, 40))
        self.label_23.setFont(font2)
        self.label_23.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.lineEdit_12 = QLineEdit(self.page_3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(20, 89, 190, 31))
        self.lineEdit_12.setFont(font3)
        self.lineEdit_12.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
                                       "border:none;\n"
                                       "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                       "color:rgba(0, 0, 0, 240);\n"
                                       "padding-bottom:7px;")
        self.lineEdit_13 = QLineEdit(self.page_3)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(20, 149, 190, 31))
        self.lineEdit_13.setFont(font3)
        self.lineEdit_13.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
                                       "border:none;\n"
                                       "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                       "color:rgba(0, 0, 0, 240);\n"
                                       "padding-bottom:7px;")
        self.lineEdit_14 = QLineEdit(self.page_3)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(80, 209, 131, 31))
        self.lineEdit_14.setFont(font3)
        self.lineEdit_14.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
                                       "border:none;\n"
                                       "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                       "color:rgba(0, 0, 0, 240);\n"
                                       "padding-bottom:7px;")
        self.pushButton_7 = QPushButton(self.page_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 210, 51, 31))
        self.pushButton_7.setFont(font5)
        self.pushButton_7.setStyleSheet(
            u"color: white;             /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272 */\n"
            "background-color: rgb(54, 144, 138);   /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u9752\u8272 */\n"
            "border-radius: 10px;        /* \u8bbe\u7f6e\u8fb9\u6846\u5706\u89d2\u7684\u534a\u5f84\u4e3a10\u50cf\u7d20 */")
        self.lineEdit_15 = QLineEdit(self.page_3)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(20, 269, 190, 31))
        self.lineEdit_15.setFont(font4)
        self.lineEdit_15.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
                                       "border:none;\n"
                                       "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                       "color:rgba(0, 0, 0, 240);\n"
                                       "padding-bottom:7px;")
        self.lineEdit_15.setEchoMode(QLineEdit.Password)
        self.lineEdit_5.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_6.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_7.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_8.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_9.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_10.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_11.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_12.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_13.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_14.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_15.setContextMenuPolicy(Qt.NoContextMenu)
        self.pushButton_8 = QPushButton(self.page_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 320, 190, 31))
        self.pushButton_8.setFont(font5)
        self.pushButton_8.setStyleSheet(
            u"color: white;             /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272 */\n"
            "background-color: rgb(54, 144, 138);   /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u9752\u8272 */\n"
            "border-radius: 10px;        /* \u8bbe\u7f6e\u8fb9\u6846\u5706\u89d2\u7684\u534a\u5f84\u4e3a10\u50cf\u7d20 */")
        self.pushButton_9 = QPushButton(self.page_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(0, 390, 101, 31))
        self.pushButton_9.setFont(font6)
        self.pushButton_9.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.pushButton_17 = QPushButton(self.page_3)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(259, 20, 21, 21))
        self.pushButton_17.setFont(font6)
        self.pushButton_17.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.pushButton_18 = QPushButton(self.page_3)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(240, 20, 21, 21))
        self.pushButton_18.setFont(font6)
        self.pushButton_18.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.pushButton_20 = QPushButton(self.page_3)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(180, 10, 21, 21))
        self.pushButton_20.setFont(font6)
        self.pushButton_20.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.pushButton_19 = QPushButton(self.page_3)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(200, 10, 21, 21))
        self.pushButton_19.setFont(font6)
        self.pushButton_19.setStyleSheet(
            u"color: gray;        /* \u8bbe\u7f6e\u5b57\u4f53\u989c\u8272\u4e3a\u7070\u8272 */\n"
            "background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 360, 191, 20))
        self.label_4.setFont(font7)
        self.label_4.setFocusPolicy(Qt.NoFocus)
        self.label_4.setStyleSheet(u"color:rgb(186, 0, 0)")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)
        # timer
        self.timer = QTimer(self.widget)
        self.timer.setInterval(30000)  # 30000ms == 30s
        self.timer.timeout.connect(self.timer.stop)
        # change to register page
        self.pushButton_11.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        # change to password reset page
        self.pushButton_12.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        # change to menu
        self.pushButton_10.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        # exit application
        self.pushButton_13.clicked.connect(QApplication.instance().quit)
        self.pushButton_15.clicked.connect(QApplication.instance().quit)
        self.pushButton_19.clicked.connect(QApplication.instance().quit)

        # register
        self.registerCode = None
        self.email_sender = EmailVerificationSender()
        self.pushButton_4.clicked.connect(self.handleEmailSending)
        self.pushButton_5.clicked.connect(self.handleRegister)
        # login
        # self.pushButton_3.clicked.connect(self.handleLogin)
        # reset password
        self.pushButton_7.clicked.connect(self.handlePasswordEmail)
        self.pushButton_8.clicked.connect(self.handlePasswordReset)



        QMetaObject.connectSlotsByName(Form)

        # setupUi

    def handlePasswordReset(self):
        if self.lineEdit_12.text().strip() == '':
            self.label_4.setText("Invalid username.")
            return 0
        db_factory = DatabaseFactory()
        result = db_factory.query_user_by_name(self.lineEdit_12.text())
        if result is None:
            self.label_4.setText("Username is not existed!")
            return 0
        if (self.lineEdit_14.text() != self.registerCode) | (self.lineEdit_14.text() == ''):
            self.label_4.setText("Error Email code.")
            return 0
        if self.lineEdit_15.text() == '':
            self.label_4.setText("Invalid password.")
            return 0
        db_factory.reset_password(self.lineEdit_12.text(), self.lineEdit_15.text())

    def handlePasswordEmail(self):
        if not self.timer.isActive():
            # self.send_email()

            # 获取输入框中的邮箱地址
            email = self.lineEdit_13.text()
            # 发送验证码，并将返回的验证码存储到self.registerCode
            self.registerCode = self.email_sender.send_verification_email(email)
            if self.registerCode is None:
                self.label_4.setText("Failed to send an email!")
                return 0
            self.label_4.setText("Email sent successfully!")
            self.timer.start()
        else:
            self.label_4.setText("Wait 30s for another email.")
            return 0

    def handleRegister(self):
        db_factory = DatabaseFactory()
        result = db_factory.query_user_by_name(self.lineEdit_7.text())
        if result is not None:
            self.label_3.setText("Username is already existed!")
            return 0
        if self.lineEdit_8.text() == '':
            self.label_3.setText("Invalid password.")
            return 0
        if self.lineEdit_9.text() == '':
            self.label_3.setText("Invalid password.")
            return 0
        if self.lineEdit_8.text() != self.lineEdit_9.text():
            self.label_3.setText("Invalid password.")
            return 0
        if self.lineEdit_11.text() != self.registerCode:
            self.label_3.setText("Error Email code.")
            return 0
        if self.lineEdit_7.text().strip() == '':
            self.label_4.setText("Invalid username.")
            return 0
        db_factory.user_register(name=self.lineEdit_7.text(), password=self.lineEdit_8.text(),
                                 email=self.lineEdit_10.text())

    def handleLogin(self):
        db_factory = DatabaseFactory()
        result = db_factory.query_user_by_name(self.lineEdit_5.text())
        if result is None:
            self.label_5.setText("Error Username!")
            return 0
        result = db_factory.check_password(self.lineEdit_5.text(), self.lineEdit_6.text())
        if result is None:
            self.label_5.setText("Error Password!")
            return 0
        else:
            self.user = result
            return 1
        # mainwindow = Window()
        # mainwindow.show()


    def handleEmailSending(self):
        if not self.timer.isActive():
            # self.send_email()

            # 获取输入框中的邮箱地址
            email = self.lineEdit_10.text()
            # 发送验证码，并将返回的验证码存储到self.registerCode
            self.registerCode = self.email_sender.send_verification_email(email)
            if self.registerCode is None:
                self.label_3.setText("Failed to send an email!")
                return 0
            self.label_3.setText("Email sent successfully!")
            self.timer.start()
        else:
            self.label_3.setText("Wait 30s for another email.")
            return 0

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Hi!", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Today is a good day \n"
                                                                "for your plan.", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"  User Name", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"  Password", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"L o g  I n", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"Register", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"Forgot your password?", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"\u4e00", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_5.setText("")
        self.label_22.setText(QCoreApplication.translate("Form", u"Register", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Form", u"  User Name", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("Form", u"  Password", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("Form", u"  Enter Password again", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("Form", u"  Email", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("Form", u"Verification Code", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Send", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Register", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"<-back to menu", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"X", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"\u4e00", None))
        self.label_3.setText("")
        self.label_23.setText(QCoreApplication.translate("Form", u"Password Reset", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("Form", u"  User Name", None))
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("Form", u"  Email", None))
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("Form", u"Verification Code", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Send", None))
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("Form", u"  New Password", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"<-back to menu", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"X", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"\u4e00", None))
        self.pushButton_20.setText(QCoreApplication.translate("Form", u"\u4e00", None))
        self.pushButton_19.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_4.setText("")
    # retranslateUi
