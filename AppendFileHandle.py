'''
Author: Ms Rya
Version: 3.10
'''
def copy_file(read_file, write_file):
    with open(read_file, 'r') as robj:
        with open(write_file, 'w') as wobj:
            s = robj.read()
            wobj.write(s)
            wobj.write('genny\n')
            wobj.write('April\n')
read_file = "/Users/kamalperumal/Downloads/FileHandleRead.py"
write_file = "/Users/kamalperumal/Downloads/Read3.log"
copy_file(read_file, write_file)

