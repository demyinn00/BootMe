import os 
import webbrowser
import subprocess
import json
from tkinter import messagebox
from scripts.workflows import (kill_all_apps, clean_desktop)
from scripts.spoticry import Spoticry

def trigger_env(index):
  try: 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_dir,"..", "config.json")
    with open(config_file_path) as config_json:
      data = json.load(config_json)
      env = data["environments"][index]

      for link in env["links"]:
        webbrowser.open(link)
      
      for app in env["apps"]:
        subprocess.call(["open", app])
      
      if env['spotify_type'] != "none":
        spoticry = Spoticry()
        if env['spotify_type'] == 'album':
          spoticry.start_album(env['spotify_id'])
        else:
          spoticry.start_playlist(env['spotify_id'])

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