import character
import monsters
import random
from pico2d import *
import title_state

buildLocation = 0
plus = 0


class Ground:
    image = None

    def __init__(self):
        if Ground.image is None:
            self.groundLong = load_image('images/groundLong.png')

    def update(self):
        global buildLocation
        global plus
        buildLocation = 1500 - character.realXLocation + plus # 연속된 두개의 땅이 계속됨. 1500은 ground사진 중간
        if character.realXLocation % 3000 >= 2200: # 3000이 ground 이미지 가로 길이 2200까지 가면 ground가 다음으로 넘어감
            plus = (character.realXLocation // 3000 + 1) * 3000 # plus는 그림이 끝나면 옮겨야하는 차이값

    def draw(self):
        # if character.leftEndMove is False:
        self.groundLong.draw(buildLocation - 3000 + character.leftEndMove, 30)
        self.groundLong.draw(buildLocation + character.leftEndMove, 30)


class ShortGround:
    def __init__(self):
        self.image = load_image('images/hole.png')
        self.x, self.y = random.randrange(1000, 2300, 100), 30
        pass

    def update(self):
        if self.x + character.leftEndMove + 50 < character.realXLocation and character.velocity < 0:
            self.x = random.randrange(character.realXLocation // 1 + 1000, character.realXLocation // 1 + 1800, 100)

    def draw(self):
        self.image.draw(self.x - character.realXLocation + character.leftEndMove, self.y)
        # draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - character.realXLocation - 40 + character.leftEndMove, self.y - 50, self.x - character.realXLocation + character.leftEndMove + 40, self.y + 36


class Brick:
    def __init__(self):
        self.image = load_image('images/wall/normalwall.png')  # 50*50
        self.imageabnormal = load_image('images/wall/abnormalwall.png')
        self.x, self.y = random.randrange(900, 2300, 50), random.randrange(200, 400, 50)
        self.abnormal = random.randint(0, 9)

    def update(self):
        # 마리오 뒤에 땅 있으면 마리오 가는 방향에 다시 스폰
        if self.x + character.leftEndMove + 50 < character.realXLocation and character.velocity < 0:
            self.abnormal = random.randint(0, 9)
            self.x = random.randrange(character.realXLocation // 1 + 1000, character.realXLocation // 1 + 1800, 50)
            self.y = random.randrange(200, 400, 50)

        if character.realXLocation + 600 < self.x + character.leftEndMove - 305 and character.velocity > 0:
            self.abnormal = random.randint(0, 9)
            self.x = random.randrange(character.realXLocation // 1 - 1000, character.realXLocation // 1 - 400, 50)
            self.y = random.randrange(200, 400, 50)

    def draw(self):
        if self.abnormal != 1:
            self.image.draw(self.x - character.realXLocation + character.leftEndMove, self.y)
        else:
            self.imageabnormal.draw(self.x - character.realXLocation + character.leftEndMove, self.y)
        # draw_rectangle(*self.get_bb())
        # draw_rectangle(*self.get_bb_out1())
        # draw_rectangle(*self.get_bb_out2())

    def get_bb(self):
        return self.x - character.realXLocation + character.leftEndMove - 25, self.y - 25, self.x - character.realXLocation + character.leftEndMove + 25, self.y + 25

    def get_bb_out1(self):
        return self.x - character.realXLocation + character.leftEndMove - 75, self.y + 10, self.x - character.realXLocation + character.leftEndMove - 25, self.y + 25

    def get_bb_out2(self):
        return self.x - character.realXLocation + character.leftEndMove + 25, self.y + 10, self.x - character.realXLocation + character.leftEndMove + 75, self.y + 25


eat = False


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
        self.ima.draw(self.x - character.realXLocation + character.leftEndMove, self.y, 30, 30)
        # draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - character.realXLocation - 15 + character.leftEndMove, self.y - 15, self.x - character.realXLocation + character.leftEndMove + 15, self.y + 15


class Goal:
    def __init__(self):
        self.ima = load_image('images/destination.png')
        self.ima1 = load_image('images/flag.png')
        self.x, self.y = 0, 0

    def update(self):
        self.x = title_state.wave * 4000 - character.realXLocation + character.leftEndMove

        if character.ingoal:
            self.y -= 3
            if character.jumpHeight == 0:
                self.y += 3

    def draw(self):
        self.ima.draw(self.x, 365)
        self.ima1.draw(self.x - 368, 340 + self.y)
        # draw_rectangle(*self.get_bb())
        # draw_rectangle(*self.get_bb1())
        pass

    def get_bb(self):
        return self.x - 325 - 10, 90, self.x - 325 + 10, 370

    def get_bb1(self):
        return self.x - 325 - 500, -10, self.x + 700, 370
