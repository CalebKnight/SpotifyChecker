import requests
from track import Track
class Tracks:
    def __init__(self):
        self.tracks = []

    def __str__(self):
        return self.tracks
    
    def getTracks(self, playlistId, spotifyAccessToken, offset, limit):
        response = requests.get('https://api.spotify.com/v1/playlists/{}/tracks'.format(playlistId), headers={ 'Authorization': 'Bearer ' + spotifyAccessToken, 'Content-Type': 'application/json' }, params={'limit': '{}'.format(limit), 'offset': '{}'.format(offset)})
        listOfTracks = []
        tracks = response.json()['items']
        for track in tracks:
            track = Track(track['track']['name'], track['track']['id'], track['track']['artists'][0]['name'], track['track']['album']['name'])
            listOfTracks.append(track)
        return listOfTracks

    def genTracks(self, playlistId, spotifyAccessToken):
        response = requests.get('https://api.spotify.com/v1/playlists/{}'.format(playlistId), headers={ 'Authorization': 'Bearer ' + spotifyAccessToken, 'Content-Type': 'application/json' })
        totalSongs = response.json()['tracks']['total']
        print(totalSongs)
        # print(response.json())
        for i in range(0, totalSongs, 50):
            self.tracks += self.getTracks(playlistId, spotifyAccessToken, i, 50)
        return self.tracks

