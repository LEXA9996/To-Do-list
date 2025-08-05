# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'read_competed_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(857, 764)
        Dialog.setMinimumSize(QSize(857, 764))
        Dialog.setMaximumSize(QSize(857, 764))
        Dialog.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #b5e1c3,\n"
"        stop:1 #7fb5b5);\n"
"}\n"
"")
        self.label_text_complect_text = QLabel(Dialog)
        self.label_text_complect_text.setObjectName(u"label_text_complect_text")
        self.label_text_complect_text.setGeometry(QRect(-60, 10, 941, 91))
        self.label_text_complect_text.setMinimumSize(QSize(941, 0))
        self.label_text_complect_text.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: #2E86C1;               /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 \u0446\u0432\u0435\u0442 */\n"
"    font-size: 18pt;              /* \u043a\u0440\u0443\u043f\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-weight: bold;            /* \u0436\u0438\u0440\u043d\u044b\u0439 */\n"
"    padding: 8px 15px;\n"
"    border-bottom: 3px solid #2E86C1;  /* \u0430\u043a\u0446\u0435\u043d\u0442\u043d\u0430\u044f \u043b\u0438\u043d\u0438\u044f \u0441\u043d\u0438\u0437\u0443 */\n"
"    margin-bottom: 10px;\n"
"}")
        self.label_text_complect_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.complected_task_wid = QListWidget(Dialog)
        self.complected_task_wid.setObjectName(u"complected_task_wid")
        self.complected_task_wid.setGeometry(QRect(-10, 100, 861, 651))
        self.complected_task_wid.setStyleSheet(u"QListWidget {\n"
"    background-color: transparent;       /* \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 1.5px solid #cccccc;         /* \u0442\u043e\u043d\u043a\u0430\u044f \u0441\u0432\u0435\u0442\u043b\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 10px;                  /* \u0441\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 5px;\n"
"    font-size: 13pt;\n"
"    color: #333333;\n"
"    selection-background-color: #448aff; /* \u0441\u0438\u043d\u0438\u0439 \u0444\u043e\u043d \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f */\n"
"    selection-color: white;               /* \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u044f */\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_text_complect_text.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u0432\u0435\u0440\u0448\u0451\u043d\u043d\u044b\u0445 \u0437\u0430\u0434\u0430\u0447 \u0437\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 7 \u0434\u043d\u0435\u0439", None))
    # retranslateUi

