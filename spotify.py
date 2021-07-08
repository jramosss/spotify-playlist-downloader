import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from os import environ
from dotenv import load_dotenv
import spotify_uri

load_dotenv('./.env')

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
#CLIENT_ID = environ["SPOTIPY_CLIENT_ID"]
#CLIENT_SECRET = environ["SPOTIPY_CLIENT_SECRET"]
#print(CLIENT_ID, CLIENT_SECRET)
CLIENT_ID = '65ac6b7644b648f0a4dea2f284e7c164'
CLIENT_SECRET = 'f039081dfe9a4f9c9d2568101224cf27'
spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))


class SpotifyUtils:

    def uriToURL(self, url):
        return spotify_uri.formatURI(url)

    def track_artist_and_names(self, results):
        d = dict()
        for i, item in enumerate(results['items']):
            track = item['track']
            # print("   %d %32.32s %s" %
            #      (i, track['artists'][0]['name'], track['name']))
            d[track['artists'][0]['name']] = track['name']
        return d

    def getTrackNamesFromPlaylist(self, url):
        res = spotify.playlist_tracks(self.uriToURL(url))
        return self.track_artist_and_names(res)

    # TODO now parse from youtube the videos using ytdl
