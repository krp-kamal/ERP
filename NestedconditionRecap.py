'''
Author: Ms Rya
Version: 3.10
'''

def check_age():
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are an adult.")
        if age >= 18:
            print("You are eligible to vote.")
    else:
        print("You are a minor. However, you are not eligible to vote.")


check_age()
