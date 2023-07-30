import os
import shutil
import webbrowser
from scripts.spoticry import Spoticry

def open_tabs(url_list):
  for url in url_list:
    os.system(f"open -a 'Google Chrome' {url}")

def std_study_env():
  spoticry = Spoticry()

  play_type = 'album' # 'playlist
  if play_type == 'album':
    spoticry.start_album("18NOKLkZETa4sWwLMIm0UZ")
  else:
    playlist_uri = "spotify:playlist:0b3Zb3pUyHwN5KJnEfPQXm"
    spoticry.start_playlist(playlist_uri)

  url_list = ["https://chat.openai.com/"]
  open_tabs(url_list)


def career_study_env():
  spoticry = Spoticry()
  
  play_type = 'album' # 'playlist
  if play_type == 'album':
    spoticry.start_album("18NOKLkZETa4sWwLMIm0UZ")
  else:
    playlist_uri = "spotify:playlist:18NOKLkZETa4sWwLMIm0UZ"
    spoticry.start_playlist(playlist_uri)

  url_list = [
    os.getenv("CAREER_LINK_1"),
    os.getenv("CAREER_LINK_2"),
    os.getenv("CAREER_LINK_3"),
    os.getenv("CAREER_LINK_4"),
    os.getenv("CAREER_LINK_5")
  ]

  os.system("open /Applications/Notion.app")
  open_tabs(url_list)

def cm_env():
  url_list = [
    os.getenv("CM_LINK_1"),
    os.getenv("CM_LINK_2"),
  ]

  open_tabs(url_list)
  os.system("open /Applications/zoom.us.app")


def lext_env():
  playlist_uri = "spotify:playlist:7JNI9JploGRjNmXYp4nmlC"
  spoticry = Spoticry()
  spoticry.start_playlist(playlist_uri)

  url_list = [
    os.getenv("LEXT_LINK_1"),
    os.getenv("LEXT_LINK_2"),
  ]

  open_tabs(url_list)

def kill_all_apps():
  os.system("killall -9 'Google Chrome'")
  os.system("killall -9 'Day One'")
  os.system("killall -9 'Notes'")
  os.system("killall -9 'Notion'")
  os.system("killall -9 'TextEdit'")
  os.system("killall -9 'zoom.us'")
  os.system("killall -9 'Messages'")
  os.system("killall -9 'Mail'")


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