import tkinter as tk
from tkinter import ttk

class UpdateExpenseWindow(tk.Toplevel):
    def __init__(self, parent, controller, refresh_callback, data):
        super().__init__(parent)
        self.controller = controller
        self.refresh_callback = refresh_callback
        self.data = data
        self.title("Edit Expense")
        w = 300
        h = 200
        x = (self.winfo_screenwidth()/2)-(w/2)
        y = (self.winfo_screenheight()/2)-(h/2)
        self.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')

        self.name_var = tk.StringVar()
        self.expense_var = tk.StringVar()
        self.amount_var = tk.IntVar()
        self.name_var.set(self.data[2])
        self.expense_var.set(self.data[3])
        self.amount_var.set(self.data[4])

        tk.Label(self, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Expense:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.expense_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Amount:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.amount_var).grid(row=2, column=1, padx=10, pady=5)

        frame = tk.Frame(self)
        frame.grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(frame, text="Update", command=self.save_update).pack(side="left", padx=10, pady=10)
        tk.Button(frame, text="Cancle", command=self.destroy).pack(side="left", padx=10, pady=10)
    
    def save_update(self):
        id = self.data[0]
        new_name = self.name_var.get()
        new_expense = self.expense_var.get()
        new_amount = self.amount_var.get()
        if new_name and new_expense and new_amount:
            self.controller.update_expense(id, new_name, new_expense, new_amount)
            self.refresh_callback()
            self.destroy()