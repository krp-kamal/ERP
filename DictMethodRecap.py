'''
Author: Ms Rya
Version: 3.10
'''

def person_info(person):
    removed_age = person.pop('age')
    print(f"Removed Age: {removed_age}\nUpdated Person: {person}")

    person.update(location='New York', age=31)
    print("New Info:", person)

person = {'name': 'Jane Doe', 'age': 30, 'job': 'Engineer'}
person_info(person)
