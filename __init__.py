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
        #if action.lower() == "blink":
        self.log.info("Blinking! " + action)
        data = {'word': "" + action}
        self.speak_dialog('answer', data)

        spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="86b15566a333442d857c62305715ce33",
                                                           client_secret="afd8ce39aa304b6db8fb1901d01b4fec"))
        if len(sys.argv) > 1:
            name = ' '.join(sys.argv[1:])
        else:
            name = ''+action

        results = spotify.search(q='tracks:' + name, type='track')
        items = results['track']['items']
        if len(items) > 0:
            track = items[0]
            print(track['name'], track['preview_url'][0]['url'])
        


def create_skill():
    return Spotify()

