import requests


OPENFOODFACTS_URL = "https://world.openfoodfacts.org/api/v2/product"

HEADERS = {
    "User-Agent": "InventoryManagementSystem/1.0 (inventory-management-system)"
}


def get_product_by_barcode(barcode):
    url = f"{OPENFOODFACTS_URL}/{barcode}.json"

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            print(f"Open Food Facts API error: {response.status_code}")
            return None

        data = response.json()

    except requests.RequestException as error:
        print(f"Request error: {error}")
        return None

    except ValueError:
        print("Invalid JSON response from Open Food Facts")
        return None

    if data.get("status") != 1:
        return None

    product = data.get("product", {})

    return {
        "barcode": data.get("code", barcode),
        "name": product.get("product_name", "Unknown product"),
        "brand": product.get("brands", ""),
        "quantity": 0,
        "price": 0.0,
        "image_url": product.get("image_url", "")
    }