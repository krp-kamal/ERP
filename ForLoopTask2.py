'''
Author: Ms Rya
Version: 3.10
'''

def filter_characters(input_string):
    for var in input_string:
        if var in '46789':
            continue
        else:
            print(var)

s = 'a4d6f7g8h9'
filter_characters(s)

