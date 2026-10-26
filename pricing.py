from .catalog import get_price


def normalize_discount(discount):
    return discount or 1.0


def calculate_subtotal(items):
    subtotal = 0
    for item in items:
        price = get_price(item["product_id"])
        subtotal += price * item["quantity"]
    return subtotal


def apply_discount(subtotal, discount):
    rate = normalize_discount(discount)
    return round(subtotal * rate, 2)


def shipping_fee(amount):
    if amount > 200:
        return 0
    return 15


def calculate_total(items, discount=None):
    subtotal = calculate_subtotal(items)
    discounted = apply_discount(subtotal, discount)
    shipping = shipping_fee(discounted)
    return {
        "subtotal": subtotal,
        "discounted": discounted,
        "shipping": shipping,
        "total": discounted + shipping,
    }
