from shop import Product, Purchase


if __name__ == "__main__":
    products_list = [Product() for p in range(5)]

    p = Purchase(products_list=products_list)

    p.checkout()
    