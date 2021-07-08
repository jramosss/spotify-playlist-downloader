import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from os import environ
from dotenv import load_dotenv
import spotify_uri

load_dotenv('./.env')

CLIENT_ID = environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = environ["SPOTIPY_CLIENT_SECRET"]

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))


class SpotifyUtils:

    def URLToURI(self, url):
        return spotify_uri.formatURI(url)

    def track_artist_and_names(self, results):
        d = dict()
        artist_and_name = []
        for i, item in enumerate(results['items']):
            track = item['track']
            # print("   %d %32.32s %s" %
            #      (i, track['artists'][0]['name'], track['name']))
            d[track['artists'][0]['name']] = track['name']

        artist_and_name = [key + ' ' + d[key] for key in d.keys()]
        return artist_and_name

    def getTrackNamesFromPlaylist(self, url):
        res = spotify.playlist_tracks(self.URLToURI(url))
        return self.track_artist_and_names(res)

    # TODO now parse from youtube the videos using ytdl
