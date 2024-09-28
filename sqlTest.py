'''
Author: Ms Rya
Version: 3.10
'''
import sqlite3
conn = sqlite3.connect('sqlTest.dp')
cur = conn.cursor()

#insert data using the variables
emp_ID = 4
emp_Name = 'Tom'
emp_cost = 3456

cur.execute("insert into employee(empID,empName,empCost)values (?,?,?)",(emp_ID,emp_Name,emp_cost))

conn.commit()

cur.execute("select *from sqlTest where empID = ?", (emp_ID))

row = cur.fetchone()
print(row)
fetchone()

conn.close()
