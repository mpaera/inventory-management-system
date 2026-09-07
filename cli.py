import requests

BASE_URL = "http://127.0.0.1:5000"


def list_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        items = response.json()

        if not items:
            print("No inventory items found.")
            return

        for item in items:
            print(
                f"ID: {item['id']} | "
                f"Name: {item['name']} | "
                f"Quantity: {item['quantity']} | "
                f"Price: {item['price']} | "
                f"Barcode: {item['barcode']}"
            )
    else:
        print("Failed to fetch inventory.")


def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    barcode = input("Enter barcode: ")

    data = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "barcode": barcode
    }

    response = requests.post(f"{BASE_URL}/inventory", json=data)

    if response.status_code in [200, 201]:
        print("Item added successfully.")
        print(response.json())
    else:
        print("Failed to add item.")
        print(response.text)


def get_item():
    item_id = input("Enter item ID: ")

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        print(response.json())
    else:
        print("Item not found.")


def update_item():
    item_id = input("Enter item ID: ")

    name = input("Enter new name: ")
    quantity = int(input("Enter new quantity: "))
    price = float(input("Enter new price: "))
    barcode = input("Enter new barcode: ")

    data = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "barcode": barcode
    }

    response = requests.put(
        f"{BASE_URL}/inventory/{item_id}",
        json=data
    )

    if response.status_code == 200:
        print("Item updated successfully.")
        print(response.json())
    else:
        print("Failed to update item.")
        print(response.text)


def delete_item():
    item_id = input("Enter item ID: ")

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    if response.status_code in [200, 204]:
        print("Item deleted successfully.")
    else:
        print("Failed to delete item.")
        print(response.text)


def main():
    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. List inventory")
        print("2. Add item")
        print("3. Get item")
        print("4. Update item")
        print("5. Delete item")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_inventory()

        elif choice == "2":
            add_item()

        elif choice == "3":
            get_item()

        elif choice == "4":
            update_item()

        elif choice == "5":
            delete_item()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()