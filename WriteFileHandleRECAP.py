'''
Author: Ms Rya
Version: 3.10
'''

def writelines_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)
    print(f"Lines have been written to '{filename}'.")

filename = '/Users/kamalperumal/Downloads/example2.log'
lines_to_write = ['Line 1\n', 'Line 2\n', 'Line 3\n']
writelines_file(filename, lines_to_write)
