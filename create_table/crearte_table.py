import sqlite3,os
def table():
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
        time TEXT,
        time_end INTEGER NULL,
        time_end_str TEXT)""")
        c.execute("""
        CREATE TABLE history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,     
        description TEXT NOT NULL,
        status TEXT NOT NULL,
        time TEXT,
        time_end INTEGER NULL,
        time_end_str TEXT)
        """)
        con.commit()
        con.close()