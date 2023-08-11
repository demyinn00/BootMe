import os
import shutil
import json


def load_config():
  # Get absolute path of current script
  current_script_path = os.path.abspath(__file__)

  # Get the directory containing the current script
  current_directory = os.path.dirname(current_script_path)

  # Form the path to config.json
  config_path = os.path.join(current_directory, '..', 'config.json')
  print(f"Workflows: {config_path}")

  with open(config_path, 'r') as file:
    return json.load(file)

CONFIG = load_config()

def kill_all_apps():
  for app in CONFIG["workflows"]["kill_all_apps"]:
    os.system(f"killall -9 '{app}'")


def clean_desktop():
  desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
  to_trash_path = os.path.join(desktop_path, "TRASH_ME")
  to_organize_path = os.path.join(desktop_path, "ORGANIZE_ME")
  ignore_list = CONFIG["workflows"]["clean_desktop_ignore_list"]

  if not os.path.exists(to_trash_path):
    os.mkdir(to_trash_path)
  if not os.path.exists(to_organize_path):
    os.mkdir(to_organize_path)

  for file in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file)
    if file in ignore_list:
      continue

    destination_path = to_organize_path if file.startswith("keep_") else to_trash_path

    if os.path.exists(os.path.join(destination_path, file)):
      print(f"File {file} already exists in destination {destination_path}. Skipping...")
      continue

    try:
      if file.startswith("keep_"):
          shutil.move(file_path, to_organize_path)
      else:
          shutil.move(file_path, to_trash_path)
    except Exception as e:
        print(f"Error moving {file_path}: {e}")

  if not os.listdir(to_organize_path):
    shutil.rmtree(to_organize_path)