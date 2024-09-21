'''
Author: Ms Rya
Version: 3.10
'''

def process_input(user_input):
    string_value = str(user_input)
    integer_value = int(user_input)
    float_value = float(user_input)
    input_length = len(user_input)

    print(f"Input number as string: {string_value}")
    print(f"Input number as Integer: {integer_value}")
    print(f"Input number as Float: {float_value}")
    print(f"Length of the Input String: {input_length}")

user_input = input("Enter a number: ")

process_input(user_input)
