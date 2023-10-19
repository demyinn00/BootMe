import os
import tkinter as tk
from scripts.backend.config_manager import ConfigManager
from scripts.ui.main_ui_manager import MainUIManager
from scripts.ui.settings_ui_manager import SettingsUIManager
from scripts.ui.help_ui_manager import HelpUIManager

settings_window = None
help_window = None

def open_settings():
    global settings_window
    if settings_window is None or not tk.Toplevel.winfo_exists(settings_window):
        settings_window = tk.Toplevel(root)
        settings_manager = SettingsUIManager(settings_window, config_manager)
        root.wait_window(settings_window)
        main_ui.refresh_buttons()

def open_help():
    global help_window
    if help_window is None or not tk.Toplevel.winfo_exists(help_window):
        help_window = tk.Toplevel(root)
        help_ui = HelpUIManager(help_window)
        root.wait_window(help_window)

script_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(script_dir, "config.json")

root = tk.Tk()
root.title("BootMe")
root.geometry("450x350")
root.configure(bg="#a9927d")

config_manager = ConfigManager(config_file_path)
main_ui = MainUIManager(root, config_manager, open_settings, open_help)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=0)

for i in range(4): 
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
