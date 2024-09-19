'''
Author: Ms Rya
Version: 3.10
'''

def print_user_details(user_info):
    print("User Details:")
    for key, value in user_info.items():
        print(f'{key}: {value}')

user = {'Name': 'Hailey', 'Age': 30, 'City': 'New York'}
print_user_details(user)
