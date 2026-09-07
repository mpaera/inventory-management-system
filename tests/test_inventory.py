from app import app


def test_get_inventory():
    client = app.test_client()

    response = client.get("/inventory")

    assert response.status_code == 200

    data = response.get_json()

    assert isinstance(data, list)


def test_get_single_inventory_item():
    client = app.test_client()

    response = client.get("/inventory/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1


def test_create_inventory_item():
    client = app.test_client()

    new_item = {
        "name": "Sugar",
        "quantity": 30,
        "price": 100.00,
        "barcode": "600100000003"
    }

    response = client.post("/inventory", json=new_item)

    assert response.status_code in [200, 201]

    data = response.get_json()

    assert data["name"] == "Sugar"
    assert data["quantity"] == 30


def test_update_inventory_item():
    client = app.test_client()

    updated_item = {
        "name": "Updated Milk",
        "quantity": 25,
        "price": 300.00,
        "barcode": "600100000001"
    }

    response = client.put("/inventory/1", json=updated_item)

    assert response.status_code == 200

    data = response.get_json()

    assert data["name"] == "Updated Milk"
    assert data["quantity"] == 25


def test_delete_inventory_item():
    client = app.test_client()

    response = client.delete("/inventory/1")

    assert response.status_code in [200, 204]