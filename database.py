import sqlite3

class Database:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    name TEXT,
                    expense REAL,       
                    amount INTEGER
            )
        """)
        self.conn.commit()

    def add_expense(self, name, expense, amount):
        self.cursor.execute("INSERT INTO expenses (name, expense, amount)VALUES (?, ?, ?)", (name, expense, amount))
        self.conn.commit()

    def get_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        return self.cursor.fetchall()

    def delete_expense(self, id):
        self.cursor.execute("DELETE FROM expenses WHERE id=?", (id,))
        self.conn.commit()

    def update_expense(self, id, name, expense, amount):
        self.cursor.execute("UPDATE expenses SET name=?, expense=?, amount=? WHERE id=?", (name, expense, amount, id))
        self.conn.commit()

    def close(self):
        self.conn.close()
