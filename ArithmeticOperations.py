'''
Author: Ms Rya
Version: 3.10
'''
# Take input from the user
num_str = input("Enter a number: ")

num_int = int(num_str)
num_float = float(num_str)


sum_result = num_int + 10
product_result = num_float * 2.5
input_length = len(num_str)

# Display results
print("Results of arithmetic operations:")
print(f"Integer + 10: {sum_result}")
print(f"Float * 2.5: {product_result}")
print(f"Length of the input string: {input_length}")

