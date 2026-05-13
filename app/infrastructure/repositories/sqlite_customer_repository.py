import sqlite3
from app.domain.customer import Customer, CustomerRepository


class SQLiteCustomerRepository(CustomerRepository):
    def __init__(self, db_path: str = "customers.db") -> None:
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            """)
            cursor = conn.execute("SELECT COUNT(*) FROM customers")
            if cursor.fetchone()[0] == 0:
                conn.execute(
                    "INSERT INTO customers (name, email) VALUES (?, ?)",
                    ("Ana Flask", "ana@flask.com"),
                )
                conn.execute(
                    "INSERT INTO customers (name, email) VALUES (?, ?)",
                    ("Bruno Flask", "bruno@flask.com"),
                )

    def list_customers(self) -> list[Customer]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT id, name, email FROM customers")
            return [
                Customer(id=row[0], name=row[1], email=row[2])
                for row in cursor.fetchall()
            ]
