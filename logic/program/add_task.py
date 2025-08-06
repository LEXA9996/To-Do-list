from logic.time_page import time_setlocal, temp_task
from . import menu
import sqlite3, time
from PySide6.QtWidgets import QMessageBox
from design.py_design.add_task_window import Ui_Dialog
from PySide6.QtWidgets import QDialog
class AddTaskWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self) 
        self.ui.add_task_button.clicked.connect(self.append_task)
    def append_task(self):
            add_task = self.ui.input_description.text().strip()
            if add_task:
                con = sqlite3.connect("TodoList.db")
                c = con.cursor()
                now = time.localtime()
                temp_time_input = self.ui.input_time_task.text().strip()
                end_timestamp = temp_task.temp_time(temp_time_input)
                if not temp_time_input:
                    c.execute("INSERT INTO task (description, status, time, time_end, time_end_str) VALUES (?,?,?,?,? )", (add_task, 
                                                                                                            "active", 
                                                                                                            time_setlocal.format_time(now), 
                                                                                                            temp_task.temp_time(temp_time_input), 
                                                                                                            "Бесконечно"), )
                    time_end_str = c.execute("SELECT time_end_str FROM task WHERE description = ?", (add_task, )).fetchone()
                    con.commit()
                    con.close()
                    msg = QMessageBox(self)
                    msg.setIcon(QMessageBox.Information)
                    msg.setText(    f"✅ Задача «{add_task}» успешно добавлена! 🎉\n"
                                    f"📅 Срок выполнения: {time_end_str[0]}")
                    msg.setWindowTitle("Успех")
                    msg.exec()
                    return
                elif end_timestamp is -1:
                        msg = QMessageBox(self)
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("⏱️ Введите время в формате: «2d 5h 30min»"); 
                        msg.setWindowTitle("Ошибка")
                        msg.exec()
                        return               
                else:
                    time_end_struct = time.localtime(end_timestamp)
                    time_end_str = time_setlocal.format_time(time_end_struct)
                    c.execute("INSERT INTO task (description, status, time, time_end, time_end_str) VALUES (?,?,?,?,? )", (add_task, 
                                                                                                            "active", 
                                                                                                            time_setlocal.format_time(now), 
                                                                                                            temp_task.temp_time(temp_time_input), 
                                                                                                            time_end_str), )
                    con.commit()
                    con.close()
                    msg = QMessageBox(self)
                    msg.setIcon(QMessageBox.Information)
                    msg.setText(    f"✅ Задача «{add_task}» успешно добавлена! 🎉\n"
                                    f"📅 Срок выполнения: {time_end_str}")
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