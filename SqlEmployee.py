'''
Author: Ms Rya
Version: 3.10
'''
import sqlite3

#create connection to a database
conn = sqlite3.connect('employee.db')

# cursor object has been created
cur = conn.cursor()

# create a new table
cur.execute('''
    CREATE TABLE IF NOT EXITS employee (
    empID integer,
    empName text,
    empCost integer
    )''')

#insert records into the new table
cur.execute("insert into employee(empID, empName, empCost)values(001,'aali',2345)")
cur.execute("insert into employee(empID, empName, empCost)values(002,'aali',2444)")
cur.execute("insert into employee(empID, empName, empCost)values(003,'aali',2555)")
# fetch all the records
cur.execute("select *from employee")
rows = cur.fetchall()
# display the records
for row in rows:
    print(row)

conn.close()    
