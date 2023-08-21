import tkinter as tk
from scripts.trigger_actions import (trigger_env, on_click_kill_all, on_click_clean_desktop)

class MainUIManager:
  def __init__(self, master, config_manager):
    self.master = master
    self.config_manager = config_manager
    self.create_buttons()

  def create_buttons(self):
    data = self.config_manager.read_config()
    button_text = [env["name"] for env in data["environments"]] + ["Kill All", "Clean Desktop"]
    button_commands = [lambda i=i: trigger_env(i) for i in range(len(data["environments"]))] + [on_click_kill_all, on_click_clean_desktop]

    for i in range(6):
      button = tk.Button(self.master, text=button_text[i], command=button_commands[i], width=20, height=2, bg="#cbb294", fg="#5c5241")
      button.grid(row=(i//2)+1, column=i%2, padx=20, pady=10, sticky="nsew", ipadx=10, ipady=10)