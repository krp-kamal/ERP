'''
Author: Ms Rya
Version: 3.10
'''

def calculate_sum_of_lengths(str1, str2):
    int1 = int(str1)
    int2 = int(str2)
    sum_of_lengths = len(str1) + len(str2)
    return sum_of_lengths + int1 + int2

str1 = '123'
str2 = '4567'

result = calculate_sum_of_lengths(str1, str2)
print("Sum of the lengths of the original strings:", result)
