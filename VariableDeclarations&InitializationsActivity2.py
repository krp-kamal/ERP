'''
Author: Ms Rya
Version: 3.10
'''

def display_variable_info():
    v1 = 10
    v2 = 2.0
    v3 = 1.2 + 3.4j
    v4 = True  # corrected from 'true' to 'True'
    v5 = ''

    print("v1 value:", v1, ", The type is:", type(v1))  
    print("v2 value:", v2, ", The type is:", type(v2))  
    print("v3 value:", v3, ", The type is:", type(v3))  
    print("v4 value:", v4, ", The type is:", type(v4))  
    print("v5 value:", v5, ", The type is:", type(v5))  

def main():
    display_variable_info()

main()
