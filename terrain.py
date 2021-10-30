import character
from pico2d import *


class Ground:
    def __init__(self):
        self.groundLong = load_image('images/groundLong.png')
        self.groundShort = load_image('images/groundShort.png')

    def draw(self):
        if character.leftEnd is False:
            self.groundLong.draw(character.x + 1500, 30)
            self.groundShort.draw(character.x + 700, 103)
        else:
            self.groundLong.draw(1500, 30)
            self.groundShort.draw(700, 103)