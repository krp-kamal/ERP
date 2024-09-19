'''
Author: Ms Rya
Version: 3.10
'''

def user_info():
    Name = input('Enter your name: ')
    Age = int(input('Enter your age: '))
    Height = int(input('How tall are you (cm): '))
    File_Name = input('Enter the file name you need to save: ')

    with open(File_Name, 'w') as file:
        file.write('File Name: ' + File_Name + '\n')
        file.write('Details about the user:\n')
        file.write('Name: ' + Name + '\n')
        file.write('Age: ' + str(Age) + '\n')
        file.write('Height: ' + str(Height) + ' cm\n')

    with open(File_Name, 'r') as file:
        content = file.read()
        print(content)

user_info()
