import tkinter as tk
from scripts.trigger_actions import (on_click_std_study_env, on_click_career_study_env, 
                                  on_click_cm_env, on_click_lext_env, on_click_kill_all, on_click_clean_desktop)

root = tk.Tk()
root.title("BootMe")
root.geometry('450x300')
root.configure(bg='#a9927d')

title_label = tk.Label(root, text="BootMe", font=("Helvetica", 24), bg='#a9927d', fg='#5c5241')
title_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

button_text = ["Standard Environment", "Recruiting Environment", "CM Environment", "LeXT Environment", "Kill All", "Clean Desktop"]
button_commands = [on_click_std_study_env, on_click_career_study_env, on_click_cm_env, on_click_lext_env, on_click_kill_all, on_click_clean_desktop]

for i in range(6):
  button = tk.Button(root, text=button_text[i], command=button_commands[i], width=20, height=2, bg='#cbb294', fg='#5c5241')
  button.grid(row=(i//2)+1, column=i%2, padx=20, pady=10, sticky="nsew", ipadx=10, ipady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

for i in range(4): 
  root.grid_rowconfigure(i, weight=1)

root.mainloop()
