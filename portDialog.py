# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'portDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(355, 315)
        self.recv_Text = QTextBrowser(Dialog)
        self.recv_Text.setObjectName(u"recv_Text")
        self.recv_Text.setGeometry(QRect(10, 50, 331, 231))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 10, 71, 31))
        self.AutoLast = QRadioButton(Dialog)
        self.AutoLast.setObjectName(u"AutoLast")
        self.AutoLast.setGeometry(QRect(180, 280, 101, 22))
        self.end_select = QComboBox(Dialog)
        self.end_select.addItem("")
        self.end_select.addItem("")
        self.end_select.addItem("")
        self.end_select.addItem("")
        self.end_select.setObjectName(u"end_select")
        self.end_select.setGeometry(QRect(50, 280, 111, 22))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 280, 54, 22))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 280, 61, 23))
        self.send_Input = QLineEdit(Dialog)
        self.send_Input.setObjectName(u"send_Input")
        self.send_Input.setGeometry(QRect(10, 9, 261, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u4e32\u53e3\u8c03\u8bd5\u52a9\u624b", None))
        self.recv_Text.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u53d1\u9001", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("Dialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.AutoLast.setText(QCoreApplication.translate("Dialog", u"\u81ea\u52a8\u8f6c\u5230\u884c\u5c3e", None))
        self.end_select.setItemText(0, QCoreApplication.translate("Dialog", u"\u65e0", None))
        self.end_select.setItemText(1, QCoreApplication.translate("Dialog", u"\u6362\u884c (\\n)", None))
        self.end_select.setItemText(2, QCoreApplication.translate("Dialog", u"\u56de\u8f66 (\\r)", None))
        self.end_select.setItemText(3, QCoreApplication.translate("Dialog", u"CR NL(\\r\\n)", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"\u7ed3\u675f\u7b26", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u6e05\u7a7a", None))
    # retranslateUi

