# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buttonSetDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(263, 89)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.buttonChoose = QComboBox(Dialog)
        self.buttonChoose.setObjectName(u"buttonChoose")

        self.gridLayout.addWidget(self.buttonChoose, 1, 0, 1, 1)

        self.functionChoose = QComboBox(Dialog)
        self.functionChoose.addItem("")
        self.functionChoose.addItem("")
        self.functionChoose.addItem("")
        self.functionChoose.setObjectName(u"functionChoose")

        self.gridLayout.addWidget(self.functionChoose, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6309\u94ae\u529f\u80fd\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6309\u94ae", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u529f\u80fd", None))
        self.functionChoose.setItemText(0, QCoreApplication.translate("Dialog", u"\u65e0\u529f\u80fd", None))
        self.functionChoose.setItemText(1, QCoreApplication.translate("Dialog", u"\u589e\u52a0\u901f\u5ea6\u6863\u4f4d", None))
        self.functionChoose.setItemText(2, QCoreApplication.translate("Dialog", u"\u964d\u4f4e\u901f\u5ea6\u6863\u4f4d", None))

    # retranslateUi

