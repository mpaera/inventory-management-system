Inventory Management API

A simple RESTful API built with Flask for managing inventory items. The API supports creating, reading, updating, and deleting inventory items. It also integrates with the OpenFoodFacts API to retrieve product information using a barcode.

Features

- View all inventory items
- View a single inventory item
- Add a new inventory item
- Update an existing inventory item
- Delete an inventory item
- Search for product information using a barcode
- Error handling for invalid or missing inventory items
- Automated tests using pytest

Technologies Used

- Python 3.8+
- Flask
- Requests
- Pytest
- OpenFoodFacts API

Project Structure

inventory-management-system/
│
├── app.py
├── inventory.py
├── external_api.py
├── cli.py
├── requirements.txt
├── README.md
│
└── tests/
    ├── test_inventory.py
    └── test_external_api.py

Installation

1. Clone the repository

git clone <your-github-repository-url>
cd inventory-management-system

2. Create a virtual environment

python3 -m venv venv

3. Activate the virtual environment

On Linux/macOS:

source venv/bin/activate

On Windows:

venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

Running the Application

Start the Flask application with:

python app.py

The API will normally be available at:

http://127.0.0.1:5000

API Endpoints

Home

GET /

Returns a message confirming that the Inventory Management API is running.

Get All Inventory

GET /inventory

Returns all inventory items.

Get One Inventory Item

GET /inventory/<id>

Returns a single inventory item using its ID.

Example:

GET /inventory/1

Add Inventory Item

POST /inventory

Example request body:

{
    "name": "Milk",
    "quantity": 10,
    "price": 250.00,
    "barcode": "600100000001"
}

Update Inventory Item

PUT /inventory/<id>

Example:

PUT /inventory/1

Request body:

{
    "name": "Updated Milk",
    "quantity": 25,
    "price": 300.00,
    "barcode": "600100000001"
}

Delete Inventory Item

DELETE /inventory/<id>

Example:

DELETE /inventory/1

OpenFoodFacts Integration

The application integrates with the OpenFoodFacts API to retrieve product information using a product barcode.

The external API is handled through "external_api.py".

The application sends a request using the product barcode and processes the response from OpenFoodFacts.

Running Tests

The project uses pytest for automated testing.

Run all tests with:

pytest

To see more detailed test output:

pytest -v

The test suite covers the inventory functionality and the external OpenFoodFacts API integration.

Error Handling

The API handles common errors such as:

- Inventory item not found
- Invalid inventory IDs
- Invalid request data
- External API request failures

Appropriate HTTP status codes are returned when errors occur.

Example Response

A successful inventory request may return:

[
    {
        "id": 1,
        "name": "Milk",
        "quantity": 10,
        "price": 250.00,
        "barcode": "600100000001"
    }
]

Author

Terry Mpaera

License

This project was created for educational purposes.