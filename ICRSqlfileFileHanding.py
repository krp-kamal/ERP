'''
Author: Ms Rya
Version: 3.10
'''

import sqlite3

def icr_records(file_path):
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

    # Data to be inserted
    ICR = {
        'ICR_NO': [102, 103],
        'Sender_name': ['HSTA', 'IBM'],
        'SenderDate': ['2nd Aug 2024', '3rd Aug 2024'],
        'Subject': ['Postal', 'BBConf'],
        'ReceivedBy': ['Ms.Anu', 'Mr.Arun']
    }
    
    # Inserting records into the database
    sth.execute('''
    INSERT INTO ICRRecord (ICR_NO, Sender_name, Subject, SenderDate, ReceivedBy)
    VALUES (?, ?, ?, ?, ?)
    ''', [(ICR['ICR_NO'][i], ICR['Sender_name'][i], ICR['Subject'][i], ICR['SenderDate'][i], ICR['ReceivedBy'][i]) for i in range(len(ICR['ICR_NO']))])
    
    print('Records have been inserted into the database.')

    # Write records to the log file
    with open(file_path, "a") as wobj:
        for var in ICR:
            wobj.write('{}\t{}\n'.format(var, ICR[var]))

    print('Text has been appended to the file.')

    # Commit and close the database connection
    conn.commit()
    conn.close()
    print('Database connection closed.')

# Specify the file path and call the function
file_path = "/Users/kamalperumal/Downloads/ICR.log"
icr_records(file_path)
