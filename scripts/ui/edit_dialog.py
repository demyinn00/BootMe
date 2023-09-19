import tkinter as tk

class EditDialog(tk.simpledialog.Dialog):
    def __init__(self, parent, title, initial_value):
        self.result_value = initial_value
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Edit:").grid(row=0)
        self.edit_entry = tk.Entry(master)
        self.edit_entry.insert(0, self.result_value)
        self.edit_entry.grid(row=0, column=1)
        return self.edit_entry

    def apply(self):
        self.result_value = self.edit_entry.get()