'''
Author: Ms Rya
Version: 3.10
'''

def write_default_names_to_file(file_path):
    names = ['neil', 'Tom', 'zack', 'shan']
    with open(file_path, 'w') as wobj:
        for name in names:
            wobj.write(name + '\n')

file_path = '/Users/kamalperumal/Downloads/Writefile.log'
write_default_names_to_file(file_path)
