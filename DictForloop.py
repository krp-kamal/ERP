'''
Author: Ms Rya
Version: 3.10
'''

def print_server_details(server_details):
    for key, value in server_details.items():
        print("Alias:", key, "\nIP-Address:", value)

server_details = {
    "Unix-Server": '10.20.30.40',
    "Linux-Server": '10.20.55.45',
    "Winx-Server": '10.45.65.45',
    "Aix-Server": '10.42.98.78'
}

print_server_details(server_details)
