import json
import os
from pathlib import Path

class ConfigManager:
  def __init__(self, config_filename="config.json"):
    script_dir = Path(__file__).resolve().parent.parent.parent
    # Append the config_filename to this path
    self.config_path = script_dir / config_filename
    self.config_exists()

  def config_exists(self):
    if not os.path.exists(self.config_path):
      self.create_default_config()

  def create_default_config(self):
    default_config = {
      "environments": [
        {
          "name": "Standard Enviornment",
          "links": [
            "https://google.com/"
          ],
          "apps": [],
          "spotify_url": "",
          "spotify_type": "",
          "spotify_id": ""
        },
        {
          "name": "Recruiting Environment",
          "links": [
            "https://www.indeed.com/jobs?l=Los+Angeles%2C+CA&mna=&=&aceid=&gclid=Cj0KCQjwoK2mBhDzARIsADGbjerBCq7yKXkuBzkVAoQAdrNS2UeV0rYpsdxzsaTcjoQ0GrQGUKzVgm4aAk3dEALw_wcB&gclsrc=aw.ds&from=mobRdr&utm_source=%2Fm%2F&utm_medium=redir&utm_campaign=dt",
            "https://www.linkedin.com/jobs/",
            "https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/"
          ],
          "apps": [],
          "spotify_url": "",
          "spotify_type": "",
          "spotify_id": ""
        },
        {
          "name": "Extra Environment 1",
          "links": [
            "https://www.google.com/"
          ],
          "apps": [],
          "spotify_url": "",
          "spotify_type": "",
          "spotify_id": ""
        },
        {
          "name": "Extra Environment 2",
          "links": [
            "https://www.google.com/"
          ],
          "apps": [],
          "spotify_url": "",
          "spotify_type": "",
          "spotify_id": ""
        }
      ],
      "workflows": {
        "kill_all_apps": [],
        "clean_desktop_ignore_list": [
          "TRASH_ME",
          "ORGANIZE_ME"
        ]
      }
    }
    self.write_config(default_config)

  def read_config(self):
    if not os.path.exists(self.config_path):
      return {}
    with open(self.config_path, "r") as f:
      return json.load(f)
    
  def write_config(self, data):
    with open(self.config_path, "w") as f:
      json.dump(data, f, indent=4)
