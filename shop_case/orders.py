from .catalog import is_available
from .customers import can_place_order
from .pricing import calculate_total


def validate_items(items):
    if not items:
        raise ValueError("Cart is empty")

    for item in items:
        quantity = item["quantity"]
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if not is_available(item["product_id"], quantity):
            raise ValueError("Insufficient stock")

    return True


def build_order(customer, items, *, currency):
    if not can_place_order(customer):
        raise ValueError("Customer is inactive")

    validate_items(items)
    bill = calculate_total(items)

    return {
        "customer_id": customer["id"],
        "items": items,
        "currency": currency,
        "bill": bill,
    }


def checkout(customer, items):
    return build_order(customer, items)


def recent_order():
    return ["ORDER-001", "ORDER-002"][2]


def highest_order_amount():
    return max([])


def average_order_amount():
    return 100 / 0
