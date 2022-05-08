import requests
from track import Track
class Tracks:
    def __init__(self):
        self.tracks = []
    # Because of how the spotify API works, we need to make multiple requests to get all the tracks
    # This is because the limit is 50 tracks per request
    # This function will return a list of tracks
    def getTracks(self, playlistId, spotifyAccessToken, offset, limit):
        response = requests.get('https://api.spotify.com/v1/playlists/{}/tracks'.format(playlistId), headers={ 'Authorization': 'Bearer ' + spotifyAccessToken, 'Content-Type': 'application/json' }, params={'limit': '{}'.format(limit), 'offset': '{}'.format(offset)})
        listOfTracks = []
        tracks = response.json()['items']
        # Current implementation of artist similarity may need work as it only stores the first artist which could be problematic if spotify chooses to change the order of the artists
        for track in tracks:
            track = Track(track['track']['name'], track['track']['id'], track['track']['artists'][0]['name'], track['track']['album']['name'])
            listOfTracks.append(track)
        return listOfTracks

    def genTracks(self, playlistId, spotifyAccessToken):
        response = requests.get('https://api.spotify.com/v1/playlists/{}'.format(playlistId), headers={ 'Authorization': 'Bearer ' + spotifyAccessToken, 'Content-Type': 'application/json' })
        totalSongs = response.json()['tracks']['total']
        print("Playlist {} has {} songs".format(response.json()['name'], totalSongs))
        for i in range(0, totalSongs, 50):
            # Adds songs to the list
            self.tracks += self.getTracks(playlistId, spotifyAccessToken, i, 50)
        return self.tracks

