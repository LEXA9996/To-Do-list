# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(498, 712)
        MainWindow.setMinimumSize(QSize(498, 712))
        MainWindow.setMaximumSize(QSize(498, 712))
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #b5e1c3,\n"
"        stop:1 #7fb5b5);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.hello = QLabel(self.centralwidget)
        self.hello.setObjectName(u"hello")
        self.hello.setGeometry(QRect(110, 10, 291, 151))
        self.hello.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    background: transparent;\n"
"}")
        self.hello.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hello.setWordWrap(True)
        self.add_task = QPushButton(self.centralwidget)
        self.add_task.setObjectName(u"add_task")
        self.add_task.setGeometry(QRect(290, 210, 171, 111))
        self.add_task.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_task.setStyleSheet(u"QPushButton {\n"
"    background-color: #3B82F6;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 15px;\n"
"}\n"
"    QPushButton:hover {\n"
"        background-color: #2563EB;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #1D4ED8;\n"
"    }")
        self.read_active_task = QPushButton(self.centralwidget)
        self.read_active_task.setObjectName(u"read_active_task")
        self.read_active_task.setEnabled(True)
        self.read_active_task.setGeometry(QRect(50, 210, 171, 111))
        self.read_active_task.setMinimumSize(QSize(0, 0))
        self.read_active_task.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.read_active_task.setTabletTracking(True)
        self.read_active_task.setStyleSheet(u"QPushButton {\n"
"    background-color: #3B82F6;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 15px;\n"
"}\n"
"    QPushButton:hover {\n"
"        background-color: #2563EB;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #1D4ED8;\n"
"    }")
        icon = QIcon()
        icon.addFile(u":/add_task/icon/list_active.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.read_active_task.setIcon(icon)
        self.read_active_task.setAutoDefault(False)
        self.edit_task = QPushButton(self.centralwidget)
        self.edit_task.setObjectName(u"edit_task")
        self.edit_task.setGeometry(QRect(290, 330, 171, 111))
        self.edit_task.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.edit_task.setStyleSheet(u"QPushButton {\n"
"    background-color: #3B82F6;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 15px;\n"
"}\n"
"    QPushButton:hover {\n"
"        background-color: #2563EB;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #1D4ED8;\n"
"    }")
        self.completed_task = QPushButton(self.centralwidget)
        self.completed_task.setObjectName(u"completed_task")
        self.completed_task.setGeometry(QRect(50, 330, 171, 111))
        self.completed_task.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.completed_task.setStyleSheet(u"QPushButton {\n"
"    background-color: #3B82F6;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 15px;\n"
"}\n"
"    QPushButton:hover {\n"
"        background-color: #2563EB;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #1D4ED8;\n"
"    }")
        self.active_task_history = QPushButton(self.centralwidget)
        self.active_task_history.setObjectName(u"active_task_history")
        self.active_task_history.setGeometry(QRect(50, 570, 171, 111))
        self.active_task_history.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.active_task_history.setStyleSheet(u"QPushButton {\n"
"    background-color: #3B82F6;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 15px;\n"
"}\n"
"    QPushButton:hover {\n"
"        background-color: #2563EB;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #1D4ED8;\n"
"    }")
        self.delete_task_2 = QPushButton(self.centralwidget)
        self.delete_task_2.setObjectName(u"delete_task_2")
        self.delete_task_2.setGeometry(QRect(290, 570, 171, 111))
        self.delete_task_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_task_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #505c52;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    padding: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #3e493f;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #2e382f;\n"
"}\n"
"")
        self.delete_task = QPushButton(self.centralwidget)
        self.delete_task.setObjectName(u"delete_task")
        self.delete_task.setGeometry(QRect(290, 570, 171, 111))
        self.delete_task.setStyleSheet(u"QPushButton {\n"
"    background-color: #3B82F6;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 15px;\n"
"}\n"
"    QPushButton:hover {\n"
"        background-color: #EF4444; \n"
"        color: white;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #DC2626;\n"
"    }")
        self.read_completed_task = QPushButton(self.centralwidget)
        self.read_completed_task.setObjectName(u"read_completed_task")
        self.read_completed_task.setGeometry(QRect(50, 450, 171, 111))
        self.read_completed_task.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.read_completed_task.setStyleSheet(u"QPushButton {\n"
"    background-color: #3B82F6;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 15px;\n"
"}\n"
"    QPushButton:hover {\n"
"        background-color: #2563EB;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #1D4ED8;\n"
"    }")
        self.histoty_task = QPushButton(self.centralwidget)
        self.histoty_task.setObjectName(u"histoty_task")
        self.histoty_task.setGeometry(QRect(290, 450, 171, 111))
        self.histoty_task.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.histoty_task.setStyleSheet(u"QPushButton {\n"
"    background-color: #3B82F6;\n"
"    border-radius: 15px;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    padding: 15px;\n"
"}\n"
"    QPushButton:hover {\n"
"        background-color: #2563EB;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: #1D4ED8;\n"
"    }")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.hello.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c\n"
"\u0432 ToDo List!\n"
"\n"
"\u0427\u0442\u043e \u0432\u044b \u0445\u043e\u0442\u0438\u0442\u0435 \u0441\u0434\u0435\u043b\u0430\u0442\u044c?\n"
"", None))
        self.add_task.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.read_active_task.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0438\u0435\n"
"\u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.edit_task.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.completed_task.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u0442\u0438\u0442\u044c \u043a\u0430\u043a\n"
"\u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u0443\u044e", None))
        self.active_task_history.setText(QCoreApplication.translate("MainWindow", u"C\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0437\u0430 7 \u0434\u043d\u0435\u0439", None))
        self.delete_task_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.delete_task.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.read_completed_task.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0451\u043d\u043d\u044b\u0435\n"
"\u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.histoty_task.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432 \u0437\u0430\u0434\u0430\u0447", None))
    # retranslateUi

