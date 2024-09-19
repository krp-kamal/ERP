'''
Author: Ms Rya
Version: 3.10
'''

def count_spaces(input_string):
    space_count = input_string.count(' ')
    return space_count

def main():
    s = ' a b c d ef g'
    print("Original string:", repr(s))
    
    space_count = count_spaces(s)
    print("Number of spaces in the string:", space_count)

main()
