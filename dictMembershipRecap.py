'''
Author: Ms Rya
Version: 3.10
'''
List = {'apples': 5,'bananas': 12,'oranges': 7}

# Looping through dictionary items
for fruit, quantity in List.items():
    print(f"We have {quantity} {fruit}.")  


if 'apples' in List:
    print("Apples are in stock.")

if 'grapes' not in List:
    print("Grapes are out of stock.") 
