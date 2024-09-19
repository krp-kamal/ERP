'''
Author: Ms Rya
Version: 3.10
'''

def create_icr_records():
    ICR = {
        'ICR_NO': [],
        'Sender_name': [],
        'Subject': [],
        'SenderDate': [],
        'ReceivedBy': []
    }
    
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
    
    for var in ICR:
        print('{}\t{}'.format(var, ICR[var]))


create_icr_records()
