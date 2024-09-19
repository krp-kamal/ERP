'''
Author: Ms Rya
Version: 3.10
'''

def read_file(file_path, num_chars=None):
    with open(file_path, 'r') as robj:
        if num_chars is not None:
            contents = robj.read(num_chars)
        else:
            contents = robj.read()
    
    print(contents)

file_path = '/Users/kamalperumal/Downloads/r3.log'
read_file(file_path)  
read_file(num_chars=50)  
