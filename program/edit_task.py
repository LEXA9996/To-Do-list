import sqlite3,time, locale 
from . import menu, time_setlocal

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
                task_edit_text = input("Введите, как вы хотите изменить задачу: ")
                now = time.localtime()
                if task_edit_text.strip():
                    c.execute("UPDATE task SET description = ?, time = ? WHERE id = ?",(task_edit_text, time_setlocal.format_time(now), task_id))
                    conn.commit()
                    print(f"Задача обновлена успешно!\nБыло: {task_text}\nСтало:{task_edit_text}")
                    break
                else:
                    print("Задача не может сать пустой")
                    continue
        except ValueError:
            print("Введите только цифры")
            continue
    conn.close()
    menu.back_menu()