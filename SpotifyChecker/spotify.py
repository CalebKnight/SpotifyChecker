from tabnanny import check
import requests
import os
from dotenv import load_dotenv
from track import Track
from tracks import Tracks
from file import File
load_dotenv()


ClientId = os.getenv('SPOTIFY_CLIENT_ID')
ClientSecret = os.getenv('SPOTIFY_CLIENT_SECRET')

def main():
    createNewFile = input("Create new file? (y/n): ")
    spotifyAccessToken = getAccessToken()
    playlistId = "1I3op6do4myH4RouoJFn0s"
    file = File("SpotifyChecker/tracks.csv")
    try:
        file.read()
    except FileNotFoundError:
        file.write([])
        file.read()
    if(len(file.fileContent) == 0 or createNewFile == "y"):
        tracks = Tracks()
        tracks.genTracks(playlistId, spotifyAccessToken)
        file.write(tracks.tracks)
        file.read()
    tracks = file.fileContent
    
    # for track in tracks:
    #     print(track.name)
    for idx,track in enumerate(tracks):
        for idx2,track2 in enumerate(tracks):
            if(track.id != track2.id ):
                if track.nameIsSimilar(track2):
                    print(track.toString() + "\nis similar to\n" + track2.toString() + "\n")
                   
def getAccessToken():
    response = requests.post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'client_credentials',
        'client_id': ClientId,
        'client_secret': ClientSecret
    })
    return response.json()['access_token']




if __name__ == '__main__':
    main()