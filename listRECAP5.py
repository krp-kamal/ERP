'''
Author: Ms Rya
Version: 3.10
'''
def sort_and_lowercase(words):
    sorted_words = sorted(words, key=str.lower)
    lowercase_words = [word.lower() for word in sorted_words]
    return lowercase_words
  
words = ['BANANA', 'APPLE', 'CHERRY', 'DATE']
result = sort_and_lowercase(words)
print(result)
