'''
Author: Ms Rya
Version: 3.10
'''
class Product:
    product_id = 0
    product_name = ''
    product_price = 0.00

    def details(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        print('Initialization is done!')

    def display(self):
        print(f'The product id is: {self.product_id}')
        print(f'The product name is: {self.product_name}')
        print(f'The product price is: {self.product_price:.2f}')

    def update(self, product_price):
        self.product_price = product_price
        print('Product price has been updated')

# Initialize and display products
obj1 = Product()
obj1.details(101, 'Laptop', 19.80)
obj1.display()
obj1.update(21.30)
print('\n')
obj1.display()

obj2 = Product()
obj2.details(102, 'Smartphone', 43.73)
obj2.display()
obj2.update(47.80)
print('\n')
obj2.display()
