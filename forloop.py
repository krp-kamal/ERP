'''
Author: Ms Rya
Version: 3.10
'''
def count_character(s, target):
    c = 0
    for var in s:
        if var == target:
            c += 1
    return c

s = 'abcadgt6dyahpaaa'

count_a = count_character(s, 'a')
print(count_a)
