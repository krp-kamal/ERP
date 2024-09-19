'''
Author: Ms Rya
Version: 3.10
'''

def append_text(filename, append_text, search_text):
    with open(filename, 'r') as file:
        content = file.read()

    if search_text in content:
        with open(filename, 'a') as file:
            file.write(append_text)
        print(f"Text '{append_text}' has been appended.")
    else:
        print("The specific text was not found. Nothing was appended.")

filename = '/Users/kamalperumal/Downloads/example.log'
append_text = 'Additional text.'
search_text = 'Line 1'
append_text(filename, append_text, search_text)
