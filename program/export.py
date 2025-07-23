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
            print("❗ Введите, пожалуйста, от 1 до 100 символов.")
            continue
        else:
            for char in r'\/:*?"<>|':
                name = name.replace(char, "_")
            filename = name
            if not aktive_task and not completed_task:
                print("📭 У вас нет ни активных, ни выполненных задач.\nПопробуйте добавить хотя бы одну 📝")
                menu.back_menu()
                break
            with open(filename+".txt", "w", encoding="utf-8") as f:
                if aktive_task:
                    f.write("📌 Активные задачи:\n\n")
                    for index, i in enumerate(aktive_task):
                        f.write(f"{index + 1}) {i[1]}\n   ➤ Добавлено: {i[3]}\n\n")
                if completed_task:
                    f.write("✅ Выполненные задачи:\n\n")
                    for index, i in enumerate(completed_task):
                        f.write(f"{index + 1}) {i[1]}\n   ✔ Выполнено: {i[3]}\n\n")
        print(f"📄 Файл «{filename}.txt» успешно создан!")
        menu.back_menu()
        break
    conn.close()