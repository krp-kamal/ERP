'''
Author: Ms Rya
Version: 3.10
'''
words = ['BANANA', 'APPLE', 'CHERRY', 'DATE']

sorted_words = sorted(words, key=str.lower)

lowercase_words = [word.lower() for word in sorted_words]

print(lowercase_words)
