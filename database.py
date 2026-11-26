import sqlite3

def connect_db():
    conn = sqlite3.connect("students.db")
    return conn
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            class TEXT,
            marks REAL,
            gender TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_student_db(student):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (roll, name, age, class, marks, gender, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        student["roll"],
        student["name"],
        student["age"],
        student["class"],
        student["marks"],
        student["gender"],
        student["created_at"]
    ))

    conn.commit()
    conn.close()

def view_students_db():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students