# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_BMIView(object):
    def setupUi(self, BMIView):
        if not BMIView.objectName():
            BMIView.setObjectName(u"BMIView")
        BMIView.resize(400, 400)
        BMIView.setMinimumSize(QSize(400, 400))
        BMIView.setMaximumSize(QSize(400, 400))
        icon = QIcon()
        icon.addFile(u":/assets/empty.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        BMIView.setWindowIcon(icon)
        BMIView.setStyleSheet(u"QWidget#BMIView {\n"
"	background-color: #50BFAB;	\n"
"\n"
"}\n"
"\n"
"/* Unit button*/\n"
"QPushButton#btn_unit {\n"
"font-family: Calibri;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"color:#3a9393;\n"
"background-color:#50BFAB;\n"
" text-align: top right; \n"
"padding: 0;\n"
"\n"
"}\n"
"\n"
"QPushButton#btn_unit:hover {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton#btn_unit:pressed {\n"
"background-color: transparent;\n"
"border: none\n"
"}\n"
"\n"
"/* Result Label*/\n"
"QLabel#lbl_result {\n"
"font-family: Calibri;\n"
"font-size: 150px;\n"
"font-weight: bold;\n"
"color:#F2F2F2;\n"
"}\n"
"\n"
"/* weight and height labels*/\n"
"QLabel#lbl_weight,\n"
"QLabel#lbl_height {\n"
"font-family: Calibri;\n"
"font-size: 26px;\n"
"color:#1F1F1F;\n"
"}\n"
"\n"
"/* weight buttons*/\n"
"QPushButton#btn_big_minus,\n"
"QPushButton#btn_small_minus,\n"
"QPushButton#btn_big_plus,\n"
"QPushButton#btn_small_plus {\n"
"font-family: Calibri;\n"
"font-size: 26px;\n"
"color:#1F1F1F;\n"
"background-color: #e8e8e8;\n"
""
                        "border: 2px solid #e8e8e8;\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton#btn_big_minus:hover,\n"
"QPushButton#btn_small_minus:hover,\n"
"QPushButton#btn_big_plus:hover,\n"
"QPushButton#btn_small_plus:hover {\n"
"background-color: #d9d9d9;\n"
"}\n"
"\n"
"QPushButton#btn_big_minus:pressed,\n"
"QPushButton#btn_small_minus:pressed,\n"
"QPushButton#btn_big_plus:pressed,\n"
"QPushButton#btn_small_plus:pressed {\n"
"background-color: #e8e8e8;\n"
"}\n"
"/* Frames*/\n"
"\n"
"QFrame#frame,\n"
"QFrame#frame_2 {\n"
"	background-color: #F2F2F2;\n"
"	border: 2px solid #F2F2F2;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(BMIView)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.btn_unit = QPushButton(BMIView)
        self.btn_unit.setObjectName(u"btn_unit")
        self.btn_unit.setMinimumSize(QSize(65, 0))
        self.btn_unit.setMaximumSize(QSize(65, 16777215))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.btn_unit.setFont(font)
        self.btn_unit.setFlat(True)

        self.verticalLayout_2.addWidget(self.btn_unit, 0, Qt.AlignmentFlag.AlignRight)

        self.lbl_result = QLabel(BMIView)
        self.lbl_result.setObjectName(u"lbl_result")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setBold(True)
        self.lbl_result.setFont(font1)
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_result)

        self.frame = QFrame(BMIView)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_big_minus = QPushButton(self.frame)
        self.btn_big_minus.setObjectName(u"btn_big_minus")
        self.btn_big_minus.setMinimumSize(QSize(60, 60))
        self.btn_big_minus.setMaximumSize(QSize(60, 60))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        self.btn_big_minus.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_big_minus)

        self.btn_small_minus = QPushButton(self.frame)
        self.btn_small_minus.setObjectName(u"btn_small_minus")
        self.btn_small_minus.setMaximumSize(QSize(40, 40))
        self.btn_small_minus.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_small_minus)

        self.lbl_weight = QLabel(self.frame)
        self.lbl_weight.setObjectName(u"lbl_weight")
        self.lbl_weight.setFont(font2)
        self.lbl_weight.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lbl_weight)

        self.btn_small_plus = QPushButton(self.frame)
        self.btn_small_plus.setObjectName(u"btn_small_plus")
        self.btn_small_plus.setMaximumSize(QSize(40, 40))
        self.btn_small_plus.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_small_plus)

        self.btn_big_plus = QPushButton(self.frame)
        self.btn_big_plus.setObjectName(u"btn_big_plus")
        self.btn_big_plus.setMaximumSize(QSize(60, 60))
        self.btn_big_plus.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_big_plus)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(BMIView)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(242, 242, 242, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.frame_2.setPalette(palette)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slider_height = QSlider(self.frame_2)
        self.slider_height.setObjectName(u"slider_height")
        palette1 = QPalette()
        brush1 = QBrush(QColor(80, 191, 171, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush1)
        self.slider_height.setPalette(palette1)
        self.slider_height.setAutoFillBackground(True)
        self.slider_height.setMinimum(100)
        self.slider_height.setMaximum(250)
        self.slider_height.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.slider_height)

        self.lbl_height = QLabel(self.frame_2)
        self.lbl_height.setObjectName(u"lbl_height")
        self.lbl_height.setMinimumSize(QSize(120, 0))
        self.lbl_height.setFont(font2)
        self.lbl_height.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lbl_height)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 2)

        self.retranslateUi(BMIView)

        QMetaObject.connectSlotsByName(BMIView)
    # setupUi

    def retranslateUi(self, BMIView):
        BMIView.setWindowTitle(QCoreApplication.translate("BMIView", u"Form", None))
        self.btn_unit.setText(QCoreApplication.translate("BMIView", u"imperial", None))
        self.lbl_result.setText(QCoreApplication.translate("BMIView", u"22.49", None))
        self.btn_big_minus.setText(QCoreApplication.translate("BMIView", u"-", None))
        self.btn_small_minus.setText(QCoreApplication.translate("BMIView", u"-", None))
        self.lbl_weight.setText(QCoreApplication.translate("BMIView", u"65.0kg", None))
        self.btn_small_plus.setText(QCoreApplication.translate("BMIView", u"+", None))
        self.btn_big_plus.setText(QCoreApplication.translate("BMIView", u"+", None))
        self.lbl_height.setText(QCoreApplication.translate("BMIView", u"1.00ml", None))
    # retranslateUi

