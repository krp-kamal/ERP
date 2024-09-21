'''
Author: Ms Rya
Version: 3.10
'''
def calculate_sum(s1, s2):
    sum_s1_s2 = int(s1) + int(s2)
    return sum_s1_s2

def calculate_percentage(s1):
    percentage = float(s1) * 0.12
    return percentage

def convert_and_check_type(n, m):
    str_n = str(n)
    str_m = str(m)
    return type(str_n), type(str_m)

def convert_to_int_and_float(s):
    int_s = int(s.strip())
    float_s = float(s.strip())
    return int_s, type(int_s), float_s, type(float_s)

s1 = '450'
s2 = '560'
print("Sum of s1 and s2:", calculate_sum(s1, s2))

s1 = '14356.77'
print("12% of s1 value:", calculate_percentage(s1))

n = 100
m = 456.67
type_str_n, type_str_m = convert_and_check_type(n, m)
print("Type of str_n:", type_str_n)
print("Type of str_m:", type_str_m)

s = '456\n'
int_s, type_int_s, float_s, type_float_s = convert_to_int_and_float(s)
print("Converted to int:", int_s)
print("Type of int_s:", type_int_s)
print("Converted to float:", float_s)
print("Type of float_s:", type_float_s)
