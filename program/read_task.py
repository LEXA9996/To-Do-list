from . import menu
import sqlite3
def show_completed():
    con = sqlite3.connect("ToDoList.db")
    c = con.cursor()
    c.execute("SELECT * from task WHERE status = 'completed'")
    task_completed = c.fetchall()
    if not task_completed:
        print("Пока нет задач, выполненных за последние 7 дней. 💤")
        menu.back_menu()
    else:
        print("\nСписок выполненных задач за 7 дней🎊:")
        for index, value in enumerate(task_completed):
            print(f"{index + 1}. {value[1]}\n   └ Выложено: {value[3]} | Выполнено: {value[5]}")
    menu.back_menu()
def read_task():
    con = sqlite3.connect("ToDoList.db")
    c = con.cursor()
    c.execute("SELECT * from task WHERE status = 'active'")
    task = c.fetchall()
    if not task:
        print("У вас пока нет активных задач. Добавьте новую! 😊")
    else:
        print("\nСписок текущих задач 📋:")
        for index, item in enumerate(task):
            if item[4] is None:
                print(f"{index+1}. {item[1]} — добавлено: {item[3]} | срок: бесконечно")
            else:
                print(f"{index+1}. {item[1]} — добавлено: {item[3]} | срок: {item[5]}")
    con.commit()
    con.close()
    menu.back_menu()