'''
Author: Ms Rya
Version: 3.10
'''

def manage_products():
    products = {}

    while True:
        add_product = input('Would you like to add a product? (yes or no): ').strip().lower()
        if add_product == 'yes':
            product = input('Enter the product you would like to purchase: ')
            model_name = input('Enter the model name: ')
            cost = float(input('Enter the price: '))
            code = input('Enter the vendor code: ')
            products[product] = {'model_name': model_name, 'cost': cost, 'code': code}
        elif add_product == 'no':
            break

    print('These are the products priced above 1000:')
    for product, details in products.items():
        if details['cost'] > 1000:
            print(f"Product: {product}, Details: {details}")

    return products

def product_info(product, model_name, cost=0, code=""):
    product_details = {product: {'model_name': model_name, 'cost': cost, 'code': code}}
    
    print("Product Details:")
    for product, details in product_details.items():
        print(f"Product: {product}, Model Name: {details['model_name']}, Price: {details['cost']}, Vendor Code: {details['code']}")


products = manage_products()
