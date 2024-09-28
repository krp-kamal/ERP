'''
Author: Ms Rya
Version: 3.10
'''
import sqlite3
conn = sqlite3.connect('SQLcost.dp')
cur = conn.cursor()

#insert data using the variables
emp_ID = 4
emp_telephone = 123456789
emp_Cost= 8978

cur.execute("insert into file2(empID,empName,empCost)values (?,?,?)",(emp_ID,emp_telephone,emp_Cost))

conn.commit()

fetchall()
cur.execute("select *from SQLcost where empID = ?", (emp_ID))
cur.execute("select *from SQLcost where empName = ?", (emp_telephone))
cur.execute("select *from SQLcost where empCost = ?", (emp_Cost))

row = cur.fetchall()
print(row)

conn.close()
