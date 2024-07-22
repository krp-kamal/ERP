'''
Author: Ms Rya
Version: 3.10
'''
server_details={} 

K = input("Enter an alias name:")  
V = input("Enter an IP-Address:")  
server_details[K] = V  # Add the alias name (K) and IP address (V) as a key-value pair to the dictionary

print("Alias:{}\t IP-Address:{}".format(K, server_details[K]))  #Print the alias name and its associated IP address

server_details[K] = "12456"  #  Change the IP address associated with the alias name to "127.0.0.1"

print("Updated_dict")  # Indicate that the dictionary has been updated
print("Alias:{}\t IP-Address:{}".format(K, server_details[K]))  # Print the alias name and its new associated IP address
