import character
import monsters
import random
from pico2d import *

buildLocation = 0
plus = 0


class Ground:
    image = None

    def __init__(self):
        if Ground.image == None:
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


# class Brick:
#     def __init__(self):
#         self.image = load_image('images/wall/normalwall.png') # 50*50
#         self.buildLocation = random.randrange(50, 2300, 50)
#         self.buildHeight = random.randrange(250, 400, 50)
#         self.sticked = random.randint(0, 1)
#
#     def update(self):
#         pass
#
#     def draw(self):
#         if 2197 <= character.realXLocation % 3000 <= 2200:
#             self.buildLocation = random.randrange(50 + 3000 * (monsters.spawnBlock - 1),
#                                                   3000 * (monsters.spawnBlock - 1) + 2000, 50)
#
#         # print(self.buildLocation)
#         # print(character.realXLocation)
#
#         self.image.draw(self.buildLocation - character.realXLocation + character.leftEndMove, self.buildHeight)
#         self.image.draw(self.buildLocation - character.realXLocation + character.leftEndMove + 3000, self.buildHeight)


class Brick:
    image = None

    def __init__(self):
        if Brick.image == None:
            self.image = load_image('images/wall/normalwall.png')  # 50*50
            self.imageabnormal = load_image('images/wall/abnormalwall.png')
            self.x, self.y = random.randrange(300, 2300, 50), random.randrange(200, 400, 50)
            self.abnormal = random.randint(0, 9)

    def update(self):
        # 마리오 뒤에 몬스터 있으면 마리오 가는 방향에 다시 스폰
        if self.x + character.leftEndMove + 50 < character.realXLocation and character.velocity < 0:
            self.abnormal = random.randint(0, 9)
            self.x = random.randrange(character.realXLocation // 1 + 1000, character.realXLocation // 1 + 1800, 50)
            self.y = random.randrange(200, 400, 50)

        if character.realXLocation + 600 < self.x + character.leftEndMove - 305 and character.velocity > 0:
            self.abnormal = random.randint(0, 9)
            self.x = random.randrange(character.realXLocation // 1 - 1000, character.realXLocation // 1 - 400, 50)
            self.y = random.randrange(200, 400, 50)

        # if 325 < self.x - character.realXLocation + character.leftEndMove - 25 < 335 and self.y - 50 < character.jumpHeight + character.moreHigher < self.y + 50 and character.velocity < 0:
        #     if self.y - 25 < character.jumpHeight + 100 < self.y + 25:
        #         character.velocity += character.RUN_SPEED_PPS
        #         character.keepJump = False
        #     if character.stopSide == 1:
        #         if character.charDir == 1:  # a,d 동시입력하다가 손떼면 가던 방향 계속 갈수 있게끔
        #             character.charDir = -1
        #             character.velocity -= character.RUN_SPEED_PPS * 2
        #
        # print(character.velocity)

    def draw(self):
        if self.abnormal != 1:
            self.image.draw(self.x - character.realXLocation + character.leftEndMove, self.y)
        else:
            self.imageabnormal.draw(self.x - character.realXLocation + character.leftEndMove, self.y)
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb_out1())
        draw_rectangle(*self.get_bb_out2())

    def get_bb(self):
        return self.x - character.realXLocation + character.leftEndMove - 25, self.y - 25, self.x - character.realXLocation + character.leftEndMove + 25, self.y + 25

    def get_bb_out1(self):
        return self.x - character.realXLocation + character.leftEndMove - 75, self.y + 10, self.x - character.realXLocation + character.leftEndMove - 25, self.y + 25

    def get_bb_out2(self):
        return self.x - character.realXLocation + character.leftEndMove + 25, self.y + 10, self.x - character.realXLocation + character.leftEndMove + 75, self.y + 25


class Coin:
    def __init__(self):
        self.ima = load_image('images/money.png')
        self.x, self.y = random.randrange(500, 2300, 50), 100

    def update(self):
        if self.x + character.leftEndMove + 50 < character.realXLocation and character.velocity < 0:
            self.x = random.randrange(character.realXLocation // 1 + 1000, character.realXLocation // 1 + 1800, 50)

        if character.realXLocation + 600 < self.x + character.leftEndMove - 305 and character.velocity > 0:
            self.x = random.randrange(character.realXLocation // 1 - 1000, character.realXLocation // 1 - 400, 50)

    def draw(self):
        self.ima.draw(self.x - character.realXLocation + character.leftEndMove, self.y)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - character.realXLocation - 20 + character.leftEndMove, self.y - 20, self.x - character.realXLocation + character.leftEndMove + 20, self.y + 20


class Goal:
    def __init__(self):
        self.ima = load_image('images/final.png')
        self.ima1 = load_image('images/tower.png')
        pass

    def update(self):
        pass

    def draw(self):
        pass