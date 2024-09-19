'''
Author: Ms Rya
Version: 3.10
'''

def port_number():
    database_name = input("Enter database name: ")

    if database_name.lower() == 'oracle': 
        port_number = 1234
    else:
        port_number = 5546
    
    return port_number

port = port_number()
print(f"The port number is: {port}")

