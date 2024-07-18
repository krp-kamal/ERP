'''
Author: Ms Rya
Version: 3.10
'''
# default argument
def f1(user=100,port=200):
    print(user,port)
    print(type(user),type(port))
print('Start block')
f1()# gives 100 200
f1('AB')#single argument(AB 200)
f1('AB','CD') # AB CD
print('Exit')

