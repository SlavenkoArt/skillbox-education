import sqlite3

with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE students("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "name TEXT NOT NULL,"
                   "surname TEXT NOT NULL"
                   ");")

    cursor.execute("INSERT INTO STUDENTS (name, surname) VALUES ('Петр', 'Петров');")
    cursor.execute('.headers on')
    cursor.execute('.mode box')
    cursor.execute("SELECT * FROM students;")
    print(cursor.fetchall())
