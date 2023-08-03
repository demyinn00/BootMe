import os
import shutil

def kill_all_apps():
  os.system("killall -9 'Google Chrome'")
  os.system("killall -9 'Day One'")
  os.system("killall -9 'Notes'")
  os.system("killall -9 'Notion'")
  os.system("killall -9 'TextEdit'")
  os.system("killall -9 'zoom.us'")
  os.system("killall -9 'Messages'")
  os.system("killall -9 'Mail'")
  os.system("killall -9 'Figma'")


def clean_desktop():
  desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
  to_trash_path = os.path.join(desktop_path, "TRASH_ME")
  to_organize_path = os.path.join(desktop_path, "ORGANIZE_ME")
  ignore_list = ["CM", "LeXT", "repos", "TM", "TRASH_ME", "ORGANIZE_ME"]

  if not os.path.exists(to_trash_path):
    os.mkdir(to_trash_path)
  if not os.path.exists(to_organize_path):
    os.mkdir(to_organize_path)

  for file in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, file)
    if file in ignore_list:
      continue
    try:
      if file.startswith("keep_"):
          shutil.move(file_path, to_organize_path)
      else:
          shutil.move(file_path, to_trash_path)
    except Exception as e:
        print(f"Error moving {file_path}: {e}")

  if not os.listdir(to_organize_path):
    shutil.move(to_organize_path, to_trash_path)