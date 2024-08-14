'''
Author: Ms Rya
Version: 3.10
'''
def f1(a1):
    def f2():
        a1() 
    return f2

@f1
def app1():
    print("AboutUs Page")
app1()
