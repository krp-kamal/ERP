'''
Author: Ms Rya
Version: 3.10
'''

def file_content(source_file, destination_file):
    with open(source_file, 'r') as src:
        content = src.read()

    with open(destination_file, 'w') as dest:
        dest.write(content)

    print(f"Content from '{source_file}' has been copied to '{destination_file}'.")

source_file = '/Users/kamalperumal/Downloads/example.log'
destination_file = '/Users/kamalperumal/Downloads/DFile.log'
file_content(source_file, destination_file)
