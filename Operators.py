'''
Author: Ms Rya
Version: 3.10
'''

def validate_inputs():
    partition = input("Enter partition number (1-4): ")
    if partition.isdigit():
        partition = int(partition)
        if 1 <= partition <= 4:
            print("Valid partition number.")
        else:
            print("Invalid partition number.")
    else:
        print("Invalid partition number.")

    disk_name = input("Enter disk name (gcsi or hda): ")
    if disk_name in ['gcsi', 'hda']:
        print("Valid disk name.")
    else:
        print("Invalid disk name.")

    user_name = input("Enter user name (root or admin): ")
    if user_name in ['root', 'admin']:
        print("Valid user name.")
    else:
        print("Invalid user name.")

validate_inputs()
