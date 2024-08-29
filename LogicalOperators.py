'''
Author: Ms Rya
Version: 3.10
'''
a = True
b = False

x = 5
y = 10
z = 20

and_operation = a and b  
or_operation = a or b    
not_operation = not a    

combined_oper = (x < y) and (y < z)  
or_combined = (x > y) or (y < z)          

print("a and b:", and_operation)
print("a or b:", or_operation)
print("not a:", not_operation)
print("(x < y) and (y < z):", combined_oper)
print("(x > y) or (y < z):", or_combined)
