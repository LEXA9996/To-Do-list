import sqlite3
from . import menu
def export_task():
    conn = sqlite3.connect("ToDoList.db")
    c = conn.cursor()
    c.execute("SELECT * FROM task WHERE status = 'active'")
    aktive_task = c.fetchall()
    c.execute("SELECT * FROM task WHERE status = 'completed'")
    completed_task = c.fetchall()
    while True:
        name = input("Как вы хотите назвать файл? ").strip()
        if len(name)>100 or len(name)<1:
            conn.commit()
            conn.close()
            print("❗ Введите, пожалуйста, от 1 до 100 символов.")
            continue
        else:
            for char in r'\/:*?"<>|':
                name = name.replace(char, "_")
            filename = name
            if not aktive_task and not completed_task:
                print("📭 У вас нет ни активных, ни выполненных задач.\nПопробуйте добавить хотя бы одну 📝")
                menu.back_menu()
                conn.commit()
                conn.close()
                break
            with open(filename+".txt", "w", encoding="utf-8") as f:
                if aktive_task:
                    f.write("┌────────────────────── 📌 АКТИВНЫЕ ЗАДАЧИ ──────────────────────┐\n\n")
                    for index, i in enumerate(aktive_task):
                        if i[4] is None:
                            f.write(f"{index + 1}) {i[1]}\n   ➤ Добавлено: {i[3]}  ⏳ Срок: бесконечный\n\n")
                        else:
                            f.write(f"{index + 1}) {i[1]}\n   ➤ Добавлено: {i[3]}  ⏳ Срок: {i[5]}\n\n")
                if completed_task:
                    f.write("┌──────────── ✅ ВЫПОЛНЕННЫЕ ЗАДАЧИ ЗА 7 ДНЕЙ ────────────┐\n\n")
                    for index, i in enumerate(completed_task):
                        f.write(f"{index + 1}) {i[1]}\n   ➕ Добавлено: {i[5]}   ✔ Выполнено: {i[3]}\n\n")
        print(f"📄 Файл «{filename}.txt» успешно создан!")
        menu.back_menu()
        break
    conn.close()
def export_history():
    con = sqlite3.connect("ToDoList.db")
    c = con.cursor()
    c.execute("SELECT * FROM history WHERE status = 'overdue'" )
    overdue_task = c.fetchall()
    c.execute("SELECT * FROM history WHERE status = 'completed'")
    completed_task = c.fetchall()
    while True:
        name = input("Как вы хотите назвать файл? ").strip()
        if len(name)>100 or len(name)<1:
            print("❗ Введите, пожалуйста, от 1 до 100 символов.")
            con.commit()
            con.close()
            continue
        else:
            for char in r'\/:*?"<>|':
                name = char.replace(char, "_")
            filename = name
            if not overdue_task and not completed_task:
                print("📭 У вас нет ни просроченных, ни выполненных задач в архиве.")
                con.commit()
                con.close()
                menu.back_menu()
                break
            with open(filename+".txt", "w", encoding="utf-8") as f:
                if overdue_task:
                    f.write("┌──────────── ⚠ ПРОСРОЧЕННЫЕ ЗАДАЧИ ────────────┐\n\n")
                    for index, i in enumerate(overdue_task):
                        f.write(f"{index + 1}) {i[1]}\n   ➕ Добавлено: {i[3]}   ❌ Просрочено: {i[5]}\n\n")
                if completed_task:
                    f.write("┌────── ✅ ВЫПОЛНЕННЫЕ ЗАДАЧИ (АРХИВ) ──────┐\n\n")
                    for index, i in enumerate(completed_task):
                        f.write(f"{index + 1}) {i[1]}\n   ➕ Добавлено: {i[3]}   ✔ Выполнено: {i[3]}\n\n")
        print(f"📄 Файл «{filename}.txt» успешно создан!")
        con.commit()
        con.close()
        menu.back_menu()
        break