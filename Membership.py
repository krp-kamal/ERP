'''
Author: Ms Rya
Version: 3.10
'''
def membership():
    membership_codes = {
        'M001': 'Alice',
        'M002': 'Bob',
        'M003': 'Charlie'
    }

    code = input("Enter membership code: ")

    if code in membership_codes:
        print(f'Code {code} belongs to {membership_codes[code]}')
    else:
        print(f'Code {code} not found.')

membership()
