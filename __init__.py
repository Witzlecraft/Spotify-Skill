from mycroft import intent_file_handler, MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context
import spotipy
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

            sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="86b15566a333442d857c62305715ce33", client_secret="c0640cff12c64092abedb334d9678fc8"))
            results = sp.search(q='weezer', limit=20)
            for idx, track in enumerate(results['tracks']['items']):
                print(idx, track['name'])
        


def create_skill():
    return Spotify()

