from logic.time_page import time_setlocal, temp_task
from . import menu
import sqlite3, time
def append_task():
    while True:
        add_task = input("Введите новую задачу ✍️: ")
        if add_task.strip():
            con = sqlite3.connect("TodoList.db")
            c = con.cursor()
            now = time.localtime()
            while True:
                temp_time_input = input(
                    "\n📆 Укажите срок задачи:\n"
                    "Например:\n"
                    "  - 3d         → 3 дня\n"
                    "  - 2h 30min   → 2 часа 30 минут\n"
                    "  - 1m 5d 2h   → 1 месяц, 5 дней и 2 часа\n"
                    "  - 0          → бесконечная задача ♾️\n\n"
                    "Введите срок: ").strip()
                end_timestamp = temp_task.temp_time(temp_time_input)
                if temp_time_input:
                    error = temp_task.temp_time(temp_time_input)
                    if error is -1:
                        print("❌ Неверный формат времени. Пример: '1d 3h 20min'")
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
                        print("Задача успешно добавлена! 🎉")
                        menu.back_menu()
                        break
        else:
            print("Пустая задача не может быть добавлена. 🚫")
            continue
def mark_completed():
    con = sqlite3.connect("ToDoList.db")
    c = con.cursor()
    c.execute("SELECT * from task WHERE status = 'active'")
    task = c.fetchall()
    if not task:
        print("У вас нет активных задач для отметки. 😌")
        menu.back_menu()
        return

    print("\nСписок текущих задач 📋:")
    for index, value in enumerate(task):
        print(f"{index + 1}. {value[1]}.")

    while True:
        try:
            complet = int(input("Введите номер задачи, которую вы выполнили ✅: "))
            if complet < 1 or complet > len(task):
                print(f"Пожалуйста, введите число от 1 до {len(task)}. ⚠️")
            else:
                complet_id = task[complet - 1][0]
                complet_text = task[complet -1][1]
                time_end_str = time.localtime()
                
                c.execute("UPDATE task SET status = ?, time_end = ?, time_end_str = ? WHERE id = ?", ("completed",temp_task.temp_time("7d"), time_setlocal.format_time(time_end_str), complet_id))
                con.commit()
                print(f"Задача '{complet_text}' успешно отмечена как выполненная! 🎉")
                break
        except ValueError:
            print("Пожалуйста, вводите только цифры. 🚫")
    con.close()
    menu.back_menu()