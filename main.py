import os
import json
import tkinter as tk
from scripts.backend.config_manager import ConfigManager
from scripts.ui.settings_ui_manager import SettingsUIManager
from scripts.ui.main_ui_manager import MainUIManager

def open_settings():
    settings_window = tk.Toplevel(root)
    settings_manager = SettingsUIManager(settings_window, config_manager)

    root.wait_window(settings_window)
    main_ui.refresh_buttons()

script_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(script_dir, "config.json")

root = tk.Tk()
root.title("BootMe")
root.geometry("450x300")
root.configure(bg="#a9927d")

title_label = tk.Label(root, text="BootMe", font=("Helvetica", 24), bg="#a9927d", fg="#5c5241")
title_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

settings_button = tk.Button(root, text="Settings", command=open_settings)
settings_button.grid(row=0, column=1, sticky="ne")

config_manager = ConfigManager(config_file_path)

main_ui = MainUIManager(root, config_manager, open_settings)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=0)

for i in range(4): 
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
