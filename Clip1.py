'''
Author: Ms Rya
Version: 3.10
'''

def file(file_path):
    with open(file_path, 'r') as FH:
        
        print(FH.readlines(3))  
        print(FH.readlines(4))
        
        for var in FH.readlines():
            print(var.strip())

file_path = '/Users/kamalperumal/Downloads/FileHandleRead.py'
file(file_path)

