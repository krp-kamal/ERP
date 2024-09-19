'''
Author: Ms Rya
Version: 3.10
'''

def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text + '\n')

filename = '/Users/kamalperumal/Downloads/Writefile'
text_to_append = 'jack'
append_to_file(filename, text_to_append)
