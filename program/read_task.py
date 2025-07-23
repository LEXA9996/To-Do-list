from . import menu
import sqlite3
def show_completed():
    con = sqlite3.connect("ToDoList.db")
    c = con.cursor()
    c.execute("SELECT * from task WHERE status = 'completed'")
    task_completed = c.fetchall()
    if not task_completed:
        print("Пока нет выполненных задач. Вперед к делам! 🚀")
        menu.back_menu()
    else:
        print("\nСписок выполненных задач 🎊:")
        for index, value in enumerate(task_completed):
            print(f"{index + 1}. {value[1]}. Выполнено в {value[3]}")
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
            print(f'{index+1}. {item[1]}. Добавлено в {item[3]}')
    con.commit()
    con.close()
    menu.back_menu()