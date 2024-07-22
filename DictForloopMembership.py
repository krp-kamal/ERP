'''
Author: Ms Rya
Version: 3.10
'''
empty_dict = {}  
b = input('enter an alias name:') 
c = input('enter an IP address:') 
empty_dict[b] = c  # Add the alias name as the key and the IP address as the value to empty_dict
print(empty_dict[b])  # Print the IP address stored under the alias name in empty_dict
empty_dict[b] = '2345'  # Change the value of the alias name in empty_dict to '2345'
print('updated_dict')  # Print the text 'updated_dict' to show that the dictionary has been updated
print(empty_dict[b])  # Print the new value ('2345') stored under the alias name in empty_dict

