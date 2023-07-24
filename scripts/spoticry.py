import os
from dotenv import load_dotenv
from pathlib import Path
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spoticry:
  def __init__(self):
    base_dir = Path(__file__).resolve().parent.parent
    env_path = base_dir/'.env'
    load_dotenv(dotenv_path=env_path) 

    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

    # The scope of the permissions
    scope = "user-modify-playback-state"

    cache_path = base_dir / ".cache"

    sp_oauth = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri=redirect_uri,
                            scope=scope,
                            cache_path=str(cache_path))

    token_info = sp_oauth.get_cached_token()

    if not token_info or sp_oauth.is_token_expired(token_info):
      print("No valid token found. Getting new token.")
      token_info = sp_oauth.get_access_token()
    else:
      print("Valid token found in cache.")

    self.sp = spotipy.Spotify(auth=token_info['access_token'])
  
  def start_playlist(self, playlist_uri):
    self.sp.start_playback(context_uri=playlist_uri)

