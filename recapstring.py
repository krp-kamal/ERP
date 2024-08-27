'''
Author: Ms Rya
Version: 3.10
'''
text = "Hello, Python!"

# String indexing
first_char = text[0]          
last_char = text[-1]          

# String slicing
greeting = text[:5]           
language = text[7:13]        

# String operators
combined = greeting + ", " + language + "!"  

repeated = language * 3      

# String methods
uppercase_text = text.upper()        
replaced_text = text.replace("Python", "World")  

# String formatting
formatted_text = f"{greeting}, {language}! Welcome to {replaced_text.split()[1]}."  # 'Hello, Python! Welcome to World.'

print(first_char)    
print(last_char)     
print(greeting)      
print(language)      
print(combined)      
print(repeated)      
print(uppercase_text)  
print(replaced_text)  
print(formatted_text)
