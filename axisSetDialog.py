# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'axisSetDialog.ui'
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
    QDialogButtonBox, QDoubleSpinBox, QGridLayout, QLabel,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 110)
        Dialog.setMinimumSize(QSize(460, 110))
        Dialog.setMaximumSize(QSize(115200, 115200))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 5, 1, 2)

        self.highSpeed = QDoubleSpinBox(Dialog)
        self.highSpeed.setObjectName(u"highSpeed")
        self.highSpeed.setMinimum(-99999.000000000000000)
        self.highSpeed.setMaximum(99999.000000000000000)
        self.highSpeed.setValue(3600.000000000000000)

        self.gridLayout.addWidget(self.highSpeed, 2, 6, 1, 1)

        self.lowSpeed = QDoubleSpinBox(Dialog)
        self.lowSpeed.setObjectName(u"lowSpeed")
        self.lowSpeed.setMinimum(-99999.000000000000000)
        self.lowSpeed.setMaximum(99999.990000000005239)
        self.lowSpeed.setSingleStep(0.100000000000000)
        self.lowSpeed.setValue(-3600.000000000000000)

        self.gridLayout.addWidget(self.lowSpeed, 2, 5, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 2)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.axisSelect = QComboBox(Dialog)
        information = [1,2,3,4,5,6,7,8,9,10]
        self.axisSelect.setObjectName(u"axisSelect")
        self.axisSelect.addItems(information)
        self.axisSelect.setMinimumSize(QSize(100, 0))
        self.axisSelect.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.axisSelect, 2, 0, 1, 1)

        self.lowAxis = QDoubleSpinBox(Dialog)
        self.lowAxis.setObjectName(u"lowAxis")
        self.lowAxis.setMinimum(-99.000000000000000)
        self.lowAxis.setSingleStep(0.100000000000000)
        self.lowAxis.setValue(-1.000000000000000)

        self.gridLayout.addWidget(self.lowAxis, 2, 2, 1, 1)

        self.highAxis = QDoubleSpinBox(Dialog)
        self.highAxis.setObjectName(u"highAxis")
        self.highAxis.setMinimum(-99.000000000000000)
        self.highAxis.setSingleStep(0.100000000000000)
        self.highAxis.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.highAxis, 2, 3, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 2, 4, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 5, 5, 1, 2)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.motoSelect = QComboBox(Dialog)
        self.motoSelect.addItem("")
        self.motoSelect.addItem("")
        self.motoSelect.addItem("")
        self.motoSelect.addItem("")
        self.motoSelect.setObjectName(u"motoSelect")

        self.gridLayout.addWidget(self.motoSelect, 5, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 5, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u624b\u67c4\u6620\u5c04\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5668\u68b0\u901f\u5ea6\u533a\u95f4", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u624b\u67c4\u8f74\u533a\u95f4", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u8f74\u53f7", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"->", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u88ab\u64cd\u7eb5\u5668\u68b0", None))
        self.motoSelect.setItemText(0, QCoreApplication.translate("Dialog", u"\u65e0\u64cd\u4f5c", None))
        self.motoSelect.setItemText(1, QCoreApplication.translate("Dialog", u"\u5bfc\u7ba1\u9012\u9001", None))
        self.motoSelect.setItemText(2, QCoreApplication.translate("Dialog", u"\u5bfc\u4e1d\u9012\u9001", None))
        self.motoSelect.setItemText(3, QCoreApplication.translate("Dialog", u"\u5bfc\u4e1d\u65cb\u8f6c", None))

    # retranslateUi

