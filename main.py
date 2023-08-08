import os
import json
import tkinter as tk
from windows.settings_window import SettingsWindow
from scripts.trigger_actions import (trigger_env, on_click_kill_all, on_click_clean_desktop)

def open_settings():
  settings = SettingsWindow(root)

root = tk.Tk()
root.title("BootMe")
root.geometry('450x300')
root.configure(bg='#a9927d')

title_label = tk.Label(root, text="BootMe", font=("Helvetica", 24), bg='#a9927d', fg='#5c5241')
title_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

edit_button = tk.Button(root, text="Edit", command=open_settings)
edit_button.grid(row=0, column=2, sticky="nsew")

config_file_path = "config.json"

if not os.path.exists(config_file_path):
  default_config = {
    "environments": [
      {
        "name": "Standard Enviornment",
        "links": [
          "https://google.com/"
        ],
        "apps": [],
        "spotify_type": "album",
        "spotify_id": "18NOKLkZETa4sWwLMIm0UZ"
      },
      {
        "name": "Recruiting Environment",
        "links": [
          "https://www.indeed.com/jobs?l=Los+Angeles%2C+CA&mna=&=&aceid=&gclid=Cj0KCQjwoK2mBhDzARIsADGbjerBCq7yKXkuBzkVAoQAdrNS2UeV0rYpsdxzsaTcjoQ0GrQGUKzVgm4aAk3dEALw_wcB&gclsrc=aw.ds&from=mobRdr&utm_source=%2Fm%2F&utm_medium=redir&utm_campaign=dt",
          "https://www.linkedin.com/jobs/",
          "https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/"
        ],
        "apps":[],
        "spotify_type": "album",
        "spotify_id": "18NOKLkZETa4sWwLMIm0UZ"
      },
      {
        "name": "Extra Environment 1",
        "links": [
          "https://www.google.com/"
        ],
        "apps":[],
        "spotify_type": "none",
        "spotify_id": "none"
      },
      {
        "name": "Extra Environment 2",
        "links": [
          "https://www.google.com/"
        ],
        "apps":[],
        "spotify_type": "playlist",
        "spotify_id": "spotify:playlist:5sXRm52jnGFLluxfgeZ1Ng"
      }
    ]
  }
  with open(config_file_path, 'w') as output_file: 
    json.dump(default_config, output_file)

with open(config_file_path) as config_json:
  data = json.load(config_json)
  button_text = [env['name'] for env in data['environments']] + ["Kill All", "Clean Desktop"]

button_commands = [lambda i=i: trigger_env(i) for i in range(len(data['environments']))] + [on_click_kill_all, on_click_clean_desktop]

for i in range(6):
  button = tk.Button(root, text=button_text[i], command=button_commands[i], width=20, height=2, bg='#cbb294', fg='#5c5241')
  button.grid(row=(i//2)+1, column=i%2, padx=20, pady=10, sticky="nsew", ipadx=10, ipady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

for i in range(4): 
  root.grid_rowconfigure(i, weight=1)

root.mainloop()
