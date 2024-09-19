'''
Author: Ms Rya
Version: 3.10
'''

def calculate_average():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    total = num1 + num2 + num3
    average = total / 3

    print(f"The sum of the numbers is: {total}")
    print(f"The average of the three numbers is: {average}")

def main():
    calculate_average()

main()
