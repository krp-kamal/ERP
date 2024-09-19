'''
Author: Ms Rya
Version: 3.10
'''

def append_text_to_file(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text + '\n')
            print(f"Successfully appended '{text}' to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = 'Writefile.log'
text_to_append = 'jack'
append_text_to_file(filename, text_to_append)
