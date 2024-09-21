'''
Author: Ms Rya
Version: 3.10
'''

def create_icr_record():
    ICR = {
        'ICR_NO': [],
        'Sender_name': [],
        'Subject': [],
        'SenderDate': [],
        'ReceivedBy': []
    }

    return ICR

def add_icr_entry(ICR, icr_no, sender_name, sender_date, subject, received_by):
    ICR['ICR_NO'].append(icr_no)
    ICR['Sender_name'].append(sender_name)
    ICR['SenderDate'].append(sender_date)
    ICR['Subject'].append(subject)
    ICR['ReceivedBy'].append(received_by)

ICR = create_icr_record()

print(type(ICR))
print(ICR.keys())

add_icr_entry(ICR, 101, 'IBM', '1st Aug 2024', 'Conference', 'Mr.Arun')

print(type(ICR))
print(ICR.keys())

import pprint
pprint.pprint(ICR)
