from classes.spotify import SpotifyUtils
from classes.youtube import YoutubeUtils
from os import system
from os.path import isdir
from platform import system as psystem
from optparse import OptionParser

# https://open.spotify.com/playlist/7vmhdvmFLeEs6gNoUg1dmF?si=c29e021775164965 2 songs
# https://open.spotify.com/playlist/78tw7XfmsRyQNMf3iFiDy6?si=ddce76760c8b4cc8 23 songs
# https://open.spotify.com/playlist/37i9dQZEVXbMMy2roB9myp?si=cc2a8fca549048a0 50 songs
# https://open.spotify.com/playlist/4kYzJUyyotahj7jNHLjVn3?si=9c2176a7d1f54020 +2000 songs


def move_to_path(path: str = './songs'):
    path = path.strip()
    path = path.replace(' ', '_')
    print("path: ", path)
    if (not isdir(path)):
        system('mkdir ' + path)
    sys = psystem()
    if sys == 'Linux' or sys == 'macOS':
        system('mv *.mp3 ' + path)
    elif sys == 'Windows':
        system('move *.mp3 ' + path)
    else:
        print('\033[91m' +
              "ERROR: Not recognized OS " + sys + ",files will stay in this folder")
        print('\033[39m')


def main(pick=False, path=None, nresults=5):
    sp = SpotifyUtils()
    yt = YoutubeUtils()
    PLAYLIST_URL = input("Playlist URL: ").strip()
    if psystem() == 'Windows':
        _path = input("Specify a path (leave it blank for default): ")
        if _path == '' or _path == "" or _path == " " or _path == ' ':
            path = _path
        _pick = input("Do you want to pick which song to download? <y/n>: ")
        pick = _pick == 'y'
        _nresults = input(
            "How much results do you want to fetch? (default 5) (If you dont know what this means leave it blank): ")
        if _nresults != '':
            nresults = int(_nresults)

    if not sp.is_playlist(PLAYLIST_URL):
        print("Not a valid spotify playlist")
        main()

    print('\033[92m' + "Getting song names...")
    print('\033[39m')
    songs_names = sp.getTrackNamesFromPlaylist(PLAYLIST_URL)
    songs_yt_names_and_links = {}
    for name in songs_names:
        songs_yt_names_and_links[name] = (yt.find_video_URL_by_name(
            name, pick, nresults).strip())

    print('\033[92m' + "Downloading songs...")
    print('\033[39m')
    yt.download_videos(songs_yt_names_and_links)
    if path != None:
        print('\033[92m' + "Moving songs to " + path)
        print('\033[39m')
        if path != '.':
            move_to_path(path)
    else:
        move_to_path(sp.get_playlist_name(PLAYLIST_URL))

    retry = input(
        '\033[94m' + "Press y to download another playlist, press any other key to exit: ")
    print('\033[39m')
    if retry == 'y':
        main()


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
