'''
Author: Ms Rya
Version: 3.10
'''
def nested():
    nested_tuple = (1, ("inner", "tuple"), 3.14, "hello", (True, False))

    print(nested_tuple[1][0])    
    print(nested_tuple[4][0])
    
nested()
