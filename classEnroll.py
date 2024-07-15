'''
Author: Ms Rya
Version: 3.10
'''
class enrollment:
    Emp_name = ''
    Emp_id = ''
    Emp_dept = ''
    def enrol(self, emp_name, emp_id, emp_dept):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_dept = emp_dept
        print('Initialization is done!')

    def display(self):
        print(f'emp_name: {self.emp_name}')
        print(f'emp_id: {self.emp_id}')
        print(f'emp_dept: {self.emp_dept}')

    def update(self, emp_dept):
        self.emp_dept = emp_dept
        print('Department is updated')
        

obj1 = enrollment()
obj1.enrol('kamal',101,'sales')
obj1.display()
obj1.update('admin')
print('\n')
obj1.display()

obj2 = enrollment()
obj2.enrol('Karthick', 102, 'prod')
obj2.display()
obj2.update('admin')
print('\n')
obj2.display()

obj3 = enrollment()
obj3.enrol('rya',103,'DBA')
obj3.display()
obj3.update('admin')
print('\n')
obj3.display()

obj4 = enrollment()
obj4.enrol('Anu',104,'Cloud')
obj4.display()
obj4.update('admin')
print('\n')
obj4.display()
