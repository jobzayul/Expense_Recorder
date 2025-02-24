from database import Database

class ExpenseController:
    def __init__(self):
        self.db = Database()  # <--- สร้างอ็อบเจกต์ database

    def add_expense(self, name, expense, amount):
        if name and amount > 0:
            self.db.add_expense(name, expense, amount)

    def get_expenses(self):
        return self.db.get_expenses()

    def delete_expense(self, expense_id):
        self.db.delete_expense(expense_id)

    def update_expense(self, expense_id, name, amount):
        self.db.update_expense(expense_id, name, amount)


if __name__ == "__main__":
    controller = ExpenseController()
    controller.add_expense("Lunch", 12.99, 1)
    controller.delete_expense(4)
    controller.update_expense(3, "Dinner", 19.99)
    for i in controller.get_expenses():
        print(i)
    
    