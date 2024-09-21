'''
Author: Ms Rya
Version: 3.10
'''

def check_enquiry_number(enquiry_number):
    if enquiry_number > 5000:
        return "Enquiry number is above 5000."
    else:
        return "Enquiry number is not above 5000."

enquiry_number = int(input("Enter business enquiry number: "))

print(check_enquiry_number(enquiry_number))
