'''
Author: Ms Rya
Version: 3.10
'''

def strip_strings():
    s1 = 'python'
    s2 = 'programming:'
    s3 = '\tdata\t'
    s4 = '\nsamplecode\n'
    
    stripped_s1 = s1.strip()
    stripped_s2 = s2.strip(':')
    stripped_s3 = s3.strip()
    stripped_s4 = s4.strip()
    
    return stripped_s1, stripped_s2, stripped_s3, stripped_s4

def main():
    stripped_results = strip_strings()
    for result in stripped_results:
        print(result)

main()
