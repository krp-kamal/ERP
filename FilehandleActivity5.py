'''
Author: Ms Rya
Version: 3.10
'''

def n_chars(file_path, num_chars=4):
    with open(file_path, 'r') as robj:
        contents = robj.read(num_chars)
    print(contents)

file_path = '/Users/kamalperumal/Downloads/r3.log'
n_chars(file_path)

