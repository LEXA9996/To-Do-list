from PySide6.QtWidgets import QDialog, QListWidget, QVBoxLayout
from PySide6.QtWidgets import QMessageBox
from design.py_design.read_competed_window import Ui_Dialog as Ui_CompletedDialog
import sqlite3
class ComletedTask(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CompletedDialog()
        self.ui.setupUi(self)
        self.show_completed()  # Загружаем данные

    def show_completed(self):
        self.ui.complected_task_wid.clear()
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute("SELECT * from task WHERE status = 'completed'")
        task_completed = c.fetchall()
        con.commit()
        con.close()
        if task_completed:
            for index, value in enumerate(task_completed):
                add_text = f"{index + 1}. {value[1]}\n   └ Выложено: {value[3]} | Выполнено: {value[5]}"
                self.ui.complected_task_wid.addItem(add_text)
        else:
            add_text = "Пока нет задач, выполненных за последние 7 дней. 💤"
            self.ui.complected_task_wid.addItem(add_text)