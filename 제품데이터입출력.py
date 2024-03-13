import sqlite3
import random
import string

class ProductManager:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                price REAL
                                )''')
        self.conn.commit()

    def insert_product(self, name, price):
        self.cursor.execute('''INSERT INTO products (name, price) VALUES (?, ?)''', (name, price))
        self.conn.commit()

    def update_product(self, product_id, name, price):
        self.cursor.execute('''UPDATE products SET name = ?, price = ? WHERE id = ?''', (name, price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''DELETE FROM products WHERE id = ?''', (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        self.cursor.execute('''SELECT * FROM products WHERE id = ?''', (product_id,))
        return self.cursor.fetchone()

def generate_random_product_name():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def generate_random_price():
    return round(random.uniform(10.0, 1000.0), 2)

if __name__ == "__main__":
    manager = ProductManager()

    # Insert sample data
    for _ in range(100):
        name = generate_random_product_name()
        price = generate_random_price()
        manager.insert_product(name, price)

    # Update a product
    manager.update_product(1, 'New Product Name', 999.99)

    # Delete a product
    manager.delete_product(2)

    # Select a product
    product = manager.select_product(3)
    print("Selected product:", product)

    # Close the connection
    manager.conn.close()
