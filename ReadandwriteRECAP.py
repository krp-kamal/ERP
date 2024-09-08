'''
Author: Ms Rya
Version: 3.10
'''
source_file = '/Users/kamalperumal/Downloads/example.log'
destination_file = '/Users/kamalperumal/Downloads/DFile.log'

with open(source_file, 'r') as src:
    content = src.read()
'''
Read Entire existing File
'''
with open(destination_file, 'w') as dest:
    dest.write(content)
'''
Write it in a new File
'''
print(f"Content from '{source_file}' has been copied to '{destination_file}'.")

