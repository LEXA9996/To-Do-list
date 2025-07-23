from . import menu
import sqlite3, time
def append_task():
    add_task = input("Введите новую задачу ✍️: ")
    if add_task.strip():
        con = sqlite3.connect("TodoList.db")
        c = con.cursor()
        time_str = time_str = time.strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO task (description, status, time) VALUES (?,?,?)", (add_task, "active", time_str))
        con.commit()
        con.close()
        print("Задача успешно добавлена! 🎉")
    else:
        print("Пустая задача не может быть добавлена. 🚫")
    menu.back_menu()
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
                time_str = time.strftime("%Y-%m-%d %H:%M:%S")
                c.execute("UPDATE task SET status = ?, time = ? WHERE id = ?", ("completed", time_str, complet_id))
                con.commit()
                print(f"Задача '{complet_text}' успешно отмечена как выполненная! 🎉")
                break
        except ValueError:
            print("Пожалуйста, вводите только цифры. 🚫")
    con.close()
    menu.back_menu()