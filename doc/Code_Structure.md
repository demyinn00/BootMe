# BootMe Project Documentation

_Version: 2023-10-12_

## Table of Contents

- [BootMe Project Documentation](#bootme-project-documentation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Directory Structure](#directory-structure)
  - [Main Modules](#main-modules)
    - [main\_ui\_manager.py](#main_ui_managerpy)
    - [settings\_ui\_manager.py](#settings_ui_managerpy)
    - [trigger\_actions.py](#trigger_actionspy)
    - [config\_manager.py](#config_managerpy)
    - [spoticry.py](#spoticrypy)
    - [workflows.py](#workflowspy)
  - [Configuration](#configuration)

---

## Introduction

BootMe is a desktop application built to aid users in booting up their personal workspace environment. With a single click, users can open up predefined websites, applications, and more. 

---

## Directory Structure
```
BootME
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── config.json
├── doc
│   ├── Code_Structure.md
│   ├── Spotify_Setup.md
│   └── images
├── icons
├── main.py
├── requirements.txt
└── scripts
    ├── backend
    │   ├── config_manager.py
    │   ├── spoticry.py
    │   ├── trigger_actions.py
    │   └── workflows.py
    └── ui
        ├── edit_dialog.py
        ├── environment_field_manager.py
        ├── main_ui_manager.py
        └── settings_ui_manager.py
```

---

## Main Modules

### main_ui_manager.py

This module is responsible for managing and displaying the main user interface of the BootMe application.

- `MainUIManager`: Class responsible for creating and managing the main UI. It displays available environments as well as utility buttons such as "Kill All" and "Clean Desktop".

### settings_ui_manager.py

This module manages the user interface for settings and configurations. 

- `SettingsUIManager`: Class responsible for creating and displaying the settings UI. Allows users to modify and save environment configurations and other app settings.

### trigger_actions.py

This module is the main action handler for the application. It includes functions that are executed when certain buttons are pressed on the UI.

- `trigger_env(index)`: Opens up the predefined links and apps for a specific environment.
- `on_click_kill_all()`: Kills all the running applications.
- `on_click_clean_desktop()`: Cleans up the desktop.

### config_manager.py

Handles all operations related to the configuration file.

- `ConfigManager`: Class responsible for checking, reading, and writing to the `config.json` file.

### spoticry.py

Module for integrating with Spotify, allowing for the playback of specific albums or playlists as part of an environment.

- `Spoticry`: Class with methods to interact with Spotify's API, initiate playback of albums or playlists, and more.

### workflows.py

This module contains various workflow actions and utilities, including the logic for cleaning the desktop and killing applications.

- `get_config()`: Returns the configuration data. Utilizes caching to speed up repeated requests.

---

## Configuration

The configuration for the application is stored in a file named `config.json`. This file contains details about the various environments, links associated with each environment, and other settings.

