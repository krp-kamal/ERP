'''
Author: Ms Rya
Version: 3.10
'''

def manage_numbers():
    numbers = [10, 20, 30, 40, 50, 60]

    # Slicing the list
    print("Sliced numbers (index 1 to 4):")
    print(numbers[1:4])  

    print("All numbers:")
    print(numbers[:]) 
  
    # Appending a new number
    numbers.append(70)
    print("After appending 70:")
    print(numbers) 

manage_numbers()
