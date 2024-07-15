'''
Author: Ms Rya
Version: 3.10
'''
FH= open('/Users/kamalperumal/Downloads/FileHandleRead.py')
for var in FH.readlines()[-2]:
    print(var.strip())
FH.close()
