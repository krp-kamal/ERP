'''
Author: Ms Rya
Version: 3.10
'''
ICR={}  

ICR['ICR_NO']=[]
ICR['Sender_name']=[]
ICR['Subject']=[]
ICR['SenderDate']=[]
ICR['ReceivedBy']=[]
print(type(ICR))
print(ICR.keys())

ICR['ICR_NO'].append(102)
ICR['Sender_name'].append('HSTA')
ICR['SenderDate'].append('2nd Aug 2024')
ICR['Subject'].append('Postal')
ICR['ReceivedBy'].append('Ms.Anu')

ICR['ICR_NO'].append(103)
ICR['Sender_name'].append('IBM')
ICR['SenderDate'].append('3rd Aug 2024')
ICR['Subject'].append('BBConf')
ICR['ReceivedBy'].append('Mr.Arun')

print(type(ICR))
print(ICR.keys())

wobj = open("E:\\ICR.log","a")

for var in ICR:
    wobj.write('{}\t{}\n'.format(var,ICR[var]))
    
wobj.close()    
