import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spoticry:
  def __init__(self):
    load_dotenv() 
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

    # The scope of the permissions
    scope = "user-modify-playback-state"

    sp_oauth = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri=redirect_uri,
                            scope=scope)
    
    # Only works if already logged in on machine
    token_info = sp_oauth.get_cached_token()
    
    self.sp = spotipy.Spotify(auth=token_info["access_token"])
  
  def start_playlist(self, playlist_uri):
    self.sp.start_playback(context_uri=playlist_uri)