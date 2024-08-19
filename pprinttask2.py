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

ICR['ICR_NO'].append(101)
ICR['Sender_name'].append('IBM')
ICR['SenderDate'].append('1st Aug 2024')
ICR['Subject'].append('Conference')
ICR['ReceivedBy'].append('Mr.Arun')

print(type(ICR))
print(ICR.keys())

import pprint
pprint.pprint(ICR)
