from pydub import AudioSegment
from pydub.playback import play


def playSpeech():
    response = AudioSegment.from_mp3("response.mp3")
    play(response)