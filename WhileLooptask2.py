'''
Author: Ms Rya
Version: 3.10
'''

def login():
    while True:
        name = input('Enter the login name: ')
        if name == 'apple':
            print('You have logged in!')
            break
        else:
            print('Failed! Try again.')

def main():
    login()

main()
