import character
import random
from pico2d import *


monsterFrame = 0
monsterAniSpeed = 1


class Monster:
    def __init__(self):
        self.imageL = load_image('images/monsterL.png')
        self.monsterX = random.randint(200, 3000)
        self.frame = random.randint(0, 3)

    def update(self):
        global monsterAniSpeed
        self.monsterX -= 0.5
        monsterAniSpeed += 1
        if monsterAniSpeed % 7 == 0: # 속도조절장치인데 소수만 입력 가능함. 아니면 몇놈만 정해져서 프레임 안넘어감
            self.frame = (self.frame + 1) % 4

    def draw(self):
        global monsterAniSpeed
        self.imageL.clip_draw(self.frame * 51, 0, 50, 60, 1200 + self.monsterX + character.leftEndMove + character.x, 95)

        # if monsterAniSpeed % 6 == 0:
        #     self.frame = (self.frame + 1) % 4
        # monsterAniSpeed += 1
