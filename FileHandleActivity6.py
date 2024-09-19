'''
Author: Ms Rya
Version: 3.10
'''

def print_file_lines(file_path):
    with open(file_path, 'r') as robj:
        for line in robj:
            print(line)

file_path = '/Users/kamalperumal/Downloads/r3.log'
print_file_lines(file_path)
