import json
import pandas as pd
import requests
from secrets import access_token, user_id

class CreatePlaylist:

    def __init__(self):
        self.user_id = user_id
        self.access_token = access_token
        self.csv = '/Users/kellylam/optimal_playlist.csv'


    def create_playlist(self):
        request_body = json.dumps({
            'name': 'Optimal Playlist',
            'description': 'Python script that converts CSV file of reordered songs of "Top Songs 2020" into a Spotify playlist. Songs have been reordered by energy, tempo, valence, loudness, danceability',
            'public': True
        })
        query = 'https://api.spotify.com/v1/users/{}/playlists'.format(self.user_id)
        response = requests.post(
            query,
            data = request_body,
            headers = {
                'Content-Type':'application/json',
                'Authorization':'Bearer {}'.format(self.access_token)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json['id']


    def add_to_playlist(self):
        df = pd.read_csv(self.csv)
        
        # Create new playlist
        playlist_id = self.create_playlist()

        # Populate playlist
        request_data = json.dumps(df.uri.tolist())
        query = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(playlist_id)
        response = requests.post(
            query,
            data = request_data,
            headers = {
                'Content-Type':'application/json',
                'Authorization':'Bearer {}'.format(self.access_token)
            }
        )
        response_json = response.json()
        return response_json


if __name__ == '__main__':
    cp = CreatePlaylist()
    cp.add_to_playlist()