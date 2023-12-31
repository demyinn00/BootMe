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
                    "spotify_id": "",
                    "spotify_display_name": ""
                },
                {
                    "name": "Recruiting Environment",
                    "links": [
                        "https://www.indeed.com/",
                        "https://www.linkedin.com/jobs/",
                        "https://leetcode.com/"
                    ],
                    "apps": [],
                    "spotify_url": "",
                    "spotify_type": "",
                    "spotify_id": "",
                    "spotify_display_name": ""
                },
                {
                    "name": "Extra Environment 1",
                    "links": [
                        "https://www.google.com/"
                    ],
                    "apps": [],
                    "spotify_url": "",
                    "spotify_type": "",
                    "spotify_id": "",
                    "spotify_display_name": ""
                },
                {
                    "name": "Extra Environment 2",
                    "links": [
                        "https://www.google.com/"
                    ],
                    "apps": [],
                    "spotify_url": "",
                    "spotify_type": "",
                    "spotify_id": "",
                    "spotify_display_name": ""
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

    def get_all_names(self):
        config_data = self.read_config()
        return [env["name"] for env in config_data.get("environments", [])]
    
    def get_display_name(self, environment_name):
        config_data = self.read_config()
        for env in config_data.get("environments", []):
            if env["name"] == environment_name:
                return env.get("display_name", "")
        return ""

    def read_config(self):
        if not os.path.exists(self.config_path):
            return {}
        with open(self.config_path, "r") as f:
            return json.load(f)

    def write_config(self, data):
        with open(self.config_path, "w") as f:
            json.dump(data, f, indent=4)
