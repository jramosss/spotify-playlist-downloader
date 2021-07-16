from __future__ import unicode_literals
import youtube_dl as ytdl
from youtubesearchpython import VideosSearch
from pprint import pprint
from utils.utils import print_in_green, print_in_red


class YoutubeUtils:

    def isChosen(self, strr: str):
        strr = strr.lower()
        wanted_words = ['lyrics', 'letra']
        banned_words = ['reaccion',
                        'reaction', 'coreography', 'dance', 'bass boosted',
                        'choreography', 'official video', 'video oficial', '1 hora', '10 horas']
        for word in wanted_words:
            if strr.__contains__(word):
                return True
        for word in banned_words:
            if strr.__contains__(word):
                return False
        return True

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

    def download_videos(self, names_and_urls):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        failed = {}
        with ytdl.YoutubeDL(ydl_opts) as ydl:
            i = 1
            for name in names_and_urls.keys():
                try:
                    ydl.download([names_and_urls[name]])
                    print_in_green("Downloaded " + name +
                                   " " + str(i) + '/' + str(len(names_and_urls)))
                    i += 1
                except Exception as e:
                    try:
                        # TODO do something with this
                        failed[name] = names_and_urls[name]
                        print_in_red("ERROR: Failed to download " +
                                     name, " " + str(e))
                    except:
                        pass
