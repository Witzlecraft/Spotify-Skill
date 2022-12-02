from mycroft import intent_file_handler, MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context


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
            data = {'inqiury_total': "" + action}
            self.speak_dialog('answer', data)
        


def create_skill():
    return Spotify()

