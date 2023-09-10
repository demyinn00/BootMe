# BootMe
**Version 0.11.1**

BootMe is a personal productivity application that automates the setup of your work environment, allowing you to focus on what really matters. It handles opening up necessary apps, setting up your favorite music on Spotify, cleaning up your desktop, and more, all with a single command.

## Installation
1. Clone the repository to your local machine.
2. Install the required packages with `pip install -r requirements.txt`
3. Set up your Spotify API credentials as environment variables (see below).

## Spotify API Credentials
To use BootMe's music features, you'll need to set up your Spotify API credentials as environment variables:

1. Visit the Spotify Developer Dashboard and create a new app.
2. Get the Client ID and Client Secret from your new app's page.
3. Set these as environment variables named SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET, respectively.

## How to Use
- Run `python3 main.py` to start the app.
- Choose the environment you want to set up from the list.
- BootMe will take care of the rest.

## Code Structure
The main logic for BootMe is contained within bootme.py. This file uses several helper functions to set up different parts of your environment, such as your music and your desktop.

The Spoticry class in spoticry.py is used to interact with the Spotify API.

## Platform Compatibility
BootMe was developed and tested on a Mac with an M1 chip. It's likely to work best on this platform. It may also work on other MacOS systems, and potentially on Linux with some modifications.

Unfortunately, we haven't been able to test BootMe on other platforms yet, so we can't guarantee that it will work everywhere. If you're trying to use BootMe on a different platform and running into issues, we'd appreciate hearing about your experiences.

## Known Issues
If Spotify has been inactive on for a period time, the Spotify API does not recognize an active device, and BootMe's music features will not work. 

## Future Plans
For version 1.0.0, we plan to:

- Add the ability to customize the list of apps and websites that are opened.
- Allow user configure workflow settings.

## Credits
BootMe is a project by David Mitchell Em-Yinn. It's free and open source, and you're welcome to modify it or use it for your own purposes. demyinn00.bootme@gmail.com

Gear and Help icons made by Freepik from http://www.flaticon.com/ <br>
Add icon made by dmitri13 from http://www.flaticon.com/