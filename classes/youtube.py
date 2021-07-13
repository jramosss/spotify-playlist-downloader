from __future__ import unicode_literals
import youtube_dl as ytdl
from youtubesearchpython import VideosSearch
from pprint import pprint


class YoutubeUtils:

    def isChosen(self, strr: str):
        return (strr.__contains__('lyrics') or strr.__contains__('Lyrics')
                or strr.__contains__('Letra') or strr.__contains__('letra'))

    def __picker(self, result):
        titles = dict()
        for i, item in enumerate(result):
            titles[i] = item['title']

        chose = 0
        while True:
            print("Which song do you want to download?: \n")
            # TODO print thumbnails
            pprint(titles)
            chose = int(
                input(": "))
            if chose < 0 or chose > len(titles):
                print("Invalid choice")
            else:
                break

        for i, item in enumerate(result):
            if i == chose:
                return item['link']

    def find_video_URL_by_name(self, name, pick=False, nresults=5):
        videosSearch = VideosSearch(name, limit=nresults)
        result = videosSearch.result()['result']
        if pick:
            return self.__picker(result)
        else:
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
