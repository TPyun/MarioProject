import character
from pico2d import *

buildLocation = 0
plus = 0


class Ground:
    def __init__(self):
        self.groundLong = load_image('images/groundLong.png')
        self.groundShort = load_image('images/groundShort.png')

    def update(self):
        global buildLocation
        global plus
        buildLocation = 1500 - character.realXLocation + plus # 연속된 두개의 땅이 께속됨
        if character.realXLocation % 3000 >= 2200:
            plus = (character.realXLocation // 3000 + 1) * 3000

    def draw(self):

        if character.leftEnd is False:
            self.groundLong.draw(buildLocation - 3000, 30)
            self.groundLong.draw(buildLocation, 30)
            self.groundShort.draw(character.x + 700, 103)
        else:
            self.groundLong.draw(1500, 30)
            self.groundShort.draw(700, 103)
