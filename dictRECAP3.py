'''
Author: Ms Rya
Version: 3.10
'''
inventory = {'sword': 1, 'shield': 1, 'potion': 5}

potion_count = inventory.pop('potion', 'Item not found')
print("Potion count:", potion_count)  

print("Inventory after removing potion:", inventory)
