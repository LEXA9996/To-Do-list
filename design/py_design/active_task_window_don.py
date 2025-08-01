# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'active_task_window_don.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(473, 484)
        Dialog.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #b5e1c3,\n"
"        stop:1 #7fb5b5);\n"
"}\n"
"")
        self.input_filename_active = QLineEdit(Dialog)
        self.input_filename_active.setObjectName(u"input_filename_active")
        self.input_filename_active.setGeometry(QRect(20, 270, 431, 51))
        self.input_filename_active.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc;         /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;                /* \u0441\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px 12px;                 /* \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 14pt;                   /* \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    background-color: #fefefe;         /* \u043f\u043e\u0447\u0442\u0438 \u0431\u0435\u043b\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: #333333;                    /* \u0442\u0451\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    transition: border-color 0.3s ease; /* \u043f\u043b\u0430\u0432\u043d\u043e\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0440\u0430\u043c\u043a\u0438 "
                        "*/\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #448aff;             /* \u044f\u0440\u043a\u043e-\u0441\u0438\u043d\u0438\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"    background-color: #ffffff;         /* \u0431\u0435\u043b\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"    outline: none;                     /* \u0443\u0431\u0438\u0440\u0430\u0435\u043c \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u043e\u0435 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435 */\n"
"}\n"
"    QLineEdit::placeholder {\n"
"        color: #999999;\n"
"        font-style: italic;\n"
"    }")
        self.input_filename_active.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.add_task_label_des_2 = QLabel(Dialog)
        self.add_task_label_des_2.setObjectName(u"add_task_label_des_2")
        self.add_task_label_des_2.setGeometry(QRect(-90, 30, 651, 101))
        self.add_task_label_des_2.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2E86C1;               /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u0446\u0432\u0435\u0442 */\n"
"    font-size: 15pt;              /* \u043a\u0440\u0443\u043f\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-weight: bold;            /* \u0436\u0438\u0440\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    padding: 8px 15px;\n"
"    border-bottom: 3px solid #2E86C1;  /* \u043d\u0438\u0436\u043d\u044f\u044f \u0446\u0432\u0435\u0442\u043d\u0430\u044f \u043b\u0438\u043d\u0438\u044f \u2014 \u0430\u043a\u0446\u0435\u043d\u0442 */\n"
"    margin-bottom: 10px;\n"
"}\n"
"")
        self.add_task_label_des_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.don_active = QPushButton(Dialog)
        self.don_active.setObjectName(u"don_active")
        self.don_active.setGeometry(QRect(120, 390, 231, 51))
        self.don_active.setStyleSheet(u"QPushButton {\n"
"    background-color: #448aff;          /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: white;                       /* \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;                      /* \u0431\u0435\u0437 \u0440\u0430\u043c\u043a\u0438 */\n"
"    border-radius: 10px;               /* \u0441\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 10px 20px;                /* \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 14pt;                   /* \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: bold;                 /* \u0436\u0438\u0440\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-col"
                        "or: #2979ff;          /* \u0431\u043e\u043b\u0435\u0435 \u044f\u0440\u043a\u0438\u0439 \u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c54b2;          /* \u0442\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 170, 281, 71))
        self.label.setStyleSheet(u"QLabel {\n"
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

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.input_filename_active.setText("")
        self.add_task_label_des_2.setText(QCoreApplication.translate("Dialog", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u0430\u0440\u0445\u0438\u0432 \u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u0438 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u0434\u0430\u0447  \n"
"\u0437\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 7 \u0434\u043d\u0435\u0439.", None))
        self.don_active.setText(QCoreApplication.translate("Dialog", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u043a \u0432\u044b\u0445\u043e\u0442\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u0442\u044c \u0444\u0430\u0439\u043b?", None))
    # retranslateUi

