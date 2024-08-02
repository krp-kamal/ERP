'''
Author: Ms Rya
Version: 3.10
'''
def f1(a1,a2=100,*a3,**a4):
    print(a1)
    print(a2)
    print(a3)
    print(a4)
f1('Ab')
f1('Ab','Test1')
f1('Ab','Test1')
f1('Ab','Test1','Test3','Test4','Test5')
f1('Ab','Test1','Test3','Test4','Test5',user='root',name = 'avin', port = 12)
