'''
Author: Ms Rya
Version: 3.10
'''
def variable_operations(a, b, c):
    print(f"The type of a is: {type(a)}")   
    print(f"The type of b is: {type(b)}")   
    print(f"The type of c is: {type(c)}")  

    sum_of_ab = a + b
    concatenation = c + " World"

    print("Sum of a and b:", sum_of_ab)        
    print("Concatenated string:", concatenation)

a = 5
b = 10.5
c = 'Hello'
variable_operations(a, b, c)
