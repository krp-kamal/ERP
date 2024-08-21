'''
Author: Ms Rya
'''
import sqlite3

conn = sqlite3.connect('DB_example.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        city TEXT
    )
''')

cur.execute("INSERT INTO people (name, city) VALUES ('Delwin', 'Chennai')")

conn.commit()

cur.execute("SELECT * FROM people")

records = cur.fetchall()

# Iterate through all fetched records
for record in records:
    person_id, person_name, person_city = record
    print(f"Person ID: {person_id}")
    print(f"Person Name: {person_name}")
    print(f"Person City: {person_city}")

print("Data entered successfully.")

conn.close()
