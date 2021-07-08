# Spotify Downloader

### Have you ever wanted to download many songs but the process was very slow and handmade? Well, this is your program.
This program downloads all songs from a specified playlist.

---

## Setup:
* Optional but recommended: setup a virtual enviroment with `python3 -m venv path/to/repo ; source bin/activate`
* $ `pip install -r requirements.txt`
* Later, set the enviroment variables *SPOTIPY_CLIENT_ID* and *SPOTIPY_CLIENT_SECRET* which you can get [*here*](https://developer.spotify.com/dashboard/login)
* All set!

## Usage:
Run the main file with python main.py, then, enter a playlist URL and the program will download all the songs to the ./your_playlist_name folder

### Options:

* **-n or --nresults**:  
Lets you decide how many videos you want to fetch (default 5) and you can set it with python3 main.py --nresults=10.   
Why would i want to do that? The answer is just below you.   
This flag wont do anything if the flag --pick isnt set.

* **-p or --pick**:  
What if i dont want the program to decide which song to download? I want to do it!, well you can do it because im an awesome programmer.
Run the program with the flag -p or --pick, then the program will give you some options *(default 5, but you can specify how much you want with the --nresults flag!)*.

* **--path**:  
What if i dont want to store the songs in the *my_playlist_name* folder?, use the --path option to tell the program where to store the songs.