# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QWidget)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(625, 565)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 550, 500))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 280, 430))
        self.label.setStyleSheet(u"border-top-left-radius: 50px;\n"
                                 "border-image: url(:/new/prefix1/background.jpg);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet(u"border-top-left-radius: 50px;\n"
                                   "background-color:rgba(0,0,0,80);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet(u"background-color:rgba(255,255,255,255);\n"
                                   "border-bottom-right-radius:50px")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 80, 100, 40))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(295, 150, 190, 40))
        self.lineEdit.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(46,82,101,200);\n"
                                    "color:rgba(0,0,0,240);\n"
                                    "padding-bottom:7px;")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(295, 215, 190, 40))
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:7px;")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 280, 191, 40))
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton #pushButton {\n"
                                      "	background-color: rgba(255, 255, 255, 255); /* White background */\n"
                                      "	color: rgba(0, 0, 0, 210); /* Black text color, slightly transparent */\n"
                                      "	border: 2px solid black; /* Solid black border */\n"
                                      "	border-radius: 5px; /* Keeping the border radius for a slight curve at the edges */\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton #pushButton:hover {\n"
                                      "	background-color: rgba(245, 245, 245, 255); /* Slightly grey background on hover for a subtle effect */\n"
                                      "	border-color: #333; /* Darker border color when hovered */\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton #pushButton:pressed {\n"
                                      "	padding-left: 5px;\n"
                                      "	padding-top: 5px;\n"
                                      "	background-color: rgba(235, 235, 235, 255); /* Even darker background when pressed */\n"
                                      "	border-color: #222; /* Very dark border when pressed */\n"
                                      "}\n"
                                      "")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 340, 191, 40))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton #pushButton {\n"
                                        "	background-color: rgba(255, 255, 255, 255); /* White background */\n"
                                        "	color: rgba(0, 0, 0, 210); /* Black text color, slightly transparent */\n"
                                        "	border: 2px solid black; /* Solid black border */\n"
                                        "	border-radius: 5px; /* Keeping the border radius for a slight curve at the edges */\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton #pushButton:hover {\n"
                                        "	background-color: rgba(245, 245, 245, 255); /* Slightly grey background on hover for a subtle effect */\n"
                                        "	border-color: #333; /* Darker border color when hovered */\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton #pushButton:pressed {\n"
                                        "	padding-left: 5px;\n"
                                        "	padding-top: 5px;\n"
                                        "	background-color: rgba(235, 235, 235, 255); /* Even darker background when pressed */\n"
                                        "	border-color: #222; /* Very dark border when pressed */\n"
                                        "}\n"
                                        "")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(290, 420, 191, 31))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Widget", u"Log In", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"User Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Widget", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Log In", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Register", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"PushButton", None))
    # retranslateUi
