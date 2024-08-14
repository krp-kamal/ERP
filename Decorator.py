'''
Author: Ms Rya
Version: 3.10
'''
def f1(a):
    def f2():
          a()
    return f2

@f1
def app1():
   print("App1 demo")
app1()     
@f1
def app2():
   print("App2 demo") 
app2()   
@f1
def app3():
   print("App3 demo")    
app3()
