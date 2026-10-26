from .customers import create_customer, format_customer
from .orders import checkout
from .pricing import calculate_total


def sample_items():
    return [
        {"product_id": "P100", "quantity": 1},
        {"product_id": "P200", "quantity": 2},
    ]


def preview_regular_order():
    return calculate_total(sample_items())


def preview_free_order():
    return calculate_total(sample_items(), discount=0)


def preview_threshold_order():
    items = [{"product_id": "P100", "quantity": 2}]
    return calculate_total(items)


def submit_sample_order():
    customer = create_customer("C001", "Alice")
    return checkout(customer, sample_items())


def display_customer():
    customer = create_customer("C001", "Alice")
    return format_customer(customer)
