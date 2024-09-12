'''
Author: Ms Rya
Version: 3.10
'''
def listOperations():
    fruits = ['apple', 'banana', 'cherry', 'orange', 'grape']
    fruits[2] = 'kiwi'
    fruits.append('pear')
    print("Fruits list:", fruits)

    some_fruits = fruits[1:4]
    print("Some fruits:", some_fruits)

    nested_fruits = [['apple', 'banana'], ['cherry', 'kiwi']]
    print('kiwi' in nested_fruits[1])  

    fruits.sort()
    fruits.reverse()
    print("Sorted and reversed fruits:", fruits)

listOperations()
