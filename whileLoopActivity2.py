'''
Author: Ms Rya
Version: 3.10
'''
def Loops():
    while True:
        answers = input('Enter yes or no: ')
        if answers.lower() == 'yes':
            print('You Said yes!')
            break
        elif answers.lower() == 'no':
            print('You said no!')
            break
        else:
            print('Please enter either yes or no.')
        
Loops()
