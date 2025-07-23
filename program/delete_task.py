from . import menu
import sqlite3
def delete_task():
    con = sqlite3.connect("ToDoList.db")
    c = con.cursor()
    c.execute("SELECT * from task WHERE status = 'active'")
    task = c.fetchall()
    if not task:
        print("Список задач пуст. Нет задач для удаления. 😕")
        menu.back_menu()
        return

    print("\nСписок задач 📝:")
    for index, value in enumerate(task):
        print(f"{index + 1}. {value[1]}")

    while True:
        try:
            delete = int(input("Введите номер задачи, которую хотите удалить 🗑️: "))
            if delete < 1 or delete > len(task):
                print(f"Ошибка: введите число от 1 до {len(task)}. ⚠️")
            else:
                task_id = task[delete - 1][0]
                task_text = task[delete - 1][1]
                c.execute("DELETE from task WHERE id = ?",(task_id, ))
                con.commit()
                print(f"Задача '{task_text}' была удалена. 🗑️")
                break
        except ValueError:
            print("Ошибка: вводите только цифры. 🚫")
    con.close()
    menu.back_menu()