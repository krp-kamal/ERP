'''
Author: Ms Rya
Version: 3.10
'''
def f1(**kwargs):
    for v in kwargs:
        print('{}\t{}'.format(v,kwargs[v]))
f1(name = 'root', user = 'apple', db = 'mysql')  
