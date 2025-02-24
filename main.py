import tkinter as tk
import ui_components as ui
import controller as cont

if __name__ == "__main__":
    root = tk.Tk()
    controller = cont.ExpenseController()
    App = ui.ExpenseApp(root, controller)
    App.run()