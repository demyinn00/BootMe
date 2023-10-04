import tkinter as tk
from tkinter import ttk, simpledialog
from scripts.backend.config_manager import ConfigManager
from scripts.ui.environment_field_manager import EnvironmentFieldManager

class SettingsUIManager:
    def __init__(self, root, config_manager):
        self.root = root
        self.root.geometry("550x450")
        self.config_manager = config_manager
        self.current_config = self.config_manager.read_config()
        self.fields_frame = tk.Frame(self.root)
        self.fields_frame.pack(pady=20, padx=20)
        self.env_field_manager = EnvironmentFieldManager(self.fields_frame, self.current_config, self.config_manager)
        self.BACKGROUND_COLOR = '#a9927d'
        self.FOREGROUND_COLOR = '#5c5241'
        self.build_ui()

    def build_ui(self):
        # Set the background color for the main window
        self.root.configure(bg=self.BACKGROUND_COLOR)

        # Create a top frame to hold the dropdown
        top_frame = tk.Frame(self.root, bg=self.BACKGROUND_COLOR)
        top_frame.pack(pady=10, padx=20, fill=tk.X)

        self.selection_var = tk.StringVar()
        envs = self.current_config["environments"]
        options = [env["name"] for env in envs]
        options.append("Kill All")
        options.append("Clean Desktop")

        # Pack the selection dropdown inside the top frame
        self.selection_dropdown = ttk.Combobox(top_frame, textvariable=self.selection_var, values=options)
        self.selection_dropdown.bind("<<ComboboxSelected>>", self.load_fields_for_selection)
        self.selection_dropdown.pack(pady=5, padx=10, anchor='center')

        # Configure and pack the fields_frame
        self.fields_frame.configure(bg=self.BACKGROUND_COLOR)
        self.fields_frame.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)

        # Pack the save_button
        self.save_button = tk.Button(self.root, text="Save Config", 
                                    bg=self.BACKGROUND_COLOR, 
                                    fg=self.FOREGROUND_COLOR, 
                                    command=lambda: 
                                        self.env_field_manager.save_config(self.selection_var.get()))
        self.save_button.pack(pady=10, anchor='center')

        # Ensure the main window and its widgets resize appropriately
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def load_fields_for_selection(self, event=None):
        for widget in self.fields_frame.winfo_children():
            widget.destroy()

        selection = self.selection_var.get()

        envs = self.current_config["environments"]
        names = [env["name"] for env in envs]
        names.append("Kill All")
        names.append("Clean Desktop")
        index = names.index(selection)
        if index < 4:
            self.env_field_manager.load_environment_fields(index)
        elif index == 4:
            self.env_field_manager.load_kill_all_fields()
        else:
            self.env_field_manager.load_clean_desktop_fields()
