'''
Author: Ms Rya
Version: 3.10
'''
d = {}  # Create an empty dictionary
# Since a1 is not in the dictionary, it will be added with the value 'a2'
d.setdefault('a1', 'a2')
# Use setdefault to ensure 'a1' is in the dictionary with a default value of 'a2'
#'a3' is not in the dictionary and no default value is provided, it will be added with the value None
d.setdefault('a3')
# Use setdefault to ensure 'a3' is in the dictionary with a default value of None beacause there is no value
print(d)  

