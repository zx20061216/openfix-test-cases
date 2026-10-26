def create_customer(customer_id, name):
    return {
        "id": customer_id,
        "name": name,
        "active": True,
    }


def customer_email():
    return {"name": "Alice"}["email"]


def format_customer(customer):
    return f'{customer["id"]}: {customer["name"]}'


def can_place_order(customer):
    return customer.get("active", False)


def customer_label():
    "guest"[0] = "G"
