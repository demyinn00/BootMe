import tkinter as tk
from tkinter import ttk

class SettingsWindow(tk.Toplevel):

  def __init__(self, master=None):
    super().__init__(master)
    self.title("Settings")
    self.geometry('900x400')
    self.configure(bg='#a9927d')

    # Sidebar Frame
    self.sidebar_frame = tk.Frame(self, bg='#a9927d', width=250)
    self.sidebar_frame.grid(row=0, column=0, sticky="ns")
    self.grid_rowconfigure(0, weight=1)  # Make the row stretchable

    # Content Frame
    self.content_frame = tk.Frame(self, bg='#5c5241', width=650, relief="sunken")
    self.content_frame.grid(row=0, column=1, sticky="nsew")
    self.grid_columnconfigure(1, weight=1)

    # Add buttons/tabs to the sidebar
    button_names = ["Button 1", "Button 2", "Button 3", "Button 4", "Button 5", "Button 6"]
    for i, btn_name in enumerate(button_names):
      btn = tk.Label(self.sidebar_frame, text=btn_name, bg='#a9927d', fg='#5c5241', pady=15, padx=10, bd=1, relief='solid')
      btn.grid(row=i, column=0, sticky="new", pady=5, padx=10)
      btn.bind("<Button-1>", self.change_tab)
      btn.bind("<Enter>", lambda e, b=btn: b.config(bg='#5c5241', fg='#a9927d'))  # Hover in
      btn.bind("<Leave>", lambda e, b=btn: b.config(bg='#a9927d', fg='#5c5241'))  # Hover out

  def change_tab(self, event):
    for widget in self.content_frame.winfo_children():
      widget.destroy()

    # Create and grid labels and input fields for the configuration settings:
    fields = ['Name', 'Links', 'Apps', 'Play Spotify', 'Spotify Link']
    for i, field in enumerate(fields):
      label = tk.Label(self.content_frame, text=field, bg='#5c5241', fg='#a9927d', padx=10, pady=5)
      label.grid(row=i, column=0, sticky="w", padx=20, pady=10)

      if field in ['Links', 'Apps']:
        entry = tk.Entry(self.content_frame)
        entry.grid(row=i, column=1, padx=10, pady=10, sticky="ew")
        add_button = tk.Button(self.content_frame, text="Add", command=self.add_input_field)
        add_button.grid(row=i, column=2, padx=10, pady=10)
      elif field == 'Play Spotify':
        options = ['Yes', 'No']
        dropdown = ttk.Combobox(self.content_frame, values=options, state='readonly')
        dropdown.set(options[0])
        dropdown.grid(row=i, column=1, padx=10, pady=10, sticky="ew")
      else:
        entry = tk.Entry(self.content_frame)
        entry.grid(row=i, column=1, padx=10, pady=10, sticky="ew")

    self.content_frame.grid_columnconfigure(1, weight=1)

  def add_input_field(self):
    pass  # This function will add an additional input field below the current one. You can implement this further.

if __name__ == "__main__":
  root = tk.Tk()
  tk.Button(root, text="Open Settings", command=lambda: SettingsWindow(root)).pack(pady=20, padx=20)
  root.mainloop()
