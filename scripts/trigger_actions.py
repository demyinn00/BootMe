from tkinter import messagebox
from scripts.workflows import (std_study_env, career_study_env, cm_env, 
                              lext_env, kill_all_apps, clean_desktop)

def on_click_std_study_env():
  try:
    std_study_env()
    messagebox.showinfo("Success", "Study Environment Set")
  except Exception as e:
    messagebox.showerror("Error", str(e))

def on_click_career_study_env():
  try: 
    career_study_env()
    messagebox.showinfo("Success", "Career Environment Set")
  except Exception as e: 
    messagebox.showerror("Error", str(e))

def on_click_cm_env():
  try: 
    cm_env()
    messagebox.showinfo("Success", "CM Environment Set")
  except Exception as e: 
    messagebox.showerror("Error", str(e))

def on_click_lext_env():
  try:
    lext_env()
    messagebox.showinfo("Success", "LeXT Environment Set")
  except Exception as e:
    messagebox.showerror("Error", str(e))

def on_click_kill_all():
  try: 
    kill_all_apps()
    messagebox.showinfo("Success", "Force quit all apps")
  except Exception as e: 
    messagebox.showerror("Error", str(e))

def on_click_clean_desktop():
  try: 
    clean_desktop()
    messagebox.showinfo("Success", "Desktop cleaned")
  except Exception as e: 
    messagebox.showerror("Error", str(e))