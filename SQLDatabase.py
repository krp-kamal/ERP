'''
Author: Ms Rya
Version: 3.10
'''

import sqlite3

conn = sqlite3.connect('DB_example.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER,
        name TEXT,
        city TEXT
    )
''')

cur.execute("INSERT INTO people (name, city) VALUES ('Delwin', 'Chennai')")

conn.commit()

cur.execute("SELECT * FROM people")
for record in cur.fetchall():
    print(record)

conn.close()
