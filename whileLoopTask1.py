'''
Author: Ms Rya
Version: 3.10
'''
def Login1():
    i = 0
    while (i<3):
        name = input('Enter the login name')
        if(name=='root'):
            print('success')
            break
        else:
            print('failed')
            i = i+1
Login1()    
