'''
Author: Ms Rya
Version: 3.10
'''

def compare_numbers(x, y):
    greater_than = x > y      
    less_than = x < y         
    equal_to = x == y         
    not_equal_to = x != y     
    greater_or_equal = x >= y 
    less_or_equal = x <= y    

    print("Greater than:", greater_than)
    print("Less than:", less_than)
    print("Equal to:", equal_to)
    print("Not equal to:", not_equal_to)
    print("Greater or equal:", greater_or_equal)
    print("Less or equal:", less_or_equal)


x = 10
y = 20
compare_numbers(x, y)
