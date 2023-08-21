import os
import platform
import tkinter as tk
from tkinter import ttk
from scripts.config_manager import ConfigManager

# Settings Window class is deprecated and should be deleted
# Keep for now, until finalized
# Aug 20, 2023

class SettingsWindow(tk.Toplevel):

  def __init__(self, master=None):
    super().__init__(master)
    self.title("Settings")
    self.geometry('900x400')
    self.configure(bg='#a9927d')

    script_dir = os.path.dirname(os.path.abspath(__file__))
    self.config_manager = ConfigManager(os.path.join(script_dir, "config.json"))
    self.config_data = self.config_manager.read_config() or {}

    # Sidebar Frame
    self.sidebar_frame = tk.Frame(self, bg='#a9927d', width=250)
    self.sidebar_frame.grid(row=0, column=0, sticky="ns")
    self.grid_rowconfigure(0, weight=1)  # Make the row stretchable

    # Content Frame
    self.content_canvas = tk.Canvas(self, bg='#5c5241')
    self.content_canvas.grid(row=0, column=1, sticky="nsew")
    self.content_scrollbar = tk.Scrollbar(self, command=self.content_canvas.yview)
    self.content_scrollbar.grid(row=0, column=2, sticky='ns')
    self.content_canvas.config(yscrollcommand=self.content_scrollbar.set)

    if platform.system() == "Darwin":  # macOS
      self.content_canvas.bind('<Button-4>', self.on_mousewheel_mac)
      self.content_canvas.bind('<Button-5>', self.on_mousewheel_mac)
    else:  # Windows and Linux
      self.content_canvas.bind('<MouseWheel>', self.on_mousewheel)

    self.content_canvas.config(yscrollcommand=self.content_scrollbar.set)

    # Content Frame inside Canvas
    self.content_frame = tk.Frame(self.content_canvas, bg='#5c5241', relief="sunken")
    self.content_window = self.content_canvas.create_window((0,0), window=self.content_frame, anchor="nw")

    self.content_canvas.bind("<Configure>", self.on_canvas_configure)
    self.grid_columnconfigure(1, weight=1)

    # Add buttons/tabs to the sidebar
    button_names = ["Button 1", "Button 2", "Button 3", "Button 4", "Button 5", "Button 6"]
    for i, btn_name in enumerate(button_names):
      btn = tk.Label(self.sidebar_frame, text=btn_name, bg='#a9927d', fg='#5c5241', pady=15, padx=10, bd=1, relief='solid')
      btn.grid(row=i, column=0, sticky="new", pady=5, padx=10)
      btn.bind("<Button-1>", self.change_tab)
      btn.bind("<Enter>", lambda e, b=btn: b.config(bg='#5c5241', fg='#a9927d'))  # Hover in
      btn.bind("<Leave>", lambda e, b=btn: b.config(bg='#a9927d', fg='#5c5241'))  # Hover out

  def on_mousewheel_mac(self, event):
    self.content_canvas.yview_scroll(-1 if event.num == 4 else 1, "units")

  def on_canvas_configure(self, event):
    width = self.content_canvas.winfo_width() if not event else event.width
    self.content_canvas.itemconfig(self.content_window, width=width)
    self.content_canvas.configure(scrollregion=self.content_canvas.bbox("all"))

  def on_mousewheel(self, event):
    self.content_canvas.yview_scroll(-1*(event.delta//120), "units")

  def change_tab(self, event):
    for widget in self.content_frame.winfo_children():
      widget.destroy()

    clicked_label = event.widget.cget("text")

    if clicked_label == "Button 5":
      self.kill_all_config()
    elif clicked_label == "Button 6":
      self.clean_desktop_config()
    else:
      self.default_config()

  def default_config(self):
    fields = ["Name", "Links", "Apps", "Play Spotify", "Spotify Link"]
    for i, field in enumerate(fields):
      self.add_label_entry_pair(field, i)

  def kill_all_config(self):
    fields = ["Name", "Apps"]
    for i, field in enumerate(fields):
      self.add_label_entry_pair(field, i)

  def clean_desktop_config(self):
    fields = ["Name", "Ignore"]
    for i, field in enumerate(fields):
      self.add_label_entry_pair(field, i)

  def add_label_entry_pair(self, field, i):
    label = tk.Label(self.content_frame, text=field, bg='#5c5241', fg='#a9927d', padx=10, pady=5)
    label.grid(row=i, column=0, sticky="w", padx=20, pady=10)

    if field in ['Links', 'Apps', 'Ignore']:
      entry = tk.Entry(self.content_frame)
      entry.grid(row=i, column=1, padx=10, pady=10, sticky="ew")
      add_button = tk.Button(self.content_frame, text="Add", command=lambda e=entry: self.add_input_field(e))
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

  def move_widgets_down(self, start_row):
    for child in self.content_frame.winfo_children():
      info = child.grid_info()
      if int(info["row"]) > start_row:
        child.grid(row=int(info["row"])+1, column=int(info["column"]), padx=10, pady=10)

  def add_input_field(self, entry_widget):
    current_row = entry_widget.grid_info()["row"]
    current_col = entry_widget.grid_info()["column"]

    # Locate the "Add" button associated with the passed entry widget.
    add_button_widget = next((child for child in self.content_frame.winfo_children() 
                              if child.grid_info().get("row") == current_row 
                              and child.grid_info().get("column") == current_col + 1 
                              and isinstance(child, tk.Button)), None)
    
    # If the button widget is found, destroy it.
    if add_button_widget:
      add_button_widget.destroy()

    # Move all widgets below the current row down to make space for the new entry.
    self.move_widgets_down(current_row)

    # Create a new entry widget below the passed entry widget.
    new_entry = tk.Entry(self.content_frame)
    new_entry.grid(row=current_row+1, column=1, padx=10, pady=10, sticky="ew")

    # Add an 'Add' button next to the new entry field, which can also spawn new fields.
    add_button = tk.Button(self.content_frame, text="Add", command=lambda e=new_entry: self.add_input_field(e))
    add_button.grid(row=current_row+1, column=2, padx=10, pady=10)
    self.on_canvas_configure(None)

if __name__ == "__main__":
  root = tk.Tk()
  tk.Button(root, text="Open Settings", command=lambda: SettingsWindow(root)).pack(pady=20, padx=20)
  root.mainloop()
