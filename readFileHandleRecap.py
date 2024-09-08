'''
Author: Ms Rya
Version: 3.10
'''
filename = 'example.log'
text_to_write = 'Hello, World!'

with open(filename, 'w') as file:
    file.write(text_to_write)

print(f"Text '{text_to_write}' has been written to '{filename}'.")
