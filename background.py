import character
import game_framework
import title_state
from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('images/background.png')
        self.ima = load_image('images/background1.png')
        self.drawblock = (character.realXLocation - 800) // 2666 + 1
        self.i = 0

    def update(self):
        self.drawblock = (character.realXLocation - 800) // 2666 + 1
        pass

    def draw(self):
        if character.leftEnd is False:
            self.image.draw(character.x + 1333 + 2666 * (self.drawblock - 1), 420)
            self.image.draw(character.x + 1333 + 2666 * self.drawblock, 420)
        else:
            self.image.draw(1333, 420)


class Bgm:
    def __init__(self):
        self.marioWav = load_wav('sound/Mario.wav')
        self.jumpWav = load_wav('sound/jump.wav')
        self.coinsound = load_wav('sound/eatmoney.wav')
        self.dead = load_wav('sound/death1.wav')
        self.dead1 = load_wav('sound/death2.wav')
        self.deadimage = load_image('images/dead.jpg')
        self.kill = load_wav('sound/kill.wav')
        self.i = 0

        if character.running is True:
            self.marioWav.play()

    def update(self):
        if character.jump is True and character.jumpHeight == 0:
            self.jumpWav.play()
        if character.leftLife == 0:
            self.i += 1
        if self.i == 300:
            game_framework.change_state(title_state)
        if self.i == 1:
            self.marioWav.__del__()
            self.dead.play()
            self.dead1.play()

    def draw(self):
        if self.i > 0:
            self.deadimage.draw(400, 300, 1200, 600)
        pass
