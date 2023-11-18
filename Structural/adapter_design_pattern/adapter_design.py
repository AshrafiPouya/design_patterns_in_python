class Product:
    def __init__(self, name, type, price) -> None:
        self.type = type
        self.price = price
        self.name = name


class WageAdapter:
    def __init__(self) -> None:
        self.products = {}
        pass


    def calculate_wage(self, product):
        return (self.products[product.type] + 1) * product.price
    

    def add_wage(self, type, percent):
        self.products[type] = percent



if __name__ == "__main__":
    product1 = Product("a", "gold", price=120)
    product2 = Product("b", "silver", price=80)
    product3 = Product("c", "other", price=20)

    adapter = WageAdapter()
    adapter.add_wage("gold", 0.2)
    adapter.add_wage("silver", 0.1)
    adapter.add_wage("other", 0.5)

    print(adapter.calculate_wage(product1))
    print(adapter.calculate_wage(product2))
    print(adapter.calculate_wage(product3))
