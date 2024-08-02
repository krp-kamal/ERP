'''
Author: Ms Rya
Version: 3.10
'''
def f1(*a):
    print(type(a))
    print('{} \t{}'.format(a, len(a)))
          
f1()
f1(10, 2.3, 'data')
f1(10, 2.3, 'data', ['D1', 'D2', 'D3'])

