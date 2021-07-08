from __future__ import unicode_literals
import youtube_dl as ytdl
from youtubesearchpython import VideosSearch
from os import system


class YoutubeUtils:

    def isChosen(self, strr: str):
        return (strr.__contains__('lyrics') or strr.__contains__('Lyrics')
                or strr.__contains__('Letra') or strr.__contains__('letra'))

    def find_video_URL_by_name(self, name):
        videosSearch = VideosSearch(name, limit=5)
        result = videosSearch.result()['result']
        for i, item in enumerate(result):
            if (self.isChosen(item['title'])):
                return item['link']
        # If there`s no chosen one, choose the second
        return item[1]['link']

    def download_video(self, urls, path='./songs'):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with ytdl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([urls])
