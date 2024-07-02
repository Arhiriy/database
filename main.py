import sqlite3

conn = sqlite3.connect('student.dp')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade REAL
)
''')

cursor.execute('''
INSERT INTO student (name, weight)
VALUES ('Petya', 69), ('Emma', 54), ('Jack', 63)
''')


conn.commit()

cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()