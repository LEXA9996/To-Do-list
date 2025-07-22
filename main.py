import json, os, sqlite3
import time
# if os.path.exists("tasks.json"):
#     with open("tasks.json", "r") as read_task:
#         try:
#             data = json.load(read_task)
#             task = data.get("active", [])
#             task_completed = data.get("completed", [])
#         except json.JSONDecodeError:
#             task = []
#             task_completed = []
# else:
#     with open("tasks.json", "w") as write_task:
#         json.dump({"active": [], "completed": []}, write_task)
#     task = []
#     task_completed = []
def create_table():
    if os.path.exists("ToDoList.db"):
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        con.commit()
        con.close()
    else:
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute("""
        CREATE TABLE task(
        id INTEGER PRIMARY KEY AUTOINCREMENT,     
        description TEXT NOT NULL,
        status TEXT NOT NULL,
        time TEXT)""")
        con.commit()
        con.close()

def back_menu():
    while True:
        return_menu = input("Хотите вернуться в меню? Да [y] 😊, Нет [n] 👋: ")
        if return_menu.lower() == "y":
            menu()
            break
        elif return_menu.lower() == "n":
            print("Спасибо за использование программы! До свидания! 👋")
            break
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова. 🤔")
            continue


def menu():
    while True:
        try:
            choice = int(input(
                "\nЗдравствуйте! 👋\nВыберите действие:\n"
                "1. Посмотреть список текущих задач 📋\n"
                "2. Добавить новую задачу ➕\n"
                "3. Отметить задачу как выполненную ✅\n"
                "4. Посмотреть список выполненных задач 🎉\n"
                "5. Удалить задачу 🗑️\n"
                "6. Выйти из программы 🚪\n"
                "Ваш выбор: "))
        except ValueError:
            print("Пожалуйста, вводите только цифры от 1 до 6. ❌")
            continue

        if choice == 1:
            read_task()
            break
        elif choice == 2:
            append_task()
            break
        elif choice == 3:
            mark_completed()
            break
        elif choice == 4:
            show_completed()
            break
        elif choice == 5:
            delete_task()
            break
        elif choice == 6:
            print("Выход из программы. До новых встреч! 👋")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите число от 1 до 6. 🤨")




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
    back_menu()


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
    back_menu()


def delete_task():
    con = sqlite3.connect("ToDoList.db")
    c = con.cursor()
    c.execute("SELECT * from task WHERE status = 'active'")
    task = c.fetchall()
    if not task:
        print("Список задач пуст. Нет задач для удаления. 😕")
        back_menu()
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
    back_menu()


def mark_completed():
    con = sqlite3.connect("ToDoList.db")
    c = con.cursor()
    c.execute("SELECT * from task WHERE status = 'active'")
    task = c.fetchall()
    if not task:
        print("У вас нет активных задач для отметки. 😌")
        back_menu()
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
    back_menu()


def show_completed():
    con = sqlite3.connect("ToDoList.db")
    c = con.cursor()
    c.execute("SELECT * from task WHERE status = 'completed'")
    task_completed = c.fetchall()
    if not task_completed:
        print("Пока нет выполненных задач. Вперед к делам! 🚀")
        back_menu()
    else:
        print("\nСписок выполненных задач 🎊:")
        for index, value in enumerate(task_completed):
            print(f"{index + 1}. {value[1]}. Выполнено в {value[3]}")
    back_menu()

create_table()
menu()