'''
Author: Ms Rya
Version: 3.10
'''

def collect_data():
    display_size = {}
    i = 0
    while i < 5:
        name = input('Enter your name: ')
        address = input('Enter your IP address: ')
        display_size[name] = address
        i += 1
    return display_size

def print_data(display_size):
    for var in display_size:
        print('{}\t{}'.format(var, display_size[var]))
    print('Size of dict: {}'.format(len(display_size)))

data = collect_data()
print_data(data)
