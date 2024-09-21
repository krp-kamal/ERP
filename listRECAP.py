'''
Author: Ms Rya
Version: 3.10
'''

def insert_fruit(fruits, fruit_to_insert, index):
    fruits.insert(index, fruit_to_insert)
    return fruits

fruits = ["apple", "banana", "cherry"]
updated_fruits = insert_fruit(fruits, "orange", 1)
print(updated_fruits)
