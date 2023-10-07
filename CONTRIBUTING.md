# Contributing to BootMe

First off, thank you for considering contributing to BootMe. It's people like you that make BootMe such a great tool.

## Table of Contents

- [Contributing to BootMe](#contributing-to-bootme)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [How Can I Contribute?](#how-can-i-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Enhancements](#suggesting-enhancements)
    - [Pull Requests](#pull-requests)
  - [Development Setup](#development-setup)
  - [Style Guidelines](#style-guidelines)
    - [Git Commit Messages](#git-commit-messages)
    - [Code Style](#code-style)

## Code of Conduct

We've adopted a Code of Conduct that we expect project participants to adhere to. Please read [the full text](CODE_OF_CONDUCT.md) so that you can understand what actions will and will not be tolerated.

## How Can I Contribute?

### Reporting Bugs

- Check if the bug is already reported in the [issues](https://github.com/demyinn00/BootMe/issues).
- If it's not, [open a new issue](https://github.com/demyinn00/BootMe/issues/new). Provide a detailed description of the problem, steps to reproduce, expected behavior, and any related information.
- Attach screenshots or screen recordings if they help illustrate the issue.

### Suggesting Enhancements

- Check the issues list to see if it's already been mentioned.
- Provide a clear and detailed explanation of the feature you want and why it's important to add.
- Discuss the pros and cons.

### Pull Requests

- Fork the repository and create your branch from the current active branch (usually `main` or `master`).
- If you've added code that should be tested, add tests.
- Ensure the test suite passes.
- Make sure your code lints and adheres to the project's style guidelines.
- Issue that pull request!

## Development Setup

Provide steps on how to set up the development environment. For example:

1. Set up Spotify keys. Read [spotify setup](/doc/Spotify_Setup.md) for details. 
  - **Quick start**:
    1. Create Spotify account if you do not have one. 
    2. Go to [Spotify for Developer](https://developer.spotify.com/) and log in with your credentials
    3. Create a new app
    4. Go to settings and store the following in a `.env` file located in `/BootMe/.env`
    ```
    export SPOTIPY_CLIENT_ID=
    export SPOTIPY_CLIENT_SECRET=
    export SPOTIPY_REDIRECT_URI= 
    ```
2. Clone the repository.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run `python3 main.py`.

## Style Guidelines

### Git Commit Messages
- Follow the Conventional Commits format: `type<scope>: description`.
  - Type: feat, fix, chore, docs, style, refactor, perf, test.
  - Scope (optional): Part of the codebase, e.g. ui, backend, settings, etc.
  - Description: Concise explanation of the change.
- Limit the first line to 72 characters or less.
- Reference issues and pull requests liberally after the first line.

### Code Style

- This is a Python project, so follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).

