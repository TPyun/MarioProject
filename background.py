import character
from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('images/background.png')
        self.ima = load_image('images/background1.png')
        self.drawblock = (character.realXLocation - 800) // 2666 + 1

    def update(self):
        self.drawblock = (character.realXLocation - 800) // 2666 + 1
        pass

    def draw(self):
        if character.leftEnd is False:
            self.image.draw(character.x + 1333 + 2666 * (self.drawblock - 1), 420)
            self.image.draw(character.x + 1333 + 2666 * (self.drawblock), 420)
        else:
            self.image.draw(1333, 420)


class Bgm:
    def __init__(self):
        self.marioWav = load_wav('sound/Mario.wav')
        self.jumpWav = load_wav('sound/jump.wav')
        if character.running is True:
            self.marioWav.play()

    def update(self):
        if character.jump is True and character.jumpHeight == 0:
            self.jumpWav.play()
        # print(character.jump, character.jumpHeight)
        pass

    def draw(self):
        pass