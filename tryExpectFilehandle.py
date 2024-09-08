'''
Author: Ms Rya
Version: 3.10
'''
filename = 'RECAP.py'

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")

