import tkinter as tk
from tkinter import simpledialog

class EditDialog(simpledialog.Dialog):
    def __init__(self, parent, title, initial_value):
        self.result_value = initial_value
        self.delete_flag = False
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text="Edit:").grid(row=0)
        self.edit_entry = tk.Entry(master)
        self.edit_entry.insert(0, self.result_value)
        self.edit_entry.grid(row=0, column=1)
        return self.edit_entry

    def apply(self):
        self.result_value = self.edit_entry.get()

    def buttonbox(self):
        box = tk.Frame(self)

        w = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="Delete", width=10, command=self.delete_item)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def delete_item(self):
        self.delete_flag = True
        self.ok()
