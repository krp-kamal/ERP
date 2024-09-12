def productInfo(product_name, product_id, product_cost):
    tax_amount = product_cost * 0.18
    print(f"Product Name: {product_name}")
    print(f"Product ID: {product_id}")
    print(f"Product Cost: {product_cost}")
    print(f"Tax Amount * 18%: {tax_amount}")


product_name = input("Enter the product name: ")
product_id = int(input("Enter the product ID: "))
product_cost = float(input("Enter the product cost: "))


productInfo(product_name, product_id, product_cost)
