'''
Author: Ms Rya
Version: 3.10
'''
membership_codes = {
    'AB123': 'Alice',
    'CD456': 'Bob',
    'EF789': 'Charlie'
}

code_to_check = 'CD456'

if code_to_check in membership_codes:
    print(f'Code {code_to_check} belongs to {membership_codes[code_to_check]}')
else:
    print(f'Code {code_to_check} not found.')
