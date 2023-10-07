# BootMe
**Version 0.15.3**

BootMe is a personal productivity application that automates the setup of your work environment, allowing you to focus on what really matters. It handles opening up necessary apps, setting up your favorite music on Spotify, cleaning up your desktop, and more, all with a single command.

## Why I Created BootMe
Every time I power up my computer, I found myself caught in a pattern. Depending on my planned activity, I would systematically open a specific set of browser tabs and applications, all tailored to the task at hand. For instance:

- **Recruiting Mode**: On days focused on career opportunities, my ritual involved launching multiple tabs - job boards, LinkedIn for networking, and Notion to jot down my thoughts. To set the mood, a specific Spotify playlist echoed in the background.
  
- **Study Mode**: My study sessions had their unique digital environment, complete with educational websites, research tools, note-taking apps, and of course, a different Spotify playlist that helped me concentrate.

This repetitive task of setting up my digital workspace led me to ponder: _Why not automate this process?_ 

And thus, **BootMe** was born.

With BootMe, I introduced the concept of "environments." Instead of manually setting up my workspace, I could now activate a pre-defined 'study environment' or 'recruiting environment', and everything I needed would spring to life automatically. 

But I didn’t stop there. I realized there were other repetitive tasks I could optimize. BootMe now features workflows that allow me to:
- **Force Quit Unwanted Apps**: Ensuring that no unnecessary apps run in the background, saving me both CPU cycles and distractions.
- **Desktop Cleanup**: With a single click, I can declutter my desktop, ensuring a clean and focused workspace.

By automating these routines, I've made my computer more task-friendly, optimizing it for productivity and focus. If you find yourself ensnared in similar patterns, give BootMe a try and create your own personalized environments.


## Installation
1. Clone the repository to your local machine.
```
git clone https://github.com/demyinn00/BootMe.git
```
2. Install the required packages with 
```
pip install -r requirements.txt
```
3. Set up your Spotify API credentials as environment variables (see below).

## Spotify API Credentials
To use BootMe's music features, you'll need to set up your Spotify API credentials as environment variables. For more detailed instructions, please view [Spotify Setup Guide](/doc/Spotify_Setup.md).

### Quick start
1. Visit the Spotify Developer Dashboard and create a new app.
2. Get the Client ID and Client Secret from your new app's page.
3. Set these as environment variables:
```
export SPOTIPY_CLIENT_ID=
export SPOTIPY_CLIENT_SECRET=
export SPOTIPY_REDIRECT_URI=
```

## How to Use
- Run `python3 main.py` to start the app.
- Choose the environment you want to set up from the list.
- BootMe will take care of the rest.

## Code Structure
The main logic for BootMe is contained within `/scripts`. These file uses several helper functions to set up different parts of your environment, such as your music and your desktop. The entry point of this app is in `main.py`.

More information in [Code Structure](/doc/Code_Structure.md)

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