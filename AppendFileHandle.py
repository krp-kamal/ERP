'''
Author: Ms Rya
Version: 3.10
'''
robj= open ("/Users/kamalperumal/Downloads/FileHandleRead.py",'r')
wobj = open ("/Users/kamalperumal/Downloads/Read3.log",'w')
s = robj.read()
wobj.write(s)
wobj.write('genny\n')
wobj.write('April\n')
robj.close()
wobj.close()