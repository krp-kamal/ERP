'''
Author: Ms Rya
Version: 3.10
'''
robj = open("/Users/kamalperumal/Downloads/r1.log", 'r')
wobj = open("/Users/kamalperumal/Downloads/r2.log" , 'w')
s = robj.read()
wobj.write(s)
robj.close()
wobj.close()