"""
Dependencies: mpg123 - a command line tool
"""

from gtts import gTTS
import subprocess

NAME = "Speak"


def serve(command, SERVE):
    tts = gTTS(text=command, lang='en')
    tts.save("./temp/1.mp3")
    subprocess.call(['mpg123', './temp/1.mp3'])
