'''
Author: Ms Rya
Version: 3.10
'''

def count_words_in_file(file_path):
    count = 0
    with open(file_path, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                count += 1
    print(count)

file_path = input('Enter a filename: ')
count_words_in_file(file_path)
