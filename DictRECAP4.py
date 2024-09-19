'''
Author: Ms Rya
Version: 3.10
'''

def f1_membership_code(membership_codes, code_to_check):
    if code_to_check in membership_codes:
        print(f'Code {code_to_check} belongs to {membership_codes[code_to_check]}')
    else:
        print(f'Code {code_to_check} not found.')

membership_codes = {
    'AB123': 'Alice',
    'CD456': 'Bob',
    'EF789': 'Charlie'
}

code_to_check = 'CD456'
f1_membership_code(membership_codes, code_to_check)

