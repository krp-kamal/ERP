'''
Author: Ms Rya
Version: 3.10
'''

def print_dictionary(D):
    for var in D:
        print('{}\t{}'.format(var, D[var]))

D = {1: 'value1', 2: 'value2', 3: 'value3'}

print_dictionary(D)
