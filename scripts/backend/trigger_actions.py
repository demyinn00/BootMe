import webbrowser
import subprocess
from tkinter import messagebox
from scripts.backend.workflows import (kill_all_apps, clean_desktop, get_config)
from scripts.backend.spoticry import Spoticry

import pdb

def trigger_env(index):
    try: 
        data = get_config()
        env = data["environments"][index]

        for link in env["links"]:
            webbrowser.open(link)
        
        for app in env["apps"]:
            subprocess.call(["open", app])
        
        # pdb.set_trace()

        if env["spotify_url"] != "":
            spoticry = Spoticry()

        if env["spotify_type"] == "album":
            spoticry.start_album(env["spotify_id"])
        else:
            spoticry.start_playlist(env["spotify_id"])

        print(f"{env['name']} Set")
    except Exception as err:
        messagebox.showerror("Error", str(err))

def on_click_kill_all():
    try: 
        kill_all_apps()
        print("Force quit all apps")
    except Exception as e: 
        messagebox.showerror("Error", str(e))

def on_click_clean_desktop():
    try: 
        clean_desktop()
        print("Desktop cleaned")
    except Exception as e: 
        messagebox.showerror("Error", str(e))
