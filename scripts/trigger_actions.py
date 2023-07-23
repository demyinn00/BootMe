from tkinter import messagebox
from scripts.workflows import (std_study_env, career_study_env, cm_env, 
                              lext_env, kill_all_apps, clean_desktop)

def on_click_std_study_env():
  try:
    std_study_env()
    print("Study Environment Set")
  except Exception as e:
    messagebox.showerror("Error", str(e))

def on_click_career_study_env():
  try: 
    career_study_env()
    print("Career Environment Set")
  except Exception as e: 
    messagebox.showerror("Error", str(e))

def on_click_cm_env():
  try: 
    cm_env()
    print("CM Environment Set")
  except Exception as e: 
    messagebox.showerror("Error", str(e))

def on_click_lext_env():
  try:
    lext_env()
    print("LeXT Environment Set")
  except Exception as e:
    messagebox.showerror("Error", str(e))

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