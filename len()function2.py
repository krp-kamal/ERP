'''
Author: Ms Rya
Version: 3.10
'''

def calculate_sums(str1, str2):
    int1 = int(str1)
    int2 = int(str2)

    sum_of_values = int1 + int2
    sum_of_lengths = len(str1) + len(str2)
    return sum_of_values, sum_of_lengths

str1 = '123'
str2 = '4567'

sum_of_values, sum_of_lengths = calculate_sums(str1, str2)

print(f"The sum of the integer values of '{str1}' and '{str2}' is: {sum_of_values}")
print(f"The sum of the lengths of '{str1}' and '{str2}' is: {sum_of_lengths}")
