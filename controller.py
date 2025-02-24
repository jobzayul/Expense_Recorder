from database import Database

class ExpenseController:
    def __init__(self):
        self.db = Database()  # <--- สร้างอ็อบเจกต์ database

    def add_expense(self, name, expense, amount):
        if name and amount > 0:
            self.db.add_expense(name, expense, amount)

    def get_expenses(self):
        return self.db.get_expenses()

    def delete_expense(self, id):
        self.db.delete_expense(id)

    def update_expense(self, id, name, expense, amount):
        self.db.update_expense(id, name, expense, amount)
    