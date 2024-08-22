from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("sounds/0_number_morse_code.ogg.mp3")
play(song)