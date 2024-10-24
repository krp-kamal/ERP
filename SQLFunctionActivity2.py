'''
Author: Ms Rya
Version: 3.10
'''

import sqlite3
import time

conn = sqlite3.connect('Time_management.db')
sth = conn.cursor()

sth.execute('''
CREATE TABLE IF NOT EXISTS time_logos(
id INTEGER PRIMARY KEY,
duration TEXT
)
''')

print('Time management table has been created!')

def f1():
    print('this is f1 block')
    time.sleep(3)#the exit statement delays after 3 seconds
    print('exit from f1 block')
    
print('this is main section-1')# prints this statemnet
f1()#calls the function
time.sleep(2)#the 'main'and 'exit main section'delays after 2 seconds
print('this is main section')
print('exit from main section')

conn.close()
