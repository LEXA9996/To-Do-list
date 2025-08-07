from PySide6.QtWidgets import QDialog, QListWidget, QVBoxLayout
from PySide6.QtWidgets import QMessageBox
from design.py_design.active_task_window_don import Ui_Dialog as Ui_DonActive
import sqlite3
class ExpostTask(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DonActive()
        self.ui.setupUi(self)
        self.ui.don_active.clicked.connect(self.export_task)
    def export_task(self):
        conn = sqlite3.connect("ToDoList.db")
        c = conn.cursor()
        c.execute("SELECT * FROM task WHERE status = 'active'")
        aktive_task = c.fetchall()
        c.execute("SELECT * FROM task WHERE status = 'completed'")
        completed_task = c.fetchall()
        name = self.ui.input_filename_active.text()
        if len(name)>100 or len(name)<1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("❗ Введите, пожалуйста, от 1 до 100 символов.")
            msg.setWindowTitle("Ошибка")
            msg.exec()
            return
        else:
            for char in r'\/:*?"<>|':
                name = name.replace(char, "_")
            filename = name
            if not aktive_task and not completed_task:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Warning)
                msg.setText("📭 У вас нет активных или выполненных задач.")
                msg.setWindowTitle("Ошибка")
                msg.exec()
                return
            with open(filename+".txt", "w", encoding="utf-8") as f:
                if aktive_task:
                    f.write("┌────────────────────── 📌 АКТИВНЫЕ ЗАДАЧИ ──────────────────────┐\n\n")
                    for index, i in enumerate(aktive_task):
                        if i[4] is None:
                            f.write(f"{index + 1}) {i[1]}\n   ➤ Добавлено: {i[3]}  ⏳ Срок: бесконечный\n\n")
                        else:
                            f.write(f"{index + 1}) {i[1]}\n   ➤ Добавлено: {i[3]}  ⏳ Срок: {i[5]}\n\n")
                if completed_task:
                    f.write("┌──────────── ✅ ВЫПОЛНЕННЫЕ ЗАДАЧИ ЗА 7 ДНЕЙ ────────────┐\n\n")
                    for index, i in enumerate(completed_task):
                        f.write(f"{index + 1}) {i[1]}\n   ➕ Добавлено: {i[5]}   ✔ Выполнено: {i[3]}\n\n")
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"📄 Файл «{filename}.txt» успешно создан!")
        msg.setWindowTitle("Успех")
        msg.exec()
        conn.close()