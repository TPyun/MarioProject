import character
import monsters
import random
from pico2d import *

buildLocation = 0
plus = 0


class Ground:
    def __init__(self):
        self.groundLong = load_image('images/groundLong.png')

    def update(self):
        global buildLocation
        global plus
        buildLocation = 1500 - character.realXLocation + plus # 연속된 두개의 땅이 계속됨. 1500은 ground사진 중간
        if character.realXLocation % 3000 >= 2200: # 3000이 ground 이미지 가로 길이 2200까지 가면 ground가 다음으로 넘어감
            plus = (character.realXLocation // 3000 + 1) * 3000 # plus는 그림이 끝나면 옮겨야하는 차이값

    def draw(self):
        if character.leftEnd is False:
            self.groundLong.draw(buildLocation - 3000, 30)
            self.groundLong.draw(buildLocation, 30)

        else:
            self.groundLong.draw(1500, 30)


class ShortGround:
    def __init__(self):
    #   self.image = load_image('images/groundShort.png') # 100 * 73
        pass

    def draw(self):
        # if character.leftEnd is False:
        #     self.image.draw(character.x + 700, 103)
        # else:
        #     self.image.draw(700, 103)
        pass


class Brick:
    def __init__(self):
        self.image = load_image('images/wall/normalwall.png') # 50*50
        self.buildLocation = random.randrange(50, 2300, 50)
        self.buildHeight = random.randrange(250, 400, 50)
        self.sticked = random.randint(0, 1)

    def draw(self):
        if 2197 <= character.realXLocation % 3000 <= 2200:
            self.buildLocation = random.randrange(50 + 3000 * (monsters.spawnBlock - 1),
                                                  3000 * (monsters.spawnBlock - 1) + 2000, 50)

        # print(self.buildLocation)
        # print(character.realXLocation)

        self.image.draw(self.buildLocation - character.realXLocation + character.leftEndMove, self.buildHeight)
        self.image.draw(self.buildLocation - character.realXLocation + character.leftEndMove + 3000, self.buildHeight)
