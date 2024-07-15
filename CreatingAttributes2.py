'''
Author: Ms Rya
Version: 3.10
'''
class Box:
    var = 100
    def f1(self, a1):
        print('A', self.var)
        self.var = a1 
obj1 = Box()

print('B', obj1.var)

obj1.f1(500)

print('C', obj1.var)



