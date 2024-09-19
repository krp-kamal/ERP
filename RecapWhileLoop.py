'''
Author: Ms Rya
Version: 3.10
'''

def sum_numbers():
    total_sum = 0

    while True:
        number = int(input("Enter a positive number (or 0/negative to stop): "))
        if number <= 0:
            break
        total_sum += number

    print(f"Total sum of positive numbers is: {total_sum}")

sum_numbers()
