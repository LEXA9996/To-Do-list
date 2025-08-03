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
    def show_completed(self):
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute("SELECT * from task WHERE status = 'completed'")
        task_completed = c.fetchall()
        if not task_completed:
            print("Пока нет задач, выполненных за последние 7 дней. 💤")
        else:
            print("\nСписок выполненных задач за 7 дней🎊:")
            for index, value in enumerate(task_completed):
                print(f"{index + 1}. {value[1]}\n   └ Выложено: {value[3]} | Выполнено: {value[5]}")
    def read_task(self):
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute("SELECT * from task WHERE status = 'active'")
        task = c.fetchall()
        con.commit()
        con.close()
        self.ui.active_task_wid.clear()
        if not task:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Ошибка")
            msg.setText("Что-то пошло не так 😢")
            msg.setInformativeText("У вас нету активных задач.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            return
        else:
            for index, item in enumerate(task):
                deadline = "бесконечно" if item[4] is None else item[5]
                task_text = f"{index+1}) {item[1]} — добавлено: {item[3]} | срок: {deadline}"
                self.ui.active_task_wid.addItem(task_text)