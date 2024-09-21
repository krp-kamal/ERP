'''
Author: Ms Rya
Version: 3.10
'''

def string_operations(text):
    first_char = text[0]          
    last_char = text[-1]          

    greeting = text[:5]           
    language = text[7:13]        

    combined = greeting + ", " + language + "!"  
    repeated = language * 3      

    uppercase_text = text.upper()        
    replaced_text = text.replace("Python", "World")  

    formatted_text = f"{greeting}, {language}! Welcome to {replaced_text.split()[1]}."  

    print(first_char)    
    print(last_char)     
    print(greeting)      
    print(language)      
    print(combined)      
    print(repeated)      
    print(uppercase_text)  
    print(replaced_text)  
    print(formatted_text)

text = "Hello, Python!"
string_operations(text)
