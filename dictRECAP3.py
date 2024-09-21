'''
Author: Ms Rya
Version: 3.10
'''

def remove_item(inventory, item):
    item_count = inventory.pop(item, 'Item not found')
    print(f"{item.capitalize()} count:", item_count)
    print("Inventory after removing item:", inventory)
  
inventory = {'sword': 1, 'shield': 1, 'potion': 5}
remove_item(inventory, 'potion')
