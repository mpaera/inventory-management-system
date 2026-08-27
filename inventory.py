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
    }
]


def get_all_items():
    return inventory


def get_item_by_id(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None


def add_item(item):
    new_id = max([item["id"] for item in inventory], default=0) + 1
    item["id"] = new_id
    inventory.append(item)
    return item


def update_item(item_id, updates):
    item = get_item_by_id(item_id)

    if item is None:
        return None

    item.update(updates)
    item["id"] = item_id

    return item


def delete_item(item_id):
    item = get_item_by_id(item_id)

    if item is None:
        return False

    inventory.remove(item)
    return True