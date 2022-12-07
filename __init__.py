from mycroft import intent_file_handler, MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context
#import spotipy
import time
from playsound import playsound
import youtube_dl
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import webbrowser
import sys
#from spotipy.oauth2 import SpotifyClientCredentials

class Spotify(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('spotify.intent')
    def handle_spotify(self, message):
        # Get string value from 'action' variable
        action = message.data.get('word')
        
        # Do a blink
        def stop(self):
            subprocess.call(["pkill", "omxplayer"])
            print("Stop now...")

        if action.lower() == "stop":
             subprocess.call(["pkill", "omxplayer"])
             #self.stop_my_subprocess()
	     #return None

        self.log.info("Blinking! " + action)
        data = {'word': "" + action}
        self.speak_dialog('answer', data)
            


        music_name = action
        query_string = urllib.parse.urlencode({"search_query": music_name})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

        video_url = clip2
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = video_url,download=False
        )
        filename = f"{video_info['title']}.mp3"
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))
        print("Playing Audio (" + filename + ")...")
        subprocess.Popen(['omxplayer', '-o', 'hdmi', filename]).wait()




        #spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="86b15566a333442d857c62305715ce33",
        #                                                   client_secret="afd8ce39aa304b6db8fb1901d01b4fec"))
        #if len(sys.argv) > 1:
        #    name = ' '.join(sys.argv[1:])
        #else:
        #    name = ''+action

        #results = spotify.search(q='track:' + name, type='track')
        #items = results['track']['items']
        #if len(items) > 0:
        #    track = items[0]
        #    print(track['name'], track['preview_url'][0]['url'])
        


def create_skill():
    return Spotify()

