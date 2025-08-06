import sqlite3, time
from logic.time_page import temp_task, time_setlocal
from PySide6.QtWidgets import QDialog, QListWidget, QVBoxLayout
from PySide6.QtWidgets import QMessageBox
from design.py_design.mark_completed_window import Ui_Dialog as Ui_CompletedDialog
import sqlite3
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
class MarkCompletedTask(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CompletedDialog()
        self.ui.setupUi(self)
        self.load_tasks()
        self.ui.comlected_buton.clicked.connect(self.mark_completed)
    def mark_completed(self):
        select_index = self.ui.combo_active_task_box.currentIndex()

        if select_index == -1 or self.ui.combo_active_task_box.currentData() is None:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Пожалуйста, выберите задачу из списка.")
            msg.setWindowTitle("Ошибка")
            msg.exec()
            return

        complet_id = self.ui.combo_active_task_box.currentData()
        complet_text = self.ui.combo_active_task_box.currentText()
        time_end_str = time.localtime()

        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute(
            "UPDATE task SET status = ?, time_end = ?, time_end_str = ? WHERE id = ?",
            ("completed", temp_task.temp_time("7d"), time_setlocal.format_time(time_end_str), complet_id)
        )
        con.commit()
        con.close()

        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Задача «{complet_text}» успешно отмечена как выполненная. 🎉")
        msg.setWindowTitle("Успех")
        msg.exec()

        self.load_tasks()
    def load_tasks(self):
        self.ui.combo_active_task_box.clear()
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute("SELECT id, description FROM task WHERE status = 'active'")
        tasks = c.fetchall()
        con.close()

        if not tasks:
            self.ui.combo_active_task_box.addItem("Нет активных задач 😌")
            self.ui.comlected_buton.setEnabled(False)
            self.ui.comlected_buton.setCursor(QCursor(Qt.ForbiddenCursor))
        else:
            for task_id, description in tasks:
                self.ui.combo_active_task_box.addItem(description, userData=task_id)
            self.ui.comlected_buton.setEnabled(True)
