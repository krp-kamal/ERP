'''
Author: Ms Rya
Version: 3.10
'''
filename = 'example2.log'
lines_to_write = ['Line 1\n', 'Line 2\n', 'Line 3\n']

with open(filename, 'w') as file:
    file.writelines(lines_to_write)

print(f"Lines have been written to '{filename}'.")
