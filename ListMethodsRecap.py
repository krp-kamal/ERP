'''
Author: Ms Rya
Version: 3.10
'''

def process_numbers(numbers, number_to_count):
    numbers.sort()
    print("Sorted numbers:", numbers)
    
    numbers.reverse()
    print("Reversed numbers:", numbers)
    
    count = numbers.count(number_to_count)
    print(f"Count of {number_to_count}:", count)

numbers_list = [5, 2, 9, 1, 5, 6]
process_numbers(numbers_list, 5)
