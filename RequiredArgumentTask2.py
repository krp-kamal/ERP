'''
Author: Ms Rya
Version: 3.10
'''
#required argument
def f1(a1,a2):# two arguments gives
    print(a1,type(a1))
    print(a2,type(a2))
def append (a3):
    print(a3,type(a3))
    print('this is a3 block')
f1(10,20)# both values are int
f1(100,3.433)# a1 is int and a2 is float
f1('',[])# it print out empty string and list
append(60)
append(70)
print('exit')

