# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'joystickDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(443, 471)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.joyStateShow = QTextBrowser(Dialog)
        self.joyStateShow.setObjectName(u"joyStateShow")
        font = QFont()
        font.setPointSize(8)
        self.joyStateShow.setFont(font)

        self.gridLayout.addWidget(self.joyStateShow, 1, 0, 3, 1)

        self.nowSettingShow = QListWidget(Dialog)
        __qlistwidgetitem = QListWidgetItem(self.nowSettingShow)
        __qlistwidgetitem.setFont(font);
        self.nowSettingShow.setObjectName(u"nowSettingShow")
        self.nowSettingShow.setFont(font)

        self.gridLayout.addWidget(self.nowSettingShow, 1, 1, 1, 3)

        self.addSettingButton = QPushButton(Dialog)
        self.addSettingButton.setObjectName(u"addSettingButton")

        self.gridLayout.addWidget(self.addSettingButton, 2, 2, 1, 2)

        self.saveButton = QPushButton(Dialog)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout.addWidget(self.saveButton, 3, 1, 1, 2)

        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.gridLayout.addWidget(self.cancelButton, 3, 3, 1, 1)


        self.retranslateUi(Dialog)
        self.saveButton.clicked.connect(Dialog.accept)
        self.cancelButton.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u624b\u67c4\u529f\u80fd\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u624b\u67c4\u72b6\u6001", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5f53\u524d\u8bbe\u7f6e", None))

        __sortingEnabled = self.nowSettingShow.isSortingEnabled()
        self.nowSettingShow.setSortingEnabled(False)
        ___qlistwidgetitem = self.nowSettingShow.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"\u8f74 1: \u5bfc\u7ba1\u8fd0\u52a8\n"
"    (-1, 1) -> (-6400, 6400)", None));
        self.nowSettingShow.setSortingEnabled(__sortingEnabled)

        self.addSettingButton.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u8bbe\u7f6e", None))
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

