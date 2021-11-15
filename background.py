import character
from pico2d import *


class Background:
    def __init__(self):
        self.image = load_image('images/background.png')
        # self.image = load_image('images/background_0000.gif')

    def update(self):
        pass

    def draw(self):
        if character.leftEnd is False:
            self.image.draw(character.x / 8 + 1300, 420)  # 백그라운드가 움직이게 하기 위해서 x좌표 입력
        else:
            self.image.draw(1300, 420)


class Bgm:
    def __init__(self):
        self.marioWav = load_wav('sound/Mario.wav')
        self.jumpWav = load_wav('sound/jump.wav')
        if character.running is True:
            self.marioWav.play()

    def update(self):
        if character.jump is True and character.jumpHeight == 0:
            self.jumpWav.play()

    def draw(self):
        pass