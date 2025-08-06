import sqlite3,time, locale
from logic.time_page import temp_task, time_setlocal
from PySide6.QtWidgets import QDialog, QListWidget, QVBoxLayout
from PySide6.QtWidgets import QMessageBox
from design.py_design.edit_task_window import Ui_Dialog as Ui_EditDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
class EditTask(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EditDialog()
        self.ui.setupUi(self)
        self.load_tasks()
        self.ui.comlected_button_edit.clicked.connect(self.edit)
    def edit(self):
        conn = sqlite3.connect("TodoList.db")
        c = conn.cursor()
        task_id = self.ui.combo_active_task_edit_box.currentData()
        task_text = c.execute("SELECT description FROM task WHERE id = ?", (task_id,)).fetchone()
        task_edit_text = self.ui.input_edit_task.text().strip()
        now = time.localtime()
        task_edit_time = self.ui.Input_time_edit_task.text().strip()
        end_timestamp = temp_task.temp_time(task_edit_time)
        time_end = c.execute("SELECT time_end_str FROM task WHERE id = ?", (task_id,)).fetchone()
        if task_edit_text.strip():
            if not task_edit_time:
                c.execute("UPDATE task SET description = ?, time = ? WHERE id = ?",(task_edit_text, time_setlocal.format_time(now), task_id))
                conn.commit()
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Information)    
                msg.setText(
                    f"✅ Задача успешно обновлена! 🎉\n\n"
                    f"📝 Было: «{task_text[0]}»\n"
                    f"✏️ Стало: «{task_edit_text}»\n"
                    f"📅 Срок остался прежним: {time_end[0]}"
                )
                msg.setWindowTitle("Успех")
                msg.exec()  
                return
            elif end_timestamp is -1:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Warning)    
                msg.setText("❌ Неверный формат времени. Пример: '1d 3h 20min'")
                msg.setWindowTitle("Ошибка")
                msg.exec()
            else:
                time_end_struct = time.localtime(end_timestamp)
                time_end_str = time_setlocal.format_time(time_end_struct)
                c.execute("UPDATE task SET description = ?, time = ?, time_end = ?, time_end_str = ? WHERE id = ?",(task_edit_text, time_setlocal.format_time(now), temp_task.temp_time(task_edit_time), time_end_str,  task_id))
                conn.commit()
                conn.close()
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Information)
                msg.setText(
                    f"✅ Задача успешно обновлена! 🎉\n\n"
                    f"📝 Было: «{task_text[0]}»\n"
                    f"✏️ Стало: «{task_edit_text}»\n"
                    f"📅 Новый срок: {time_end[0]}"
                )
                msg.setWindowTitle("Успех")
                msg.exec()
                return
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Пожалуйста, введите описание задачи — оно не может быть пустым.")
            msg.setWindowTitle("Ошибка")
            msg.exec()
            return
    def load_tasks(self):
        self.ui.combo_active_task_edit_box.clear()
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute("SELECT id, description FROM task WHERE status = 'active'")
        task = c.fetchall()
        if not task:
            self.ui.combo_active_task_edit_box.addItem("У вас нету активных задач!😦")
            self.ui.comlected_button_edit.setEnabled(False)
            self.ui.comlected_button_edit.setCursor(QCursor(Qt.ForbiddenCursor))
        else:
            for task_id, des in task:
                self.ui.combo_active_task_edit_box.addItem(des, userData = task_id)
            self.ui.comlected_button_edit.setEnabled(True)