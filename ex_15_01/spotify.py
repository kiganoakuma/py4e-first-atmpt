import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your Spotify API credentials
client_id = 'f825a04b660244b2ae7805070803d52c'
client_secret = '8945556236e745399a5e033fb93cb9a9'
redirect_uri = 'http://localhost:8000/callback'

scope = 'user-read-recently-played'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Define the song you want to track
song_name = 'Debold'
artist_name = 'Vegyn'

# Get the user's recently played tracks
recently_played = sp.current_user_recently_played(limit=999999)

# Track the play count for the specific song
play_count = 0
for item in recently_played['items']:
    track = item['track']
    if track['name'] == song_name and any(artist['name'] == artist_name for artist in track['artists']):
        play_count += 1

# Print the play count for the song
print(f"The song '{song_name}' by '{artist_name}' has been played {play_count} times.")