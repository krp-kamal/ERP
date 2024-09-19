'''
Author: Ms Rya
Version: 3.10
'''

def print_file_info(filedetails, filenames, filesize, fileindexnumber):
    print('File details:', filedetails)
    print(type(filedetails))
    
    print('File names:', filenames)
    print(type(filenames))
    
    print('File size:', filesize)
    print(type(filesize))
    
    print('File Index Number:', fileindexnumber)
    print(type(fileindexnumber))

filedetails = 'consists of users data'
filenames = 'Filename.rog'
filesize = 104
fileindexnumber = 23

print_file_info(filedetails, filenames, filesize, fileindexnumber)

