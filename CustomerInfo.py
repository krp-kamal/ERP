'''
Author: Ms Rya
Version: 3.10
'''
import time
def customerInfo():
    customer_name = input("Enter Customer Name: ")
    customer_id = int(input("Enter Customer ID: "))
    contact_number =int( input("Enter Contact Number: "))
    address = input("Enter Address: ")
    product_details = f'''\nCustomer Details:
Name: {customer_name}
Customer ID: {customer_id}
Contact Number: {contact_number}
Address: {address}
'''
  
    print(product_details)

    with open('customer.csv', mode='a') as file:
        file.write(f"{customer_name},{customer_id},{contact_number},{address}\n")

limit = 5
count = 0

while count < limit:
    customerInfo()
    count += 1
    time.sleep(2)
