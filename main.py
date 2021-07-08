from genericpath import isdir
from spotify import SpotifyUtils
from youtube import YoutubeUtils
from os import system, listdir
from os.path import isdir


def move_to_path(path='songs'):
    if (not isdir(path)):
        system('mkdir ' + path)
    FILES = listdir('.')
    songs = []
    for file in FILES:
        if (file.__contains__('.mp3')):
            songs.append(file)

    for song in songs:
        command = 'mv ' + "'" + song + "' " + path
        system(command)


if __name__ == '__main__':
    sp = SpotifyUtils()
    yt = YoutubeUtils()
    #PLAYLIST_URL = input("Playlist URL: ").strip()
    PLAYLIST_URL = 'https://open.spotify.com/playlist/2pcrXwzjOApXI5QYHifhqm?si=9ca361db2ceb47f6'
    URI = sp.URLToURI(PLAYLIST_URL)
    songs_names = sp.getTrackNamesFromPlaylist(URI)
    songs_yt_links = []
    for name in songs_names:
        songs_yt_links.append(yt.find_video_URL_by_name(name).strip())
    # print(songs_yt_links)
    yt.download_videos(songs_yt_links)
    move_to_path()
