'''
Author: Ms Rya
Version: 3.10
'''

def modify_fruits(fruits):
    fruits.pop()         # Remove the last item
    print(fruits)
    fruits.pop(2)        # Remove the item at index 2
    print(fruits)

# List of fruits
fruits = [100, 200, 300, 400]

# Call the function
modify_fruits(fruits)
