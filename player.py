import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import math

########### PRIVATE API KEYS ###########
CLIENT_ID = '551eb27f342745eeb6e09c418b7bf172'
CLIENT_SECRET = '9ee7f517915d434fbe85cbf0f7f88ec8'
REDIRECT_URI = 'http://localhost:8888/callback'
########################################


########### USER DEFINED CONSTATNS ##########
CONSTANT = 5
TOTAL_LENGTH = CONSTANT + 20

ALBUMS = {
    'oncle jazz': '4W4gNYa4tt3t8V6FmONWEK',
    'flower boy': '2nkto6YNI4rUYTLqEwWJ3o',
    'dark side': '4LH4d3cOWNNsVw41Gqt2kv',
    'over': '7d9yPFvTj1LCdqK0iMlLtx'
}

slots = {2 * x:x for x in range(1, 11)}
########################################


scope = "user-read-playback-state,user-modify-playback-state"


client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope))


def slot_to_track(slot: int, album: str) -> int:
    """"Returns intended track based on the slot."""
    amount_of_tracks = len(get_tracks_uri(album))
    total_slots = 10
    return math.floor(slot / total_slots * amount_of_tracks)


def get_tracks_uri(album: str) -> list:
    """Returns a list containing the album's tracks' uri"""
    uris = []
    for item in sp.album_tracks(ALBUMS[album])['items']:
        uris.append(item['uri'])
    return uris


def play_track(track_uris: list) -> None:
    """Plays track from uri"""
    sp.start_playback(uris=track_uris)

def start_pause() -> None:
    """Starts/pause track"""
    if sp.current_playback()['is_playing']:
        sp.pause_playback()
    else:
        sp.start_playback()


def distance_to_track(distance: float, album: str) -> None:
    """
    Input:
        - distance of the card from sensor
        - current album selected
    Output:
        - track number
    """
    # 1. distance to slot
    slot = distance / TOTAL_LENGTH
    
    # 2. slot to track of album
    tracks = slot_to_track(slot, album)
    
    # 3. play track


def volume_change(percentage: int) -> None:
    """Decreases the volume according to percentage"""
    current_volume = sp.current_playback()['device']['volume_percent']
    updated_volume = current_volume + percentage

    if updated_volume < 100 and updated_volume > 0:
        sp.volume(updated_volume)
    elif updated_volume > 100:
        sp.volume(100)
    elif updated_volume < 0:
        sp.volume(0)
        