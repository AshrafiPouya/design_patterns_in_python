from datetime import datetime

COUNTRIES = ['India', 'UAE']
VAT = {"India": 10, "UAE": 18}

class User:
    pass

class Address:
    def __init__(self, country) -> None:
        self.country = country

class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Purchase:
    def __init__(self, user, address,) -> None:
        self.user = user
        self.address = address
        self.products_list = []

    def add_products(self, product_list):
        if not isinstance(product_list, list):
            product_list = [product_list]

        self.products_list.extend(product_list)


    def total_price(self):
        s = 0

        for product in self.products_list:
            s += product.price
        
        return s
      

def calculate_tax(func):
    def wrapped_func(purchase):
        vat = VAT[purchase.address.country]
        total_price = purchase.total_price()
        
        return total_price + total_price * vat / 100

    return wrapped_func
 
def show_total_price(purchase):
    return purchase.total_price()

@calculate_tax
def show_tax_plus_price(purchase):
    return purchase.total_price()

if __name__ == "__main__":
    user  = User()
    
    address1 = Address(country=COUNTRIES[0])
    address2 = Address(country=COUNTRIES[1])

    product1 = Product('Product1', 250)
    product2 = Product('Product2', 910)
    product3 = Product('Product3', 170)

    p1 = Purchase(user=user, address=address1)
    p1.add_products(product1)
    p1.add_products([product2, product3])

    p2 = Purchase(user=user, address=address2)
    p2.add_products(product1)
    p2.add_products([product2, product3])
    
    print(show_total_price(purchase=p1))
    print(show_tax_plus_price(purchase=p1))
    
    print(show_total_price(purchase=p2))
    print(show_tax_plus_price(purchase=p2))