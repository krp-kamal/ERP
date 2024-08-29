'''
Author: Ms Rya
Version: 3.10
'''
Sleep = int(input("Enter hours of sleep last night: "))
Score = int(input("Enter your productivity score (1-10): "))

if Sleep >= 8 and Score >= 7:
    print("You are well rested and productive.")
elif Sleep < 8 and Score >= 7:
    print("You are not well rested, but still productive.")
elif Sleep >= 8 and Score < 7:
    print("You are well-rested but not very productive.")
else:
    print("You are neither well rested nor productive.")

