'''
Author: Ms Rya
Version: 3.10
'''

import sqlite3

def create_icr_records():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('ICR_DB.db')
    sth = conn.cursor()

    # Create ICR table if it doesn't exist
    sth.execute('''
    CREATE TABLE IF NOT EXISTS ICRRecord (
        ICR_NO INTEGER PRIMARY KEY,
        Sender_name TEXT,
        Subject TEXT,
        SenderDate TEXT,
        ReceivedBy TEXT
    )
    ''')

    print("ICR table created!")

    # Insert records into the ICR table
    sth.execute('''
    INSERT INTO ICRRecord (ICR_NO, Sender_name, Subject, SenderDate, ReceivedBy)
    VALUES (?, ?, ?, ?, ?)
    ''', (102, 'HSTA', 'Postal', '2nd Aug 2024', 'Ms. Anu'))

    sth.execute('''
    INSERT INTO ICRRecord (ICR_NO, Sender_name, Subject, SenderDate, ReceivedBy)
    VALUES (?, ?, ?, ?, ?)
    ''', (103, 'IBM', 'BBConf', '3rd Aug 2024', 'Mr. Arun'))

    print("ICR records inserted!")

    # Query and display the records
    sth.execute('SELECT * FROM ICRRecord')
    records = sth.fetchall()

    print("\nICR Records:")
    for record in records:
        print(f"ICR_NO: {record[0]}, Sender_name: {record[1]}, Subject: {record[2]}, "
              f"SenderDate: {record[3]}, ReceivedBy: {record[4]}")

    # Commit and close the connection
    conn.commit()
    conn.close()

    print("\nDatabase connection closed!")


# Run the function to create records and insert into SQLite
create_icr_records()
