'''
Author: Ms Rya
Version: 3.10
'''
def check_colour(colour_list, colour_to_check):
    exists = colour_to_check in colour_list
    not_exists = colour_to_check not in colour_list
    return exists, not_exists

colour = ['red', 'green', 'blue']
red_check = check_colour(colour, 'red')
yellow_check = check_colour(colour, 'yellow')

print(red_check[0])     
print(yellow_check[0])    
print(yellow_check[1])    
