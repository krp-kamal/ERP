'''
Author: Ms Rya
Version: 3.10
'''

def update_student_info(student):
    print(student['name'])
    print(student['age'])
    print(student)

    student['age'] = 21
    student['grade'] = 'A'

    print(student)

student = {'name': 'John Doe', 'age': 20, 'major': 'Computer Science'}
update_student_info(student)
