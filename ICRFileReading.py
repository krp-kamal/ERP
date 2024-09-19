'''
Author: Ms Rya
Version: 3.10
'''

def icr_records(file_path):
    ICR = {
        'ICR_NO': [],
        'Sender_name': [],
        'Subject': [],
        'SenderDate': [],
        'ReceivedBy': []
    }
    
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
    print('Text has been appended')
    
    with open(file_path, "a") as wobj:
        for var in ICR:
            wobj.write('{}\t{}\n'.format(var, ICR[var]))
            

file_path = "/Users/kamalperumal/Downloads/ICR.log"
icr_records(file_path)
