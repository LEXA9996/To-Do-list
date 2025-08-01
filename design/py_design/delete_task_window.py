# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_task_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(447, 529)
        Dialog.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #b5e1c3,\n"
"        stop:1 #7fb5b5);\n"
"}\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-80, 0, 601, 121))
        self.label.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2E86C1;               /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u0446\u0432\u0435\u0442 */\n"
"    font-size: 18pt;              /* \u043a\u0440\u0443\u043f\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-weight: bold;            /* \u0436\u0438\u0440\u043d\u044b\u0439 */\n"
"    padding: 8px 15px;\n"
"    border-bottom: 3px solid #2E86C1;  /* \u0430\u043a\u0446\u0435\u043d\u0442\u043d\u0430\u044f \u043b\u0438\u043d\u0438\u044f \u0441\u043d\u0438\u0437\u0443 */\n"
"    margin-bottom: 10px;\n"
"}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 130, 431, 101))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;    /* \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #333333;                   /* \u0442\u0451\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-size: 14pt;                  /* \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: 600;                 /* \u0447\u0443\u0442\u044c \u0436\u0438\u0440\u043d\u0435\u0435 */\n"
"    padding: 4px 8px;                 /* \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border-radius: 6px;               /* \u0441\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    border: 1px solid #cccccc;       /* \u0442\u043e\u043d\u043a\u0430\u044f \u0441\u0432\u0435\u0442\u043b\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    /* \u043c\u043e"
                        "\u0436\u043d\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043b\u0451\u0433\u043a\u0443\u044e \u0442\u0435\u043d\u044c \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);\n"
"}\n"
"")
        self.combo_delete_task_box = QComboBox(Dialog)
        self.combo_delete_task_box.setObjectName(u"combo_delete_task_box")
        self.combo_delete_task_box.setGeometry(QRect(40, 260, 351, 61))
        self.combo_delete_task_box.setStyleSheet(u"QComboBox {\n"
"    background-color: #fefefe;      /* \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0444\u043e\u043d \u043f\u043e\u043b\u044f */\n"
"    color: #222222;                 /* \u0442\u0451\u043c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0432 \u043f\u043e\u043b\u0435 */\n"
"    border: 2px solid #3B82F6;\n"
"    border-radius: 12px;\n"
"    padding: 6px 15px 6px 10px;\n"
"    font-size: 14pt;\n"
"    min-width: 150px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #2563EB;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: #1D4ED8;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* \u0422\u0435\u043a\u0441\u0442 \u0432 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u043c \u0441\u043f\u0438\u0441\u043a\u0435 */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #fefefe;      /* \u0441\u0432\u0435\u0442\u043b\u044b"
                        "\u0439 \u0444\u043e\u043d \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    color: #222222;                 /* \u0442\u0451\u043c\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    selection-background-color: #3B82F6; /* \u0441\u0438\u043d\u0438\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0438 */\n"
"    selection-color: white;         /* \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u043f\u0440\u0438 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0438 */\n"
"    border: 1px solid #3B82F6;\n"
"}\n"
"\n"
"/* \u0423\u0431\u0435\u0440\u0438 \u043b\u044e\u0431\u044b\u0435 \u0441\u0442\u0438\u043b\u0438 \u0434\u043b\u044f down-arrow, \u0447\u0442\u043e\u0431\u044b \u0441\u0442\u0440\u0435\u043b\u043a\u0430 \u0431\u044b\u043b\u0430 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u043e\u0439 */\n"
"")
        self.delete_button = QPushButton(Dialog)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(80, 350, 261, 101))
        self.delete_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #3B82F6;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 15px 25px;\n"
"    border: none;\n"
"    transition: background-color 0.25s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2563EB;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1D4ED8;\n"
"}\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0430\u043a\u0442\u0438\u0432\u043d\u0443\u044e \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u043d\u0438\u0437\u0443 \u2014 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0438\u0439 \u0441\u043f\u0438\u0441\u043e\u043a.  \n"
"\u041e\u0442\u043c\u0435\u0442\u044c\u0442\u0435 \u0437\u0430\u0434\u0430\u0447\u0443, \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u0443\u0434\u0430\u043b\u0438\u0442\u044c.", None))
        self.delete_button.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
    # retranslateUi

