'''
Author: Ms Rya
Version: 3.10
'''
def f1(x, y):
    return x + y

def f2(func, x, y):
    return func(x, y)

result = f2(f1,1,5)
print(result)
