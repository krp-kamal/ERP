'''
Author: Ms Rya
Version: 3.10
'''

def last_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    if len(lines) >= 2:
        second_last_line = lines[-2].strip()
        print(second_last_line)
    else:
        print("The file does not have enough lines.")


filename = '/Users/kamalperumal/Downloads/FileHandleRead.py'
last_line(filename)
