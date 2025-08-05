import sqlite3, time
from logic.time_page import temp_task, time_setlocal
def mark_completed():
    con = sqlite3.connect("ToDoList.db")
    c = con.cursor()
    c.execute("SELECT * from task WHERE status = 'active'")
    task = c.fetchall()
    if not task:
        print("У вас нет активных задач для отметки. 😌")
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