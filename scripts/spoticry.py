import os
from dotenv import load_dotenv
from pathlib import Path
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spoticry:
  def __init__(self):
    base_dir = Path(__file__).resolve().parent.parent
    env_path = base_dir/".env"
    load_dotenv(dotenv_path=env_path) 

    client_id = os.getenv("SPOTIPY_CLIENT_ID")
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

    self.sp = spotipy.Spotify(auth=token_info["access_token"])
    self.play_data = tuple()
  
  def start_spotify(self, spotify_link):
    self.parse_link()

    if self.play_data[0] == "playlist":
      self.start_playlist(self.play_data(1))
    elif self.play_data[0] == "album":
      self.start_album(self.play_data(1))

  def parse_link(self, spotify_link):
    parsed_link = spotify_link.split("/")
    id = parsed_link[4].split("?")[0]

    self.play_data = (parsed_link[3], id)


  def start_playlist(self, playlist_uri):
    self.sp.start_playback(context_uri=playlist_uri)


  def start_album(self, album_id: str):
    results = self.sp.album_tracks(album_id)
    track_uids = [track["uri"] for track in results["items"]]
    self.sp.start_playback(uris=track_uids)