import sqlite3
import pytest
import main
from fastapi.testclient import TestClient
client = TestClient(main.app)
@pytest.fixture
def test_db(tmp_path, monkeypatch):
    db_path = tmp_path / "test_bakery.db"
    connection = sqlite3.connect(db_path)
    connection.execute(""" CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL NOT NULL, stock INTEGER NOT NULL)""")
    connection.commit()
    connection.close()
    monkeypatch.setattr(main, "DATABASE_NAME", str(db_path))

def test_get_products(test_db):
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == []
def test_create_product(test_db):
    product = {"name": "Croissant", "price": 8.5, "stock": 20}
    response = client.post("/products", json=product)
    assert response.status_code == 201 
    get_response = client.get("/products")
    assert get_response.status_code == 200
    products = get_response.json()
    assert len(products) == 1
    assert products[0]["name"] == "Croissant"
    assert products[0]["price"] == 8.5
    assert products[0]["stock"] == 20
def test_update_stock(test_db):
    product = {"name": "Croissant", "price": 8.5, "stock": 20}
    response = client.post("/products", json=product)
    assert response.status_code == 201
    products = client.get("/products").json()
    product_id = products[0]["id"]
    response = client.patch(f"/products/{product_id}/stock", json={"stock": 50})
    assert response.status_code == 200
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    updated_product = response.json()
    assert updated_product["stock"] == 50
    assert updated_product["name"] == "Croissant"
    assert updated_product["price"] == 8.5
def test_delete_product(test_db):
    product = {"name": "Bread", "price": 5.0, "stock": 30}
    response = client.post("/products", json=product)
    assert response.status_code == 201
    products = client.get("/products").json()
    product_id = products[0]["id"]
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 404
    response = client.get("/products")
    assert response.json() == []
