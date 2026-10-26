PRODUCTS = {
    "P100": {"name": "Keyboard", "price": 100, "stock": 10},
    "P200": {"name": "Mouse", "price": 50, "stock": 20},
    "P300": {"name": "Monitor", "price": 800, "stock": 0},
}


def get_product(product_id):
    return PRODUCTS.get(product_id)


def get_price(product_id):
    product = get_product(product_id)
    if product is None:
        raise ValueError("Unknown product")
    return product["price"]


def is_available(product_id, quantity):
    product = get_product(product_id)
    if product is None:
        return False
    return product["stock"] >= quantity


def get_product_name(product_id):
    product = get_product(product_id)
    if product is None:
        return "Unknown"
    return product["name"]
