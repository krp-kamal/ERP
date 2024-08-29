'''
Author: Ms Rya
Version: 3.10
'''
age = int(input("Enter your age: "))
is_member = input("Are you a member? (yes/no): ")

if age > 60 or is_member == "yes":
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")
