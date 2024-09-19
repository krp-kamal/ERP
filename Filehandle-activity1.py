'''
Author: Ms Rya
Version: 3.10
'''

def file_contents(source_file_path, destination_file_path):
    with open(source_file_path, 'r') as robj:
        contents = robj.read()
    
    with open(destination_file_path, 'w') as wobj:
        wobj.write(contents)

source_file_path = "/Users/kamalperumal/Downloads/r1.log"
destination_file_path = "/Users/kamalperumal/Downloads/r2.log"
file_contents(source_file_path, destination_file_path)
