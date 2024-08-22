'''
Author: Ms Rya
Version: 3.10
'''
import sqlite3 
conobj = sqlite3.connect('test1.db')
sth = conobj.cursor()
'''
sth.execute(' create table T3 (pid int, pname text)')
'''
sth.execute("insert into T3(pid, pname) values(101,'productA')")
sth.execute("insert into T3(pid, pname) values(102,'productB')")
sth.execute("insert into T3(pid, pname) values(103,'productC')")
sth.execute('select * from T3')
r = sth.fetchall()
print(r)

sth.execute("insert into T3(pid, pname) values(?,?)",(104,'productD'))
sth.execute('select * from T3')
r = sth.fetchall()
print(r)
Va = 105
Vb = 'productE'
sth.execute("insert into T3(pid, pname) values(?,?)",(Va, Vb))
sth.execute('select * from T3')
r = sth.fetchall()
print(r)
