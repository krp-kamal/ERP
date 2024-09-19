'''
Author: Ms Rya
Version: 3.10
'''

def check_substrings():
    check1 = 'x' in 'root:x:bin'
    print("'x' in 'root:x:bin':", check1)

    check2 = 'bash' in '/user/bin/bash:sh'
    print("'bash' in '/user/bin/bash:sh':", check2)

    check3 = 'oracle' in 'root:/usr/bin/sq1'
    print("'oracle' in 'root:/usr/bin/sq1':", check3)

    check4 = '-' in 'useA-userB--userC'
    print("'-' in 'useA-userB--userC':", check4)

check_substrings()
