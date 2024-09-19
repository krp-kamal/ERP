'''
Author: Ms Rya
Version: 3.10
'''

def type_conversion():
    num = 30
    num_str = str(num)
    print("Integer to String:", num_str)

    num_str = '10'
    num = int(num_str)
    print("String to Integer:", num)

    char_str = 'A'
    char = char_str[0]
    print("String to Character:", char)

    char = 'A'
    char_str = str(char)
    print("Character to String:", char_str)

    num = 1
    bool_val = bool(num)
    print("Integer to Boolean:", bool_val)

    bool_val = True
    num = int(bool_val)
    print("Boolean to Integer:", num)

    bool_val = True
    str_val = str(bool_val)
    print("Boolean to String:", str_val)

    flt = 10.56
    num = int(flt)
    print("Float to Integer:", num)

    num = 10
    flt = float(num)
    print("Integer to Float:", flt)

def main():
    type_conversion()

main()
