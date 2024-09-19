'''
Author: Ms Rya
Version: 3.10
'''

def update_server_details():
    server_details = {}
    K = input("Enter an alias name:")  
    V = input("Enter an IP-Address:")  
    server_details[K] = V

    print("Alias:{}\t IP-Address:{}".format(K, server_details[K]))

    server_details[K] = "12456"

    print("Updated_dict")
    print("Alias:{}\t IP-Address:{}".format(K, server_details[K]))

update_server_details()
