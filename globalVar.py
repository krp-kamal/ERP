'''
Author: Ms Rya
Version: 3.10
'''
global_var = 100

def Var_global():
    local_var = 200.5
    result = global_var + local_var + 10.9
    
    print(result)

Var_global()

print(Var_global)
