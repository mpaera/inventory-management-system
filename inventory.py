inventory = [
    {
        "id": 1,
        "name": "Milk",
        "quantity": 10,
        "price": 250.00,
        "barcode": "600100000001"
    },
    {
        "id": 2,
        "name": "Bread",
        "quantity": 20,
        "price": 150.00,
        "barcode": "600100000002"
    },
    {
        "id": 3,
        "name": "Sugar",
        "quantity": 15,
        "price": 180.00,
        "barcode": "600100000003"
    },
    {
        "id": 4,
        "name": "Rice",
        "quantity": 25,
        "price": 300.00,
        "barcode": "600100000004"
    }
]


def get_all_items():
    return inventory


def get_item_by_id(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None


def add_item(name, quantity, price, barcode):
    new_id = max([item["id"] for item in inventory], default=0) + 1

    new_item = {
        "id": new_id,
        "name": name,
        "quantity": quantity,
        "price": price,
        "barcode": barcode
    }

    inventory.append(new_item)
    return new_item


def update_item(item_id, name, quantity, price, barcode):
    item = get_item_by_id(item_id)

    if item is None:
        return None

    item["name"] = name
    item["quantity"] = quantity
    item["price"] = price
    item["barcode"] = barcode

    return item


def delete_item(item_id):
    item = get_item_by_id(item_id)

    if item is None:
        return False

    inventory.remove(item)
    return True