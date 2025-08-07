from PySide6.QtWidgets import QDialog, QListWidget, QVBoxLayout
from PySide6.QtWidgets import QMessageBox
from design.py_design.history_task_window import Ui_Dialog as HistoryDialog
import sqlite3
class ExportHistoryTask(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = HistoryDialog()
        self.ui.setupUi(self)
        self.ui.don_history.clicked.connect(self.export_history)
    def export_history(self):
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute("SELECT * FROM history WHERE status = 'overdue'" )
        overdue_task = c.fetchall()
        c.execute("SELECT * FROM history WHERE status = 'completed'")
        completed_task = c.fetchall()
        name = self.ui.input_filename_history.text()
        if len(name)>100 or len(name)<1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("❗ Введите, пожалуйста, от 1 до 100 символов.")
            msg.setWindowTitle("Ошибка")
            msg.exec()
            return
        else:
            for char in r'\/:*?"<>|':
                name = char.replace(char, "_")
            filename = name
            if not overdue_task and not completed_task:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Warning)
                msg.setText("📭 У вас нет просроченных или выполненных задач.")
                msg.setWindowTitle("Ошибка")
                msg.exec()
                return
            with open(filename+".txt", "w", encoding="utf-8") as f:
                if overdue_task:
                    f.write("┌──────────── ⚠ ПРОСРОЧЕННЫЕ ЗАДАЧИ ────────────┐\n\n")
                    for index, i in enumerate(overdue_task):
                        f.write(f"{index + 1}) {i[1]}\n   ➕ Добавлено: {i[3]}   ❌ Просрочено: {i[5]}\n\n")
                if completed_task:
                    f.write("┌────── ✅ ВЫПОЛНЕННЫЕ ЗАДАЧИ (АРХИВ) ──────┐\n\n")
                    for index, i in enumerate(completed_task):
                        f.write(f"{index + 1}) {i[1]}\n   ➕ Добавлено: {i[3]}   ✔ Выполнено: {i[3]}\n\n")
        con.commit()
        con.close()
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"📄 Файл «{filename}.txt» успешно создан!")
        msg.setWindowTitle("Успех")
        msg.exec()

