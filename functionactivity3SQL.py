'''
Author: Ms Rya
Version: 3.10
'''
import sqlite3
conn = sqlite3.connect('Files.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Files(
File_name TEXT
File_index TEXT
File_owner TEXT
File_permission TEXT
)
''')

print('Table File has been created')

def upload():
    name = input('Enter a file name: ')
    index = input('Enter a file index: ')
    owner = input('Enter a file owner: ')
    permission = input('Enter {} for file permission: '.format(name))
    download(name, index, owner, permission)
    print('Exit from upload block')

    cursor.execute('''
insert into Files(File_name,File_index,File_owner,File_permission)
VALUES (?,?,?,?)
''',(name,index,owner,permission))

conn.commit()
print('File Information has been updated and saved')

def download(a1, a2, a3, a4):
    print('''
File name: {}

File index: {}

File owner: {}

File permission: {}
'''.format(a1, a2, a3, a4))

upload()
download()
conn.close()
