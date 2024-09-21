'''
Author: Ms Rya
Version: 3.10
'''

def check_inventory(stock):
    for fruit, quantity in stock.items():
        print(f"We have {quantity} {fruit}.")
    
    if 'apples' in stock:
        print("Apples are in stock.")

    if 'grapes' not in stock:
        print("Grapes are out of stock.")

inventory = {'apples': 5, 'bananas': 12, 'oranges': 7}
check_inventory(inventory)
