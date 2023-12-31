import os
import shutil
from scripts.backend.config_manager import ConfigManager

config_cache = None

def invalidate_config_cache():
    global config_cache
    config_cache = None

def get_config():
    global config_cache
    if config_cache is None:
        config_manager = ConfigManager()
        config_cache = config_manager.read_config()
    return config_cache

def kill_all_apps():
    config = get_config()
    for app in config["workflows"]["kill_all_apps"]:
        os.system(f"killall -9 '{app}'")

def clean_desktop():
    config = get_config()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    to_trash_path = os.path.join(desktop_path, "TRASH_ME")
    to_organize_path = os.path.join(desktop_path, "ORGANIZE_ME")
    ignore_list = config["workflows"]["clean_desktop_ignore_list"]

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
