# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(542, 418)
        icon = QIcon()
        icon.addFile(u":/icons/outline_key_black_24dp.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #121212;\n"
"    color: white;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_lower,\n"
"#btn_upper,\n"
"#btn_digits,\n"
"#btn_special {\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #090;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #090;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #006300;\n"
"    border-color: #090;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.icon_lock = QPushButton(self.centralwidget)
        self.icon_lock.setObjectName(u"icon_lock")
        self.icon_lock.setStyleSheet(u"border: none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/lock_white_24dp.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.icon_lock.setIcon(icon1)
        self.icon_lock.setIconSize(QSize(100, 100))
        self.icon_lock.setCheckable(False)
        self.icon_lock.setChecked(False)

        self.verticalLayout.addWidget(self.icon_lock)

        self.layout_password = QHBoxLayout()
        self.layout_password.setObjectName(u"layout_password")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    margin: 0;\n"
"    font-size: 20pt;\n"
"}")

        self.layout_password.addWidget(self.lineEdit)

        self.btn_invisible = QPushButton(self.centralwidget)
        self.btn_invisible.setObjectName(u"btn_invisible")
        self.btn_invisible.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_invisible.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    margin: 0;\n"
"    background-color: transparent;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/visibility_off_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_invisible.setIcon(icon2)
        self.btn_invisible.setIconSize(QSize(30, 30))
        self.btn_invisible.setCheckable(True)
        self.btn_invisible.setChecked(True)

        self.layout_password.addWidget(self.btn_invisible)

        self.btn_visible = QPushButton(self.centralwidget)
        self.btn_visible.setObjectName(u"btn_visible")
        self.btn_visible.setStyleSheet(u"QPushButton {\n"
"    margin-right: 0;\n"
"    margin-left: 0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/visibility_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_visible.setIcon(icon3)
        self.btn_visible.setIconSize(QSize(52, 52))
        self.btn_visible.setCheckable(True)

        self.layout_password.addWidget(self.btn_visible)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setStyleSheet(u"QPushButton {\n"
"    padding: 5px;\n"
"    margin-left: 0;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/content_copy_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_copy.setIcon(icon4)
        self.btn_copy.setIconSize(QSize(42, 42))
        self.btn_copy.setCheckable(True)

        self.layout_password.addWidget(self.btn_copy)


        self.verticalLayout.addLayout(self.layout_password)

        self.layout_info = QHBoxLayout()
        self.layout_info.setObjectName(u"layout_info")
        self.label_strength = QLabel(self.centralwidget)
        self.label_strength.setObjectName(u"label_strength")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_strength.sizePolicy().hasHeightForWidth())
        self.label_strength.setSizePolicy(sizePolicy1)
        self.label_strength.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.label_strength)

        self.label_entropy = QLabel(self.centralwidget)
        self.label_entropy.setObjectName(u"label_entropy")
        sizePolicy1.setHeightForWidth(self.label_entropy.sizePolicy().hasHeightForWidth())
        self.label_entropy.setSizePolicy(sizePolicy1)
        self.label_entropy.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.label_entropy)


        self.verticalLayout.addLayout(self.layout_info)

        self.layout_strength = QHBoxLayout()
        self.layout_strength.setObjectName(u"layout_strength")
        self.slider_length = QSlider(self.centralwidget)
        self.slider_length.setObjectName(u"slider_length")
        self.slider_length.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #090;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background-color: gray;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"    width: 22px;\n"
"    border-radius: 10px;\n"
"    margin-top: -8px;\n"
"    margin-bottom: -8px;\n"
"}\n"
"\n"
"")
        self.slider_length.setMaximum(100)
        self.slider_length.setValue(12)
        self.slider_length.setOrientation(Qt.Horizontal)

        self.layout_strength.addWidget(self.slider_length)

        self.spinBox_length = QSpinBox(self.centralwidget)
        self.spinBox_length.setObjectName(u"spinBox_length")
        self.spinBox_length.setStyleSheet(u"QSpinBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    background: transparent;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border-color: #009900;\n"
"}")
        self.spinBox_length.setAlignment(Qt.AlignCenter)
        self.spinBox_length.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.layout_strength.addWidget(self.spinBox_length)


        self.verticalLayout.addLayout(self.layout_strength)

        self.layout_characters = QHBoxLayout()
        self.layout_characters.setObjectName(u"layout_characters")
        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_characters.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_characters.addWidget(self.btn_upper)

        self.btn_digits = QPushButton(self.centralwidget)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setCheckable(True)
        self.btn_digits.setChecked(True)

        self.layout_characters.addWidget(self.btn_digits)

        self.btn_special = QPushButton(self.centralwidget)
        self.btn_special.setObjectName(u"btn_special")
        self.btn_special.setCheckable(True)

        self.layout_characters.addWidget(self.btn_special)


        self.verticalLayout.addLayout(self.layout_characters)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.icon_lock.setText("")
        self.btn_invisible.setText("")
        self.btn_visible.setText("")
        self.btn_copy.setText("")
        self.label_strength.setText("")
        self.label_entropy.setText("")
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_special.setText(QCoreApplication.translate("MainWindow", u"#$%", None))
    # retranslateUi

