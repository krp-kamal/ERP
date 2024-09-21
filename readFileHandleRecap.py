'''
Author: Ms Rya
Version: 3.10
'''
def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
    print(f"Text '{text}' has been written to '{filename}'.")
    
filename = 'example.log'
text_to_write = 'Hello, World!'
write_to_file(filename, text_to_write)
