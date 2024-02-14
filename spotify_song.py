from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#date=input("Please Enter date in YYYY-MM- Format")

response=requests.get("https://www.billboard.com/charts/hot-100/2023-08-05/")

soup=BeautifulSoup(response.text,"html.parser")
all_titles= soup.select(selector=".o-chart-results-list__item #title-of-a-story")

client_id="05d82555b91a4325b5e1e5563e4b0faa"
client_secret="5c3d0bc4a04d47b38935ee977742c379"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri='https://example.com',
                                               scope='playlist-modify-private'))

user_profile = sp.current_user()

# Extract user ID from the profile
user_id = user_profile['id']
print(user_id)

playlist_name = 'Top 100 Songs'
playlist_description = 'Your Playlist Description'
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)


for titles in all_titles:
    print(titles.getText().strip())
    # Search for the song
    song_title = titles.getText().strip()
    search_results = sp.search(q=song_title, type='track')

    # Extract the track URI
    track_uri = search_results['tracks']['items'][0]['uri']  # Assuming the first search result is the desired song
    playlist_id = playlist['id']
    sp.playlist_add_items(playlist_id=playlist_id, items=[track_uri])

