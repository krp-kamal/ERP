FH= open('/Users/kamalperumal/Downloads/FileHandleRead.py', 'r')
FH.readlines(3)
FH.readlines(4)
for var in FH.readlines():
    print(var.strip())
FH.close()
