# BakeryFlow API 🥐

A RESTful backend API for bakery inventory management, built with Python, FastAPI, and SQLite.

The project was developed to practice backend engineering concepts through a practical bakery management use case, including product management, inventory tracking, database persistence, input validation, and automated testing.

# Tech Stack

* Python — Backend development
* FastAPI — REST API framework
* SQLite — Relational database
* Pydantic — Request validation
* Pytest — Automated testing
* HTTPX — API testing support

# Features

* Create new bakery products
* Retrieve all products or a specific product by ID
* Update product details
* Delete products
* Update product stock independently
* Identify products with low inventory
* Customize low-stock thresholds using query parameters
* Validate incoming requests and return appropriate HTTP errors
* Persist product information in an SQLite database
* Run automated API tests using an isolated test database

# API Endpoints

Method	Endpoint	Description
GET	/products	Retrieve all products
GET	/products/{product_id}	Retrieve a product by ID
POST	/products	Create a product
PUT	/products/{product_id}	Update product details
DELETE	/products/{product_id}	Delete a product
PATCH	/products/{product_id}/stock	Update product stock
GET	/products/low_stock	Retrieve products with low stock

Example: Create a Product

POST /products

Request body:

{
  "name": "Croissant",
  "price": 8.5,
  "stock": 20
}

Example: Update Stock

PATCH /products/1/stock

Request body:

{
  "stock": 50
}

Example: Low-Stock Products

GET /products/low_stock?limit=10

Returns products with stock quantities below the specified threshold.

# Installation

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/bakeryflow-api.git
cd bakeryflow-api

2. Create a virtual environment

python -m venv .venv

Activate it on Windows:

.\.venv\Scripts\Activate.ps1

3. Install dependencies

pip install -r requirements.txt

4. Initialize the database

python database.py

5. Start the API

uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation (Swagger UI):

http://127.0.0.1:8000/docs

# Automated Testing

The project uses pytest and FastAPI’s TestClient to verify API behavior.

Tests cover:

* Retrieving products
* Creating and persisting products
* Updating product stock
* Deleting products

Tests use a separate temporary SQLite database to avoid modifying application data.

Run the tests:

python -m pytest test_main.py -v

# Future Improvements

* Order and sales management
* Automatic inventory deduction after purchases
* User authentication and authorization
* Database migrations
* Deployment to a cloud platform

Project Purposes:
BakeryFlow API demonstrates foundational backend development skills, including RESTful API design, SQL database operations, request validation, error handling, and automated testing.