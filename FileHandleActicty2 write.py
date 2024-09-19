'''
Author: Ms Rya
Version: 3.10
'''

def write_file(file_path):
    with open(file_path, "w") as wopj:
        wopj.write('Test server1\n')
        wopj.write('Test server2\n')
        wopj.write('Test server3\n')
        wopj.write('Test server4\n')
        wopj.write('Test server5\n')

file_path = "/Users/kamalperumal/Downloads/r1.log"
write_file(file_path)
