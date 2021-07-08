from __future__ import unicode_literals
import youtube_dl as ytdl
from youtubesearchpython import VideosSearch


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
        for i, item in enumerate(result):
            if (i == 1):
                return item['link']

    def download_videos(self, urls):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with ytdl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
