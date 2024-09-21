'''
Author: Ms Rya
Version: 3.10
'''
def fruit_quantities(fruits):
    for fruit, quantity in fruits.items():
        print(f"Fruit: {fruit}, Quantity: {quantity}")

fruits = {'apple': 5, 'banana': 3, 'cherry': 7}
fruit_quantities(fruits)
