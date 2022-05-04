import requests
import os
from dotenv import load_dotenv
load_dotenv()


ClientId = os.getenv('SPOTIFY_CLIENT_ID')
ClientSecret = os.getenv('SPOTIFY_CLIENT_SECRET')

def main():

    spotifyAccessToken = getAccessToken()
    playlistId = "1I3op6do4myH4RouoJFn0s"
    response = requests.get('https://api.spotify.com/v1/playlists/{}'.format(playlistId), headers={ 'Authorization': 'Bearer ' + spotifyAccessToken, 'Content-Type': 'application/json' })
    # print(response.json())
    tracks = getTracks(response)
    for idx,track in enumerate(tracks):
        for idx2,track in enumerate(tracks):
            if track == tracks[idx] and idx != idx2:
                if(checkTrackName(track[0], tracks[idx][0])) == True:
                    print("Match found for {}".format(track[0]))
                    print("Track ID: {}".format(track[1]))

def checkTrackName(trackName1, trackName2):
    count = 0
    totalCount = len(trackName2)
    for idx,char in enumerate(trackName1):
        if char == trackName2[idx]:
            count += 1
    if count == totalCount or totalCount/count > 0.8:
        return True
    else:
        return False
        


def getTracks(response):
    listOfTracks = []
    tracks = response.json()['tracks']['items']
    for track in tracks:
        print(track['track']['name'])
        listOfTracks.append([track['track']['name'], track['track']['id']])
    return listOfTracks


def getAccessToken():
    response = requests.post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'client_credentials',
        'client_id': ClientId,
        'client_secret': ClientSecret
    })
    print(response.json())
    return response.json()['access_token']




if __name__ == '__main__':
    main()