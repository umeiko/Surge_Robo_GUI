# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 785)
        MainWindow.setMinimumSize(QSize(750, 750))
        icon = QIcon()
        icon.addFile(u":/main_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.menu_joySet = QAction(MainWindow)
        self.menu_joySet.setObjectName(u"menu_joySet")
        self.menu_Port = QAction(MainWindow)
        self.menu_Port.setObjectName(u"menu_Port")
        self.menu_exit = QAction(MainWindow)
        self.menu_exit.setObjectName(u"menu_exit")
        self.style_classic = QAction(MainWindow)
        self.style_classic.setObjectName(u"style_classic")
        self.style_dark = QAction(MainWindow)
        self.style_dark.setObjectName(u"style_dark")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 26))
        self.label_5.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_2.addWidget(self.label_5)

        self.cath_speed_lcd = QLCDNumber(self.centralwidget)
        self.cath_speed_lcd.setObjectName(u"cath_speed_lcd")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cath_speed_lcd.sizePolicy().hasHeightForWidth())
        self.cath_speed_lcd.setSizePolicy(sizePolicy)
        self.cath_speed_lcd.setMinimumSize(QSize(0, 75))
        self.cath_speed_lcd.setMaximumSize(QSize(16777215, 75))
        self.cath_speed_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.cath_speed_lcd.setProperty("value", 0.000000000000000)

        self.verticalLayout_2.addWidget(self.cath_speed_lcd)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 26))
        self.label_6.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_2.addWidget(self.label_6)

        self.cath_pos_speed_lcd = QLCDNumber(self.centralwidget)
        self.cath_pos_speed_lcd.setObjectName(u"cath_pos_speed_lcd")
        self.cath_pos_speed_lcd.setMinimumSize(QSize(0, 75))
        self.cath_pos_speed_lcd.setMaximumSize(QSize(16777215, 75))
        self.cath_pos_speed_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.cath_pos_speed_lcd.setProperty("value", 0.000000000000000)

        self.verticalLayout_2.addWidget(self.cath_pos_speed_lcd)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 25))
        self.label_9.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_2.addWidget(self.label_9)

        self.stroke_progress = QProgressBar(self.centralwidget)
        self.stroke_progress.setObjectName(u"stroke_progress")
        self.stroke_progress.setMaximumSize(QSize(16777215, 25))
        self.stroke_progress.setValue(24)
        self.stroke_progress.setTextVisible(False)

        self.verticalLayout_2.addWidget(self.stroke_progress)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.cath_up_button = QPushButton(self.centralwidget)
        self.cath_up_button.setObjectName(u"cath_up_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cath_up_button.sizePolicy().hasHeightForWidth())
        self.cath_up_button.setSizePolicy(sizePolicy1)
        self.cath_up_button.setMinimumSize(QSize(70, 70))
        self.cath_up_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cath_up_button.setStyleSheet(u"border-image: url(:/up.png);\n"
"")

        self.verticalLayout_4.addWidget(self.cath_up_button)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(50, 26))
        self.label_11.setMaximumSize(QSize(16777215, 26))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_11)

        self.cath_down_button = QPushButton(self.centralwidget)
        self.cath_down_button.setObjectName(u"cath_down_button")
        sizePolicy1.setHeightForWidth(self.cath_down_button.sizePolicy().hasHeightForWidth())
        self.cath_down_button.setSizePolicy(sizePolicy1)
        self.cath_down_button.setMinimumSize(QSize(70, 70))
        self.cath_down_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cath_down_button.setStyleSheet(u"border-image: url(:/down.png);")

        self.verticalLayout_4.addWidget(self.cath_down_button)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.cath_step_slider = QSlider(self.centralwidget)
        self.cath_step_slider.setObjectName(u"cath_step_slider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cath_step_slider.sizePolicy().hasHeightForWidth())
        self.cath_step_slider.setSizePolicy(sizePolicy2)
        self.cath_step_slider.setMinimumSize(QSize(25, 1))
        self.cath_step_slider.setMaximumSize(QSize(16777215, 115200))
        self.cath_step_slider.setTabletTracking(False)
        self.cath_step_slider.setLayoutDirection(Qt.LeftToRight)
        self.cath_step_slider.setOrientation(Qt.Vertical)
        self.cath_step_slider.setInvertedAppearance(False)
        self.cath_step_slider.setInvertedControls(False)

        self.verticalLayout_5.addWidget(self.cath_step_slider, 0, Qt.AlignHCenter)

        self.cath_step_text = QLabel(self.centralwidget)
        self.cath_step_text.setObjectName(u"cath_step_text")
        self.cath_step_text.setMinimumSize(QSize(60, 25))
        self.cath_step_text.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_5.addWidget(self.cath_step_text, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.cath_disable_button = QPushButton(self.centralwidget)
        self.cath_disable_button.setObjectName(u"cath_disable_button")
        self.cath_disable_button.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.cath_disable_button.sizePolicy().hasHeightForWidth())
        self.cath_disable_button.setSizePolicy(sizePolicy1)
        self.cath_disable_button.setMaximumSize(QSize(160, 30))
        self.cath_disable_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon1 = QIcon()
        icon1.addFile(u":/disable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cath_disable_button.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.cath_disable_button, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(200, 25))
        self.label_15.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_6.addWidget(self.label_15)

        self.wire_speed_lcd = QLCDNumber(self.centralwidget)
        self.wire_speed_lcd.setObjectName(u"wire_speed_lcd")
        sizePolicy.setHeightForWidth(self.wire_speed_lcd.sizePolicy().hasHeightForWidth())
        self.wire_speed_lcd.setSizePolicy(sizePolicy)
        self.wire_speed_lcd.setMinimumSize(QSize(0, 75))
        self.wire_speed_lcd.setMaximumSize(QSize(16777215, 75))
        self.wire_speed_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.wire_speed_lcd.setProperty("value", 0.000000000000000)

        self.verticalLayout_6.addWidget(self.wire_speed_lcd)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 25))
        self.label_16.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_6.addWidget(self.label_16)

        self.wire_pos_lcd = QLCDNumber(self.centralwidget)
        self.wire_pos_lcd.setObjectName(u"wire_pos_lcd")
        self.wire_pos_lcd.setMinimumSize(QSize(0, 75))
        self.wire_pos_lcd.setMaximumSize(QSize(16777215, 75))
        self.wire_pos_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.wire_pos_lcd.setProperty("value", 0.000000000000000)

        self.verticalLayout_6.addWidget(self.wire_pos_lcd)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 25))
        self.label_17.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_6.addWidget(self.label_17)

        self.cath_mode_select = QComboBox(self.centralwidget)
        self.cath_mode_select.addItem("")
        self.cath_mode_select.addItem("")
        self.cath_mode_select.setObjectName(u"cath_mode_select")
        self.cath_mode_select.setMinimumSize(QSize(0, 25))
        self.cath_mode_select.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.cath_mode_select)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 5, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.wire_up_button = QPushButton(self.centralwidget)
        self.wire_up_button.setObjectName(u"wire_up_button")
        sizePolicy1.setHeightForWidth(self.wire_up_button.sizePolicy().hasHeightForWidth())
        self.wire_up_button.setSizePolicy(sizePolicy1)
        self.wire_up_button.setMinimumSize(QSize(70, 70))
        self.wire_up_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.wire_up_button.setStyleSheet(u"border-image: url(:/up.png);\n"
"")

        self.verticalLayout_7.addWidget(self.wire_up_button)

        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(50, 26))
        self.label_19.setMaximumSize(QSize(16777215, 26))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_19)

        self.wire_down_button = QPushButton(self.centralwidget)
        self.wire_down_button.setObjectName(u"wire_down_button")
        sizePolicy1.setHeightForWidth(self.wire_down_button.sizePolicy().hasHeightForWidth())
        self.wire_down_button.setSizePolicy(sizePolicy1)
        self.wire_down_button.setMinimumSize(QSize(70, 70))
        self.wire_down_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.wire_down_button.setStyleSheet(u"border-image: url(:/down.png);")

        self.verticalLayout_7.addWidget(self.wire_down_button)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.wire_step_slider = QSlider(self.centralwidget)
        self.wire_step_slider.setObjectName(u"wire_step_slider")
        sizePolicy1.setHeightForWidth(self.wire_step_slider.sizePolicy().hasHeightForWidth())
        self.wire_step_slider.setSizePolicy(sizePolicy1)
        self.wire_step_slider.setMinimumSize(QSize(25, 1))
        self.wire_step_slider.setMaximumSize(QSize(16777215, 115200))
        self.wire_step_slider.setTabletTracking(False)
        self.wire_step_slider.setLayoutDirection(Qt.LeftToRight)
        self.wire_step_slider.setOrientation(Qt.Vertical)
        self.wire_step_slider.setInvertedAppearance(False)
        self.wire_step_slider.setInvertedControls(False)

        self.verticalLayout_8.addWidget(self.wire_step_slider, 0, Qt.AlignHCenter)

        self.wire_step_text = QLabel(self.centralwidget)
        self.wire_step_text.setObjectName(u"wire_step_text")
        self.wire_step_text.setMinimumSize(QSize(60, 25))
        self.wire_step_text.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_8.addWidget(self.wire_step_text, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.wire_disable_button = QPushButton(self.centralwidget)
        self.wire_disable_button.setObjectName(u"wire_disable_button")
        self.wire_disable_button.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.wire_disable_button.sizePolicy().hasHeightForWidth())
        self.wire_disable_button.setSizePolicy(sizePolicy1)
        self.wire_disable_button.setMaximumSize(QSize(160, 30))
        self.wire_disable_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.wire_disable_button.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.wire_disable_button, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(200, 25))
        self.label_18.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_9.addWidget(self.label_18)

        self.wire_rotSpeed_lcd = QLCDNumber(self.centralwidget)
        self.wire_rotSpeed_lcd.setObjectName(u"wire_rotSpeed_lcd")
        sizePolicy.setHeightForWidth(self.wire_rotSpeed_lcd.sizePolicy().hasHeightForWidth())
        self.wire_rotSpeed_lcd.setSizePolicy(sizePolicy)
        self.wire_rotSpeed_lcd.setMinimumSize(QSize(0, 75))
        self.wire_rotSpeed_lcd.setMaximumSize(QSize(16777215, 75))
        self.wire_rotSpeed_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.wire_rotSpeed_lcd.setProperty("value", 0.000000000000000)

        self.verticalLayout_9.addWidget(self.wire_rotSpeed_lcd)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 25))
        self.label_20.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_9.addWidget(self.label_20)

        self.wire_rotPos_lcd = QLCDNumber(self.centralwidget)
        self.wire_rotPos_lcd.setObjectName(u"wire_rotPos_lcd")
        self.wire_rotPos_lcd.setMinimumSize(QSize(0, 75))
        self.wire_rotPos_lcd.setMaximumSize(QSize(16777215, 65))
        self.wire_rotPos_lcd.setSegmentStyle(QLCDNumber.Filled)
        self.wire_rotPos_lcd.setProperty("value", 0.000000000000000)

        self.verticalLayout_9.addWidget(self.wire_rotPos_lcd)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 25))
        self.label_13.setMaximumSize(QSize(16777215, 25))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_13)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.wire_antiClock_button = QPushButton(self.centralwidget)
        self.wire_antiClock_button.setObjectName(u"wire_antiClock_button")
        sizePolicy1.setHeightForWidth(self.wire_antiClock_button.sizePolicy().hasHeightForWidth())
        self.wire_antiClock_button.setSizePolicy(sizePolicy1)
        self.wire_antiClock_button.setMinimumSize(QSize(100, 100))
        self.wire_antiClock_button.setMaximumSize(QSize(500, 500))
        self.wire_antiClock_button.setSizeIncrement(QSize(1, 1))
        self.wire_antiClock_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.wire_antiClock_button.setStyleSheet(u"border-image: url(:/anti-clock-wise.png);")

        self.horizontalLayout_5.addWidget(self.wire_antiClock_button)

        self.wire_clock_button = QPushButton(self.centralwidget)
        self.wire_clock_button.setObjectName(u"wire_clock_button")
        sizePolicy1.setHeightForWidth(self.wire_clock_button.sizePolicy().hasHeightForWidth())
        self.wire_clock_button.setSizePolicy(sizePolicy1)
        self.wire_clock_button.setMinimumSize(QSize(100, 100))
        self.wire_clock_button.setMaximumSize(QSize(500, 500))
        self.wire_clock_button.setSizeIncrement(QSize(1, 1))
        self.wire_clock_button.setBaseSize(QSize(1, 1))
        self.wire_clock_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.wire_clock_button.setStyleSheet(u"border-image: url(:/clock-wise.png);\n"
"")

        self.horizontalLayout_5.addWidget(self.wire_clock_button)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.wireRot_step_slider = QSlider(self.centralwidget)
        self.wireRot_step_slider.setObjectName(u"wireRot_step_slider")
        self.wireRot_step_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_10.addWidget(self.wireRot_step_slider)

        self.wireRot_step_text = QLabel(self.centralwidget)
        self.wireRot_step_text.setObjectName(u"wireRot_step_text")
        self.wireRot_step_text.setMaximumSize(QSize(16777215, 25))
        self.wireRot_step_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.wireRot_step_text)

        self.wire_rot_disable_button = QPushButton(self.centralwidget)
        self.wire_rot_disable_button.setObjectName(u"wire_rot_disable_button")
        self.wire_rot_disable_button.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.wire_rot_disable_button.sizePolicy().hasHeightForWidth())
        self.wire_rot_disable_button.setSizePolicy(sizePolicy1)
        self.wire_rot_disable_button.setMinimumSize(QSize(0, 30))
        self.wire_rot_disable_button.setMaximumSize(QSize(160, 30))
        self.wire_rot_disable_button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.wire_rot_disable_button.setIcon(icon1)

        self.verticalLayout_10.addWidget(self.wire_rot_disable_button, 0, Qt.AlignHCenter)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))

        self.verticalLayout.addWidget(self.label)

        self.com_select = QComboBox(self.groupBox)
        self.com_select.addItem("")
        self.com_select.setObjectName(u"com_select")
        self.com_select.setMinimumSize(QSize(0, 25))
        self.com_select.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.com_select)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))

        self.verticalLayout.addWidget(self.label_2)

        self.joystick_select = QComboBox(self.groupBox)
        self.joystick_select.addItem("")
        self.joystick_select.setObjectName(u"joystick_select")
        self.joystick_select.setMinimumSize(QSize(0, 25))
        self.joystick_select.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.joystick_select)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.label_10)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.label_14)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gear_level_slider = QSlider(self.groupBox)
        self.gear_level_slider.setObjectName(u"gear_level_slider")
        self.gear_level_slider.setMinimumSize(QSize(0, 25))
        self.gear_level_slider.setCursor(QCursor(Qt.OpenHandCursor))
        self.gear_level_slider.setMinimum(1)
        self.gear_level_slider.setMaximum(5)
        self.gear_level_slider.setPageStep(1)
        self.gear_level_slider.setValue(1)
        self.gear_level_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.gear_level_slider)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.groupBox)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.all_stop_button = QPushButton(self.centralwidget)
        self.all_stop_button.setObjectName(u"all_stop_button")
        self.all_stop_button.setMinimumSize(QSize(230, 60))
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(20)
        self.all_stop_button.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.all_stop_button.setIcon(icon2)
        self.all_stop_button.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.all_stop_button, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 750, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menu)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.menu_joySet)
        self.menu.addAction(self.menu_Port)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.menu_exit)
        self.menu_2.addAction(self.style_classic)
        self.menu_2.addAction(self.style_dark)

        self.retranslateUi(MainWindow)
        self.gear_level_slider.valueChanged.connect(self.label_14.setNum)
        self.menu_exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u624b\u672f\u673a\u5668\u4eba\u4e13\u5bb6", None))
        self.menu_joySet.setText(QCoreApplication.translate("MainWindow", u"\u624b\u67c4\u6620\u5c04\u8bbe\u7f6e", None))
        self.menu_Port.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u8c03\u8bd5", None))
        self.menu_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.style_classic.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u5178", None))
        self.style_dark.setText(QCoreApplication.translate("MainWindow", u"\u6697\u9ed1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u7ba1\u8fdb\u7ed9\u901f\u5ea6", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u7ba1\u5f53\u524d\u4f4d\u7f6e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u7ba1\u884c\u7a0b\u4f4d\u7f6e", None))
        self.cath_up_button.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5355\u6b65\u9012\u9001\u6309\u94ae", None))
        self.cath_down_button.setText("")
        self.cath_step_text.setText(QCoreApplication.translate("MainWindow", u"0.50mm", None))
        self.cath_disable_button.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u6b64\u7981\u6b62\u5bfc\u4e1d\u8fd0\u52a8", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u4e1d\u8fdb\u7ed9\u901f\u5ea6", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u4e1d\u5f53\u524d\u4f4d\u7f6e", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u4e1d-\u5bfc\u7ba1\u534f\u540c", None))
        self.cath_mode_select.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5bfc\u7ba1\u5e26\u52a8\u5bfc\u4e1d\u8fd0\u52a8", None))
        self.cath_mode_select.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5bfc\u7ba1\u72ec\u7acb\u8fd0\u52a8", None))

        self.wire_up_button.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u5355\u6b65\u9012\u9001\u6309\u94ae", None))
        self.wire_down_button.setText("")
        self.wire_step_text.setText(QCoreApplication.translate("MainWindow", u"0.50mm", None))
        self.wire_disable_button.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u6b64\u7981\u6b62\u5bfc\u4e1d\u8fd0\u52a8", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u4e1d\u65cb\u8f6c\u901f\u5ea6", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u4e1d\u5f53\u524d\u89d2\u5ea6", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u5355\u6b65\u65cb\u8f6c\u6309\u94ae", None))
        self.wire_antiClock_button.setText("")
        self.wire_clock_button.setText("")
        self.wireRot_step_text.setText(QCoreApplication.translate("MainWindow", u"5.00\u00b0", None))
        self.wire_rot_disable_button.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u6b64\u7981\u6b62\u5bfc\u4e1d\u65cb\u8f6c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u673a\u5668\u4eba\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u9009\u62e9", None))
        self.com_select.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65ad\u5f00\u8fde\u63a5", None))

        self.com_select.setCurrentText(QCoreApplication.translate("MainWindow", u"\u65ad\u5f00\u8fde\u63a5", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u624b\u67c4\u9009\u62e9", None))
        self.joystick_select.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65ad\u5f00\u8fde\u63a5", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6\u6863\u4f4d", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.all_stop_button.setText(QCoreApplication.translate("MainWindow", u"\u673a\u5668\u6025\u505c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u76ae\u80a4", None))
    # retranslateUi

