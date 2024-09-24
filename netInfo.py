'''
Author: Ms Rya
Version: 3.10
'''
def netInfo():# Initialize an empty dictionary to store the key-value pairs from the file
    Lines = {}
    with open('/Users/kamalperumal/Downloads/ifcfg.conf', 'r') as file:# Open the 'ifcfg.conf' file in read mode
        Files = file.readlines()# Read all lines from the file into the list 'Files'
        for File in Files:# Loop through each line in 'Files'
            if '=' in File:# Check if the line contains an '=' to ensure it's a key-value pair
                File = File.strip()# Remove leading whitespace from the line
                k,v = File.split('=') # Split the line into a key and value at the '=' symbol
                Lines[k]= v # Store the key-value pair in the 'Lines' dictionary
    # Update the values in the dictionary for the specific keys
    Lines['onboot '] = 'yes'
    Lines['bootproto'] = 'static'
    Lines['defroute'] = 'no'
    Lines['IPAddress'] = '192.168.123.132'

    

    with open('/Users/kamalperumal/Downloads/net_ifcfg.conf', 'w') as wobj:
        # Open a new file 'net_ifcfg.conf' in write mode to save the updated file
        for var in Lines:
            wobj.write(var+'='+Lines[var]+'\n')# Write in 'key=value' format with newline
                    
netInfo()

        
