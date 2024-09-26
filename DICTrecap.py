'''
Author: Ms Rya
Version: 3.10
'''
def update_server_info():
    servers = {}

    alias = input("Enter alias name: ")
    IP = input("Enter IP address: ")

    servers[alias] = IP

    print(f"Alias: {alias}, IP: {servers[alias]}")

    servers[alias] = "127.0.0.1"

    print("Updated Server Info:")
    print(f"Alias: {alias}, IP: {servers[alias]}")

update_server_info()
