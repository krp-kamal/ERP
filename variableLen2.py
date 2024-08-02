'''
Author: Ms Rya
Version: 3.10
'''
def f1(a1,a2=100,*a3):
    print('A1:{}'.format(a1))
    print('A2:{}'.format(a2))
    print('A3:{}'.format(a3))
f1('ab')
f1('ab','Test1')
f1('ab','Test','File1','File2','File3')
