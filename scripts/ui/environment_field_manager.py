import os
import platform
import tkinter as tk
from tkinter import filedialog
from scripts.backend.config_manager import ConfigManager
from scripts.backend.workflows import invalidate_config_cache
from scripts.backend.spoticry import Spoticry
from scripts.ui.edit_dialog import EditDialog

class EnvironmentFieldManager:
    def __init__(self, fields_frame, current_config, config_manager, save_callback=None):
        self.fields_frame = fields_frame
        self.config_manager = config_manager
        self.current_config = current_config
        self.save_callback = save_callback

    def load_environment_fields(self, index):
        environment = self.current_config["environments"][index]

        # Configure grid columns and rows to expand with the window
        self.fields_frame.grid_columnconfigure(0, weight=1)
        self.fields_frame.grid_columnconfigure(1, weight=2)
        self.fields_frame.grid_columnconfigure(2, weight=1)
        for i in range(8):
            self.fields_frame.grid_rowconfigure(i, weight=1)

        # Name field
        name_label = tk.Label(self.fields_frame, text="Name:")
        name_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(self.fields_frame)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.name_entry.insert(0, environment["name"])

        # Links fields
        links_label = tk.Label(self.fields_frame, text="Links:")
        links_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.link_entry = tk.Entry(self.fields_frame)
        self.link_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        add_link_button = tk.Button(self.fields_frame, text="Add Link", command=self.add_link)
        add_link_button.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
        self.links_listbox = tk.Listbox(self.fields_frame, height=4)
        self.links_listbox.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        self.links_listbox.bind("<Double-Button-1>", self.edit_link)

        for link in environment["links"]:
            self.links_listbox.insert(tk.END, link)

        # Apps fields
        apps_label = tk.Label(self.fields_frame, text="Apps:")
        apps_label.grid(row=5, column=0, sticky="e", padx=5, pady=5)
        self.apps_listbox = tk.Listbox(self.fields_frame, height=4)
        self.apps_listbox.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
        add_app_button = tk.Button(self.fields_frame, text="Add App", command=self.add_app)
        add_app_button.grid(row=5, column=2, sticky="ew", padx=5, pady=5)
        self.apps_listbox.bind("<Double-Button-1>", self.edit_app)

        for app in environment["apps"]:
            self.apps_listbox.insert(tk.END, app)

        # Spotify Link field
        spotify_link_label = tk.Label(self.fields_frame, text="Spotify Link:")
        spotify_link_label.grid(row=7, column=0, sticky="e", padx=5, pady=5)
        self.spotify_link_entry = tk.Entry(self.fields_frame)
        self.spotify_link_entry.grid(row=7, column=1, columnspan=2, sticky="ew", padx=5, pady=5)
        self.spotify_link_entry.insert(0, environment["spotify_url"])

    def load_kill_all_fields(self):
        # Configure grid columns and rows to expand with the window
        self.fields_frame.grid_columnconfigure(0, weight=1)
        self.fields_frame.grid_columnconfigure(1, weight=2)
        self.fields_frame.grid_columnconfigure(2, weight=1)
        for i in range(3):  # Assuming 3 rows for this method
            self.fields_frame.grid_rowconfigure(i, weight=1)

        # Apps fields
        apps_label = tk.Label(self.fields_frame, text="Apps to Kill:")
        apps_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        
        # Move the listbox up to row 0, column 1
        self.apps_kill_listbox = tk.Listbox(self.fields_frame, height=4)
        self.apps_kill_listbox.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.apps_kill_listbox.bind("<Double-Button-1>", self.edit_app_kill)

        # Move the "Add App" button up to row 0, column 2
        add_app_kill_button = tk.Button(self.fields_frame, text="Add App", command=self.add_app_kill)
        add_app_kill_button.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

        for app in self.current_config["workflows"]["kill_all_apps"]:
            self.apps_kill_listbox.insert(tk.END, app)


    def load_clean_desktop_fields(self):
        # Configure grid columns and rows to expand with the window
        self.fields_frame.grid_columnconfigure(0, weight=1)
        self.fields_frame.grid_columnconfigure(1, weight=2)
        self.fields_frame.grid_columnconfigure(2, weight=1)
        for i in range(3):  # Assuming 3 rows for this method
            self.fields_frame.grid_rowconfigure(i, weight=1)

        # Ignore files fields
        ignore_files_label = tk.Label(self.fields_frame, text="Files to Ignore:")
        ignore_files_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)

        # Create the files_ignore_listbox widget before placing it
        self.files_ignore_listbox = tk.Listbox(self.fields_frame, height=4)
        self.files_ignore_listbox.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.files_ignore_listbox.bind("<Double-Button-1>", self.edit_file_ignore)

        add_file_folder_button = tk.Button(self.fields_frame, text="Add File/Folder", command=self.select_file_or_folder)
        add_file_folder_button.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

        for file_or_folder in self.current_config["workflows"]["clean_desktop_ignore_list"]:
            self.files_ignore_listbox.insert(tk.END, file_or_folder)

    def add_link(self):
        link = self.link_entry.get()
        if link:
            self.links_listbox.insert(tk.END, link)
            self.link_entry.delete(0, tk.END)

    def add_app(self):
        if platform.system() == "Darwin":  # macOS
            applications_path = "/Applications"
        elif platform.system() == "Windows":
            # Program Files or Program Files (x86)
            applications_path = "C:\\Program Files"
        else:
            # For Linux or other OS, default or handle differently
            applications_path = os.path.expanduser("~")
        app_path = filedialog.askopenfilename(title="Select App", initialdir=applications_path)
        
        if app_path and app_path not in self.apps_listbox.get(0, tk.END):
            self.apps_listbox.insert(tk.END, app_path)

    def sanitize_path(self, path, is_app):
        if not path:
            return ""
        
        item = path.split("/")[-1]

        if is_app:
            item = item.replace(".app", "")

        return item

    def add_app_kill(self):
        if platform.system() == "Darwin":
            applications_path = "/Applications"
        elif platform.system() == "Windows":
            applications_path = "C:\\Program Files"
        else:
            applications_path = os.path.expanduser("~")
        
        app_path = filedialog.askopenfilename(title="Select App to Kill", initialdir=applications_path)
        
        app_name = self.sanitize_path(app_path, True)
        
        if app_name and app_name not in self.apps_kill_listbox.get(0, tk.END):
            self.apps_kill_listbox.insert(tk.END, app_name)


    def select_file_or_folder(self):
        menu = tk.Menu(self.fields_frame, tearoff=0)
        menu.add_command(label="Select File", command=self.select_file)
        menu.add_command(label="Select Folder", command=self.select_folder)
        
        menu.post(self.fields_frame.winfo_pointerx(), self.fields_frame.winfo_pointery())

    def select_file(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = filedialog.askopenfilename(
            title="Select File to Ignore",
            initialdir=desktop_path
        )

        file = self.sanitize_path(file_path, False)

        if file_path and file not in self.files_ignore_listbox.get(0, tk.END):
            self.files_ignore_listbox.insert(tk.END, file)

    def select_folder(self):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        folder_path = filedialog.askdirectory(
            title="Select Folder to Ignore",
            initialdir=desktop_path
        )

        folder = self.sanitize_path(folder_path, False)

        if folder_path and folder not in self.files_ignore_listbox.get(0, tk.END):
            self.files_ignore_listbox.insert(tk.END, folder)

    def edit_link(self, event):
        selected_index = self.links_listbox.curselection()
        if not selected_index:
            return
        selected_link = self.links_listbox.get(selected_index)
        edit_dialog = EditDialog(self.fields_frame, "Edit Link", selected_link)

        if edit_dialog.delete_flag:
            self.links_listbox.delete(selected_index)
        elif edit_dialog.result_value and edit_dialog.result_value != selected_link:
            self.links_listbox.delete(selected_index)
            self.links_listbox.insert(selected_index, edit_dialog.result_value)

    def edit_app(self, event):
        selected_index = self.apps_listbox.curselection()
        if not selected_index:
            return
        selected_app = self.apps_listbox.get(selected_index)
        edit_dialog = EditDialog(self.fields_frame, "Edit App", selected_app)

        if edit_dialog.delete_flag:
            self.apps_listbox.delete(selected_index)
        elif edit_dialog.result_value and edit_dialog.result_value != selected_app:
            self.apps_listbox.delete(selected_index)
            self.apps_listbox.insert(selected_index, edit_dialog.result_value)

    def edit_app_kill(self, event):
        selected_index = self.apps_kill_listbox.curselection()
        if not selected_index:
            return
        selected_app = self.apps_kill_listbox.get(selected_index)
        edit_dialog = EditDialog(self.fields_frame, "Edit App to Quit", selected_app)
        
        if edit_dialog.delete_flag:
            self.apps_kill_listbox.delete(selected_index)
        elif edit_dialog.result_value and edit_dialog.result_value != selected_app:
            self.apps_kill_listbox.delete(selected_index)
            self.apps_kill_listbox.insert(selected_index, edit_dialog.result_value)

    def edit_file_ignore(self, event):
        selected_index = self.files_ignore_listbox.curselection()
        if not selected_index:
            return
        selected_app = self.files_ignore_listbox.get(selected_index)
        edit_dialog = EditDialog(self.fields_frame, "Edit file to ignore", selected_app)
        
        if edit_dialog.delete_flag:
            self.files_ignore_listbox.delete(selected_index)
        elif edit_dialog.result_value and edit_dialog.result_value != selected_app:
            self.files_ignore_listbox.delete(selected_index)
            self.files_ignore_listbox.insert(selected_index, edit_dialog.result_value)

    def save_config(self, selection):
        envs = self.current_config["environments"]
        names = [env["name"] for env in envs]
        names.append("Kill All")
        names.append("Clean Desktop")

        index = names.index(selection)

        if index < 4:
            # Read the data from UI fields
            name = self.name_entry.get()
            links = [self.links_listbox.get(i) for i in range(self.links_listbox.size())]
            apps = [self.apps_listbox.get(i) for i in range(self.apps_listbox.size())]
            spotify_play = bool(self.spotify_link_entry.get().strip())
            spotify_link = self.spotify_link_entry.get() if spotify_play else ""
            
            # Update the current_config dictionary
            self.current_config["environments"][index]["name"] = name
            self.current_config["environments"][index]["links"] = links
            self.current_config["environments"][index]["apps"] = apps

            spoticry = Spoticry()

            if spotify_play:
                self.current_config["environments"][index]["spotify_url"] = spotify_link
                play_data = spoticry.parse_link(spotify_link)
                self.current_config["environments"][index]["spotify_type"] = play_data[0]
                self.current_config["environments"][index]["spotify_id"] = play_data[1]
            else:
                self.current_config["environments"][index]["spotify_url"] = ""
                self.current_config["environments"][index]["spotify_type"] = ""
                self.current_config["environments"][index]["spotify_id"] = ""
            
        elif selection == "Kill All":
            # Read the data from UI fields
            apps_to_kill = [self.apps_kill_listbox.get(i) for i in range(self.apps_kill_listbox.size())]
            self.current_config["workflows"]["kill_all_apps"] = apps_to_kill
        
        elif selection == "Clean Desktop":
            # Read the data from UI fields
            files_to_ignore = [self.files_ignore_listbox.get(i) for i in range(self.files_ignore_listbox.size())]
            self.current_config["workflows"]["clean_desktop_ignore_list"] = files_to_ignore
        
        # Save the updated config using config_manager
        self.config_manager.write_config(self.current_config)
        if index < 4 and self.save_callback:
            new_name = self.name_entry.get()
            self.save_callback(new_name)
        invalidate_config_cache()
        tk.messagebox.showinfo("Saved", "Configuration saved successfully!")
