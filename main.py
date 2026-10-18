from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sqlite3
DATABASE_NAME = "bakery.db"
app = FastAPI()
class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=70)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
class StockUpdate(BaseModel):
    stock: int = Field(ge=0)
@app.get("/")
def home():
    return {"message": "Welcome to BakeryFlow API"}
@app.get("/products")
def get_products():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    products_list = []
    for product in rows:
        products_list.append({"id":  product[0], "name": product[1], "price": product[2], "stock": product[3]})
    connection.close()
    return products_list
@app.get("/products/low_stock")
def get_low_stock_products(limit: int = 10):
    connection = sqlite3.connect(DATABASE_NAME)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products where stock < ?", (limit, ))
        rows = cursor.fetchall()
    finally:
        connection.close()
    products_list = []
    for product in rows:
        products_list.append({"id":  product[0], "name": product[1], "price": product[2], "stock": product[3]})
    return products_list 
@app.patch("/products/{product_id}/stock")
def update_stock(product_id: int, update: StockUpdate):
    new_stock = update.stock
    connection = sqlite3.connect(DATABASE_NAME)
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))
        updated_count = cursor.rowcount
        connection.commit()
    finally:
        connection.close()
    if updated_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"id": product_id, "stock": new_stock}
@app.get("/products/{product_id}")
def get_product(product_id: int):
    connection = sqlite3.connect(DATABASE_NAME)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id, ))
        product = cursor.fetchone()
    finally:
        connection.close()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    prod = {"id": product[0], "name": product[1], "price": product[2], "stock": product[3]}
    return prod
@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    connection = sqlite3.connect(DATABASE_NAME)
    try:
        cursor = connection.cursor()
        new_product = product.model_dump()
        cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (new_product["name"], new_product["price"], new_product["stock"]))
        new_product["id"] = cursor.lastrowid
        connection.commit()
    finally:
        connection.close()
    return new_product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    connection = sqlite3.connect(DATABASE_NAME)
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id, ))
        deleted_count = cursor.rowcount
        connection.commit()
    finally:
        connection.close()
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product has been deleted successfully."} 
@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: ProductCreate):
    new_product = updated_product.model_dump()
    connection = sqlite3.connect(DATABASE_NAME)
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE products SET name = ?, price = ?, stock = ? WHERE id = ?",
                        (new_product["name"], new_product["price"], new_product["stock"], product_id))
        updated_count = cursor.rowcount
        connection.commit()
    finally:
        connection.close()
    if updated_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    new_product["id"] = product_id
    return new_product 



    



    




