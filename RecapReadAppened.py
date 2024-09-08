'''
Author: Ms Rya
Version: 3.10
'''
filename = 'example.log'
Append_Text = 'Additional text.'

with open(filename, 'r') as file:
    content = file.read()

if 'Line 1' in content:
    with open(filename, 'a') as file:
        file.write(Append_Text)
    print(f"Text '{Append_Text}' has been appended.")
else:
    print("The specific text was not found. Nothing was appended.")
