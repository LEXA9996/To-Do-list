import sqlite3, time
def check_overdue_time():
    while True:
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute("SELECT id, description, status, time, time_end, time_end_str FROM task")
        tasks = c.fetchall()
        now = int(time.time())
        for task in tasks:
            tasks_id, des, status, t_start, t_end, time_end_str = task
            if t_end is not None and now>int(t_end):
                c.execute("""
                    INSERT INTO history (description, status, time, time_end, time_end_str)
                    VALUES (?, ?, ?, ?, ?)
                """, (des, "overdue", t_start,  t_end, time_end_str))
                c.execute("DELETE FROM task WHERE id = ?", (tasks_id,))
        con.commit()
        con.close()
        time.sleep(10)

def check_completed_time():
    while True:
        con = sqlite3.connect("ToDoList.db")
        c = con.cursor()
        c.execute("SELECT * FROM task WHERE status = ?", ("completed", ))
        tasks = c.fetchall()
        now = int(time.time())
        for task in tasks:
            tasks_id, des, status, t_start, t_end, time_end_str = task
            if now - t_end >= 7 * 86400:
                c.execute("""
                    INSERT INTO history (description, status, time, time_end, time_end_str)
                    VALUES (?, ?, ?, ?, ?)
                """, (des, "completed", t_start,  t_end, time_end_str))
                c.execute("DELETE FROM task WHERE id = ?", (tasks_id, ))
        con.commit()
        con.close()
        time.sleep(10)