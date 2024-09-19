'''
Author: Ms Rya
Version: 3.10
'''

def last_line(file_path):
    with open(file_path, 'r') as FH:
        lines = FH.readlines()
        if len(lines) >= 2:
            second_last_line = lines[-2]
            for var in second_last_line:
                print(var.strip())
        else:
            print("The file does not have enough lines.")

file_path = '/Users/kamalperumal/Downloads/FileHandleRead.py'
last_line(file_path)
