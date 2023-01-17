import sqlite3
from task import generate_task_id








def create_database():
    conn = sqlite3.connect("task.sql")
    wis  = conn.cursor()

    wis.execute("CREATE TABLE IF NOT EXISTS task(id integer, task text, task_id text, completed text)")
    conn.commit()


def test_resturn():
    return 1

def generate_row_id():
    return len(sqlite3.connect("task.sql").cursor().execute("SELECT * FROM task").fetchall()) + 1
    
    

def add_a_task(task):
    conn = sqlite3.connect("task.sql")
    wis  = conn.cursor()

    wis.execute("INSERT INTO task VALUES(?,?,?,?)", (generate_row_id(), task, generate_task_id(), "false", ))
    conn.commit()


def get_all_task():
    return sqlite3.connect("task.sql").cursor().execute("SELECT * FROM task").fetchall()
    

def update_task(task_id):
    pass

def delete_task(task_id):
    pass


def clear_all_task():
    pass


