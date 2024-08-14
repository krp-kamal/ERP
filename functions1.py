'''
Author: Ms Rya
Version: 3.10
'''
def f1(name):
    def f2():
        return "Hello, " + name + "!"
    return f2

result = f1("ABC")
print(result())
