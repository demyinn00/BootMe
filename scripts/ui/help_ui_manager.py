import tkinter as tk

class HelpUIManager:
    def __init__(self, root_frame):
        self.root_frame = root_frame
        self.create_help_content()

    def create_help_content(self):
        # Add your help content here. For example:
        help_text = """Directions on how to use the app:
        1. Step 1
        2. Step 2
        ...
        """
        help_label = tk.Label(self.root_frame, text=help_text, wraplength=400)
        help_label.pack(padx=10, pady=10)
