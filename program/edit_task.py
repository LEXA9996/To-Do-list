import sqlite3,time, locale

from time_page import time_setlocal, temp_task
from . import menu

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
def edit():
    conn = sqlite3.connect("TodoList.db")
    c = conn.cursor()
    c.execute("SELECT * FROM task WHERE status = 'active'")
    task = c.fetchall()
    if not task:
        print("У вас нету активных задач")
        menu.back_menu()
    print("Список актвных задач")
    for index, item in enumerate(task):
        print(f"{index+1}. {item[1]}")
    while True:
        try:
            edit_task = int(input("Выберите задачу"))
            if edit_task> len(task) or edit_task<1:
                print("Пожалуйста, введите в предела диапазона")
                continue
            else:
                task_id = task[edit_task - 1][0]
                task_text = task[edit_task - 1][1]
                while True:
                    task_edit_text = input("Введите, как вы хотите изменить задачу: ")
                    now = time.localtime()
                    task_edit_time = input("Введите, на какое время, вы хотите изменить задачу.\n Если вы не хотите изменить срок, напишите q: ")
                    end_timestamp = temp_task.temp_time(task_edit_time)
                    if task_edit_text.strip():
                        if task_edit_time == "q":
                            temp_task.temp_time
                            c.execute("UPDATE task SET description = ?, time = ? WHERE id = ?",(task_edit_text, time_setlocal.format_time(now), task_id))
                            conn.commit()
                            print(f"✅ Задача обновлена! Было: '{task_text}'\n→ Стало: '{task_edit_text}'.")
                            break
                        elif end_timestamp is -1:
                            print("❌ Неверный формат времени. Пример: '1d 3h 20min'")
                            continue
                        else:
                            time_end_struct = time.localtime(end_timestamp)
                            time_end_str = time_setlocal.format_time(time_end_struct)
                            c.execute("UPDATE task SET description = ?, time = ?, time_end = ?, time_end_str = ? WHERE id = ?",(task_edit_text, time_setlocal.format_time(now), temp_task.temp_time(task_edit_time), time_end_str,  task_id))
                            conn.commit()
                            conn.close()
                            print(f"✅ Задача обновлена! Было: '{task_text}'\n→ Стало: '{task_edit_text}'. Срок: {time_end_str}")
                            menu.back_menu()
                            break
                    else:
                        print("Задача не может сать пустой")
                        continue
        except ValueError:
            print("Введите только цифры")
            continue