'''
Author: Ms Rya
Version: 3.10
'''
server_details = {}
# Adding individual key-value pairs
server_details["Unix-Server"] = '10.20.30.40'
server_details["Linux-Server"] = '10.20.55.45'
server_details["Winx-Server"] = '10.45.65.45'
server_details["Aix-Server"] = '10.42.98.78'

for key in server_details:
    value = server_details[key]
    print("Alias:", key, "\n IP-Address:", value)
