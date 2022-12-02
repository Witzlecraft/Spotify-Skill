from mycroft import intent_file_handler, MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('spotify.intent')
    def handle_spotify(self, message):
        # Get string value from 'action' variable
        action = message.data.get('word')
        
        # Do a blink
        if action.lower() == "blink":
            self.log.info("Blinking! " + action)
            data = {'word': "" + action}
            self.speak_dialog('answer', data)


            spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
            if len(sys.argv) > 1:
                name = ' '.join(sys.argv[1:])
            else:
                name = 'Radiohead'

            results = spotify.search(q='artist:' + name, type='artist')
            items = results['artists']['items']
            if len(items) > 0:
                artist = items[0]
                print(artist['name'], artist['images'][0]['url'])
        


def create_skill():
    return Spotify()

