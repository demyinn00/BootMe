import os
import json
import tkinter as tk
from scripts.config_manager import ConfigManager
from scripts.settings_ui_manager import SettingsUIManager
from scripts.main_ui_manager import MainUIManager

def open_settings():
  settings_window = tk.Toplevel(root)
  settings_manager = SettingsUIManager(settings_window, config_manager)

script_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(script_dir, "config.json")

root = tk.Tk()
root.title("BootMe")
root.geometry("450x300")
root.configure(bg="#a9927d")

title_label = tk.Label(root, text="BootMe", font=("Helvetica", 24), bg="#a9927d", fg="#5c5241")
title_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

edit_button = tk.Button(root, text="Settings", command=open_settings)
edit_button.grid(row=0, column=1, sticky="ne")

config_manager = ConfigManager(config_file_path)

main_ui = MainUIManager(root, config_manager)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=0)

for i in range(4): 
  root.grid_rowconfigure(i, weight=1)

root.mainloop()



