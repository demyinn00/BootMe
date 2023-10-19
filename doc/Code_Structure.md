# BootMe Project Documentation

_Version: 2023-10-12_

## Table of Contents

- [BootMe Project Documentation](#bootme-project-documentation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Directory Structure](#directory-structure)
  - [Main Modules](#main-modules)
    - [main.py](#mainpy)
    - [config\_manager.py](#config_managerpy)
    - [spoticry.py](#spoticrypy)
    - [trigger\_actions.py](#trigger_actionspy)
    - [workflows.py](#workflowspy)
    - [edit\_dialog.py](#edit_dialogpy)
    - [environment\_field\_manager.py](#environment_field_managerpy)
    - [help\_ui\_manager.py](#help_ui_managerpy)
    - [main\_ui\_manager.py](#main_ui_managerpy)
    - [settings\_ui\_manager.py](#settings_ui_managerpy)
  - [Configuration](#configuration)

---

## Introduction

BootMe is a desktop application built to aid users in booting up their personal workspace environment. With a single click, users can open up predefined websites, applications, and more. 

---

## Directory Structure
```
BootMe
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── config.json
├── doc
│   ├── Code_Structure.md
│   ├── Spotify_Setup.md
│   ├── help.md
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
        ├── help_ui_manager.py
        ├── main_ui_manager.py
        └── settings_ui_manager.py
```

---

## Main Modules

### main.py

This is the main entry point of the application. It initializes the application and sets up the necessary configurations.

### config_manager.py

Manages the configuration settings of the application, ensuring that user preferences are saved and loaded correctly.

### spoticry.py

Handles Spotify integration, allowing the application to interact with Spotify and manage playlists.

### trigger_actions.py

Defines the actions that can be triggered by the user, such as playing a song or adjusting volume.

### workflows.py

Manages the workflows of the application, ensuring that tasks are executed in the correct order.

### edit_dialog.py

Provides the UI for editing configurations, allowing users to customize their experience.

### environment_field_manager.py

Manages the environment fields in the UI, ensuring that the correct data is displayed.

### help_ui_manager.py

Manages the help section of the UI, providing users with guidance on how to use the application.

### main_ui_manager.py

Manages the main user interface of the application, ensuring a smooth user experience.

### settings_ui_manager.py

Manages the settings section of the UI, allowing users to adjust their preferences.

---

## Configuration

The configuration for the application is stored in a file named `config.json`. This file contains details about the various environments, links associated with each environment, and other settings. `config.json` can be thought of as the settings file.
