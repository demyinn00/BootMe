import tkinter as tk
from scripts.backend.trigger_actions import (
    trigger_env, on_click_kill_all, on_click_clean_desktop
)

class MainUIManager:
    def __init__(self, root_frame, config_manager, open_settings_cb, open_help_cb):
        self.root_frame = root_frame
        self.config_manager = config_manager
        self.create_title_and_buttons(open_settings_cb, open_help_cb)
        self.create_buttons()

    def create_title_and_buttons(self, open_settings_cb, open_help_cb):
        self.title_label = tk.Label(
            self.root_frame, text="BootMe", font=("Helvetica", 24),
            bg="#a9927d", fg="#5c5241"
        )
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        self.button_frame = tk.Frame(self.root_frame, bg="#a9927d")
        self.button_frame.grid(row=0, column=1, sticky="ne", pady=(20, 0))
        self.settings_button = tk.Button(
            self.button_frame,
            text="Settings",
            command=open_settings_cb
        )

        self.settings_button.grid(row=0, column=0, sticky="w")
        self.help_button = tk.Button(
            self.button_frame,
            text="Help",
            command=open_help_cb
        )

        self.help_button.grid(row=0, column=1, sticky="e", padx=(5, 0))

    def create_buttons(self):
        data = self.config_manager.read_config()
        button_text = (
            [env["name"] for env in data["environments"]]
            + ["Kill All", "Clean Desktop"]
        )
        button_commands = [
            lambda i=i: trigger_env(i) for i in range(len(data["environments"]))
        ]
        button_commands.extend([on_click_kill_all, on_click_clean_desktop])

        for i in range(6):
            button = tk.Button(
                self.root_frame,
                text=button_text[i],
                command=button_commands[i],
                width=20, height=2,
                bg="#cbb294",
                fg="#5c5241"
            )
            button.grid(
                row=(i//2)+1, column=i%2, padx=20, pady=(20, 10),
                sticky="nsew", ipadx=10, ipady=10
            )

    def refresh_buttons(self):
        for widget in self.root_frame.winfo_children():
            if widget not in (self.title_label, self.button_frame):
                widget.destroy()

        self.create_buttons()
