from . import menu
import sqlite3
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QDialog, QListWidget, QVBoxLayout
from design.py_design.read_task_active_window import Ui_Dialog
class ActiveComletedTaskWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()#Создаём UI
        self.ui.setupUi(self)#Привязываем UI к текущему окну
        self.read_task()# Загружаем данные
    def read_task(self):
        self.ui.active_task_wid.clear()
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute("SELECT * from task WHERE status = 'active'")
        task = c.fetchall()
        con.commit()
        con.close()
        if not task:
            task_text = "У вас пока нет активных задач. Добавьте новую! 😊"
            self.ui.active_task_wid.addItem(task_text)
        else:
            for index, item in enumerate(task):
                deadline = "бесконечно" if item[4] is None else item[5]
                task_text = f"{index+1}) {item[1]} — добавлено: {item[3]} | срок: {deadline}"
                self.ui.active_task_wid.addItem(task_text)