'''
Author: Ms Rya
Version: 3.10
'''
def upload():
    name = input('Enter a file name: ')
    index = input('Enter a file index: ')
    owner = input('Enter a file owner: ')
    permission = input('Enter {} for file permission: '.format(name))
    download(name, index, owner, permission)
    print('Exit from upload block')

def download(a1, a2, a3, a4):
    print('''
File name: {}

File index: {}

File owner: {}

File permission: {}
'''.format(a1, a2, a3, a4))

# Calling the upload function to start the process
upload()
