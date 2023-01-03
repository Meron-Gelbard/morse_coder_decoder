from playsound import playsound
from code_engine import MorseDictionary
import time

class MorsePlayer:
    def __init__(self):
        self.dot_snd = 'dot.mp3'
        self.dash_snd = 'dash.mp3'
        self.space_snd = 'space.mp3'
        self.run = False

        self.morse = MorseDictionary()

    def play_code(self, code, code_highlight):
        self.run = True
        while self.run:
            for i in range(len(code)):
                if not self.run:
                    break
                if code[i] == '.':
                    code_highlight(i)
                    playsound(self.dot_snd)
                    time.sleep(0.18)
                if code[i] == '-':
                    code_highlight(i)
                    playsound(self.dash_snd)
                    time.sleep(0.18)
                if code[i] == ' ':
                    code_highlight(i)
                    playsound(self.space_snd)
                    time.sleep(0.03)
            self.run = False
            return
