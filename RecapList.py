'''
Author: Ms Rya
Version: 3.10
'''

def manage_fruits():
    fruits = ['apple', 'banana', 'cherry']

    print("Initial fruits:")
    print(fruits[0])  
    print(fruits[1]) 

    # Modifying
    fruits[2] = 'orange'
    print("After modifying the third fruit:")
    print(fruits)

    # Appending
    fruits.append('grape')
    print("After appending a new fruit:")
    print(fruits)

manage_fruits()
