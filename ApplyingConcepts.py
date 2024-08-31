'''
Author: Ms Rya
Version: 3.10
'''
'''
List Operations with Membership Checks
'''
fruits = ['apple', 'banana', 'cherry', 'orange', 'grape']

'''
Adding and modifying elements
'''
fruits[2] = 'kiwi'
fruits.append('pear')
print("Fruits list:", fruits)

'''
Slicing and copying the list
'''
some_fruits = fruits[1:4]
print("Some fruits:", some_fruits)

'''
Nested list and membership operator
'''
nested_fruits = [['apple', 'banana'], ['cherry', 'kiwi']]
print('kiwi' in nested_fruits[1])  

'''
Sorting and reversing the list
'''
fruits.sort()
fruits.reverse()
print("Sorted and reversed fruits:", fruits)
