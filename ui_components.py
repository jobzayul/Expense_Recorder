import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controller import ExpenseController
from add_expense import AddExpenseWindow
from update_expense import UpdateExpenseWindow

class ExpenseApp:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Expense Tracker")
        self.w = 750
        self.h = 600
        self.x = (self.root.winfo_screenwidth()/2)-(self.w/2)
        self.y = (self.root.winfo_screenheight()/2)-(self.h/2)
        self.root.geometry(f'{self.w}x{self.h}+{self.x:.0f}+{self.y:.0f}')
        self.root.resizable(False,False)

        # Input fields
        tk.Label(root,text='Expense Items', font=('Arial',30,'bold'),fg= 'green').pack(pady=20)

        self.F1 = tk.Frame(root)
        self.F1.pack(padx = 10)
        self.header = ['id','date','name','expense','amout']
        self.headerwidth = [70,200,200,80,80]

        self.tree = ttk.Treeview(self.F1,columns=self.header,show='headings',height=20)
        self.tree.pack()

        for h in self.header:
            self.tree.heading(h,text=h)

        for h,w in zip(self.header,self.headerwidth):
            self.tree.column(h,width=w)
        # resulttable.insert('','end',values=('1','2','3','4','5','6','7'))

        self.F2 = tk.Frame(root)
        self.F2.pack(pady = 20)
        tk.Button(self.F2,text='Add',font=('Arial',20,'bold'),fg='green',command=self.add_expense).pack(side='left',padx = 10, ipadx=30)
        tk.Button(self.F2,text='Edit',font=('Arial',20,'bold'),fg='green',command=self.update_expense).pack(side='left',padx = 10, ipadx=30)
        tk.Button(self.F2,text='Delete',font=('Arial',20,'bold'),fg='green',command=self.delete_expense).pack(side='left',padx = 10, ipadx=30)
        tk.Button(self.F2,text='Refresh',font=('Arial',20,'bold'),fg='green',command=self.load_expenses).pack(side='left',padx = 10, ipadx=30)

        self.load_expenses()

    def run(self):
        self.root.mainloop()

    def load_expenses(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for expense in self.controller.get_expenses():
            self.tree.insert("", "end", values=expense)

    def add_expense(self):
        AddExpenseWindow(self.root, self.controller, self.load_expenses)

    def update_expense(self):
        selected_item = self.tree.selection()  # รับแถวที่ถูกเลือก
        if selected_item:
            item = self.tree.item(selected_item)
            UpdateExpenseWindow(self.root, self.controller, self.load_expenses, item["values"])

    def delete_expense(self):
        if messagebox.askyesno("","Do you want to delete this item?") == True:
            selected_item = self.tree.selection()  # รับแถวที่ถูกเลือก
            if selected_item:
                item = self.tree.item(selected_item)
                id = item["values"][0]
                self.controller.delete_expense(id)
                self.load_expenses()
                