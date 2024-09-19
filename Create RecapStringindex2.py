'''
Author: Ms Rya
Version: 3.10
'''

def manipulate_string(text):
    first_char = text[0]
    last_char = text[-1]
    greeting = text[:5]
    language = text[7:13]

    combined = greeting + ", " + language + " is great!"
    uppercase_text = text.upper()
    replaced_text = text.replace("Python", "Programming")

    # Print results
    print(first_char)
    print(last_char)
    print(greeting)
    print(language)
    print(combined)
    print(uppercase_text)
    print(replaced_text)

text = "Hello, Python! Learning Python is fun."
manipulate_string(text)
