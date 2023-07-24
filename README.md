# BootMe
This app allows me to run 6 workflows. The work flows configured have 2 main uses: 
- Launching study/work environments
  - Launch my most used tabs 
  - Play appropriate Spotify playlist  
- Orangization
  - Clean my desktop (remove clutter)
  - Kill all (Force quit background apps)

Before using this app, create a `.env` file to store your Spotify credentials. Click here for more info on spotify web api. https://developer.spotify.com/documentation/web-api

<br>

```
export SPOTIPY_CLIENT_ID= # from spotify web api
export SPOTIPY_CLIENT_SECRET= # from spotify web api
export SPOTIPY_REDIRECT_URI= # from spotify web api

# Configure these links as need be. Update the code to use links you desire.
export CAREER_LINK_1=
export CAREER_LINK_2=
export CAREER_LINK_3=
export CAREER_LINK_4=

export CM_LINK_1=
export CM_LINK_2=

export LEXT_LINK_1=
export LEXT_LINK_2=
```


To run app do: <br>
`python3 /path/to/BootMe/main.py`