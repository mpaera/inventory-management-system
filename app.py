from flask import Flask, jsonify, request

from inventory import (
    get_all_items,
    get_item_by_id,
    add_item,
    update_item,
    delete_item
)

from external_api import get_product_by_barcode


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Inventory Management API is running"
    })


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(get_all_items())


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    item = get_item_by_id(item_id)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item)


@app.route("/inventory", methods=["POST"])
def create_inventory_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    required_fields = ["name", "quantity", "price", "barcode"]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Missing required field: {field}"
            }), 400

    item = add_item(data)

    return jsonify(item), 201


@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def patch_inventory_item(item_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    item = update_item(item_id, data)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item)


@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def remove_inventory_item(item_id):
    deleted = delete_item(item_id)

    if not deleted:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({
        "message": "Item deleted successfully"
    })


@app.route("/products/barcode/<barcode>", methods=["GET"])
def search_product_by_barcode(barcode):
    product = get_product_by_barcode(barcode)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product)


if __name__ == "__main__":
    app.run(debug=True)