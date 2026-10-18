# BakeryFlow API 🥐

A RESTful backend API for bakery inventory management, built with **Python, FastAPI, and SQLite**.

BakeryFlow provides product management, inventory tracking, input validation, and automated API testing. It is a backend development project inspired by everyday bakery operations.

## Tech Stack

- **Python** — Application logic
- **FastAPI** — REST API framework and interactive documentation
- **SQLite** — Persistent relational database
- **Pydantic** — Request data validation
- **Pytest & HTTPX** — Automated API testing

## Features

- Create, retrieve, update, and delete bakery products
- Update stock quantities independently of other product details
- Find low-stock products with a configurable threshold
- Validate product inputs and return appropriate HTTP status codes
- Persist product data in SQLite
- Test API endpoints using a separate temporary SQLite database

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/products` | List all products |
| `GET` | `/products/{product_id}` | Retrieve a product by ID |
| `POST` | `/products` | Create a product |
| `PUT` | `/products/{product_id}` | Update product details |
| `DELETE` | `/products/{product_id}` | Delete a product |
| `PATCH` | `/products/{product_id}/stock` | Update product stock |
| `GET` | `/products/low_stock?limit=10` | Find products below a stock threshold |

## Example Requests

### Create a product

**POST** `/products`

```json
{
  "name": "Croissant",
  "price": 8.5,
  "stock": 20
}
```

### Update stock

**PATCH** `/products/1/stock`

```json
{
  "stock": 50
}
```

### Find low-stock products

**GET** `/products/low_stock?limit=10`

Returns products with stock below 10. The `limit` query parameter defaults to 10 when omitted.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/abomokhf-bgu/bakeryflow-api.git
cd bakeryflow-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Initialize the database

```bash
python database.py
```

### 5. Start the API

```bash
python -m uvicorn main:app --reload
```

Open the interactive Swagger UI at **http://127.0.0.1:8000/docs**.

## Automated Tests

Tests use FastAPI's `TestClient`, Pytest, and a separate temporary SQLite database so that application data is not modified.

Run the test suite:

```bash
python -m pytest test_main.py -v
```

The tests cover product retrieval, creation, updates, stock changes, and deletion.

## Future Improvements

- Order and sales management
- Automatic stock deduction when recording sales
- User authentication and authorization
- Database migrations
- Cloud deployment

## Project Purpose

BakeryFlow API demonstrates foundational backend engineering skills: RESTful API design, SQL operations, input validation, error handling, persistent storage, and automated testing.
