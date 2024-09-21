'''
Author: Ms Rya
Version: 3.10
'''

def display_membership(codes):
    for code, name in codes.items():
        print(f'Code {code} belongs to {name}')

membership_codes = {
    'AB123': 'Alice',
    'CD456': 'Bob',
    'EF789': 'Charlie'
}
display_memberships(membership_codes)
