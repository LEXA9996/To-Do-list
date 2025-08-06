import sqlite3, time
from logic.time_page import temp_task, time_setlocal
from PySide6.QtWidgets import QDialog, QListWidget, QVBoxLayout
from PySide6.QtWidgets import QMessageBox
from design.py_design.delete_task_window import Ui_Dialog as Ui_DeleteDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
class DeleteTask(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DeleteDialog()
        self.ui.setupUi(self)
        self.load_tasks()
        self.ui.delete_button.clicked.connect(self.delete_task)
    def delete_task(self):
        select_index = self.ui.combo_delete_task_box.currentIndex()
        if select_index == -1 or self.ui.combo_delete_task_box.currentData() is None:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Пожалуйста, выберите задачу из списка.")
            msg.setWindowTitle("Ошибка")
            msg.exec()
            return
        task_id = self.ui.combo_delete_task_box.currentData()
        task_text = self.ui.combo_delete_task_box.currentText()
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()

        c.execute("DELETE from task WHERE id = ?",(task_id, ))
        con.commit()
        con.close()
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Задача «{task_text}» была успешно удалена. 🗑️")
        msg.setWindowTitle("Успех")
        msg.exec()
    def load_tasks(self):
        self.ui.combo_delete_task_box.clear()
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute("SELECT id, description FROM task WHERE status = 'active'")
        task = c.fetchall()
        if not task:
            self.ui.combo_delete_task_box.addItem("Список задач пуст. Нет задач для удаления. 😕")
            self.ui.delete_button.setEnabled(False)
            self.ui.delete_button.setCursor(QCursor(Qt.ForbiddenCursor))
        else:
            for task_id, des in task:
                self.ui.combo_delete_task_box.addItem(des, userData = task_id)
            self.ui.delete_button.setEnabled(True)