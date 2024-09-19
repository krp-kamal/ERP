'''
Author: Ms Rya
Version: 3.10
'''

def write_names(file_path, names):
    with open(file_path, 'w') as wobj:
        for name in names:
            wobj.write(name + '\n')

# Example usage:
file_path = '/Users/kamalperumal/Downloads/r3.log'
names = ['Jenny', 'Bob', 'Tom', 'Matty', 'Alice', 'John', 'Sara']
write_names(file_path, names)

