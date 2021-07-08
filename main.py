from genericpath import isdir
from spotify import SpotifyUtils
from youtube import YoutubeUtils
from os import system, listdir
from os.path import isdir
from sys import exit
from platform import system as psystem
from optparse import OptionParser


def move_to_path(path='./songs'):
    if (not isdir(path)):
        system('mkdir ' + path)
    FILES = listdir('.')
    songs = []

    for file in FILES:
        if (file.__contains__('.mp3')):
            songs.append(file)

    for song in songs:
        if psystem() == 'Linux' or psystem() == 'MacOS':
            system('mv ' + "'" + song + "' " + path)
        elif psystem() == 'Windows':
            system('move ' + "'" + song + "' " + path)


def main(pick=False, path=None, nresults=5):
    sp = SpotifyUtils()
    yt = YoutubeUtils()
    PLAYLIST_URL = input("Playlist URL: ").strip()
    if (not sp.is_playlist(PLAYLIST_URL)):
        print("Not a valid spotify playlist")
        exit(1)

    songs_names = sp.getTrackNamesFromPlaylist(PLAYLIST_URL)
    songs_yt_links = []
    for name in songs_names:
        songs_yt_links.append(yt.find_video_URL_by_name(
            name, pick, nresults).strip())

    yt.download_videos(songs_yt_links)
    if path != None:
        move_to_path(path)
    else:
        move_to_path(sp.get_playlist_name(PLAYLIST_URL))


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-p", "--pick",
                      help="If you want to pick which video to download for each song",
                      default=False, action='store_true', dest='pick')

    parser.add_option("--path",
                      help="Choose where to download the songs",
                      action='store', type='string', dest='path', default=None)

    parser.add_option("-n", "--nresults",
                      help="Specify how many results you want to fetch",
                      action='store', type='int', dest='nresults', default=5)
    # https://open.spotify.com/playlist/6uwl0GNgjTluXnc5vRyYLE?si=f04a4626f9fa42bf
    (options, args) = parser.parse_args()
    main(options.pick, options.path, options.nresults)
