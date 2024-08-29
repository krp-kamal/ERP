'''
Author: Ms Rya
Version: 3.10
'''
total_sum = 0

while True:
    number = int(input("Enter a positive number or 0 and anynumber below 0 to stop: "))
    if number <= 0:
        break
    total_sum += number

print(f"Total sum of positive numbers is: {total_sum}")
