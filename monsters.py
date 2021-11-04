import character
import random
import main_state
import terrain
from pico2d import *


monsterFrame = 0
monsterAniSpeed = 1
spawnBlock = 1


class Monster:
    def __init__(self):
        global spawnBlock
        self.imageL = load_image('images/monsterL.png')
        self.imageR = load_image('images/monsterR.png')
        self.frame = random.randint(0, 3)
        self.monsterX = random.randint(1000, 1900)
        self.over2200 = False
        self.stop = False
        self.i = 0
        self.dir = -1

    def update(self):
        global spawnBlock
        global monsterAniSpeed

        monsterAniSpeed += 1
        if monsterAniSpeed % 7 == 0: # 속도조절장치인데 소수만 입력 가능함. 아니면 몇놈만 정해져서 프레임 안넘어감
            self.frame = (self.frame + 1) % 4

        spawnBlock = ((character.realXLocation + 800) // 3000 + 1)  # 800쓴 이유는 3000배수에서 2200을 넘기면 한칸 넘김

        if 2197 <= character.realXLocation % 3000 <= 2200 and self.stop is False:
            main_state.somemonsters = [Monster() for i in range(10)]
            self.frame = random.randint(0, 3)
            if character.realXLocation % 3000 > 2200:
                self.stop = True

        if character.realXLocation >= 2200 and self.over2200 is False:
            self.monsterX = random.randint(3000 * (spawnBlock - 1) + 200, 3000 * spawnBlock - 1000)
            self.over2200 = True

        self.monsterX += 0.5 * self.dir
        self.i += 1
        if self.i > 1000:
            self.dir *= -1
            self.i = 0

        if character.realXLocation - 100 < self.monsterX + character.leftEndMove + character.x < character.realXLocation + 100 and character.jumpHeight < 10:
            character.Mario().die = True
            print(character.Mario().die)
 
    def draw(self):
        global monsterAniSpeed
        if self.dir == -1:
            self.imageL.clip_draw(self.frame * 51, 0, 50, 60, self.monsterX + character.leftEndMove + character.x, 95)
        else:
            self.imageR.clip_draw(self.frame * 51, 0, 50, 60, self.monsterX + character.leftEndMove + character.x, 95)

        # if monsterAniSpeed % 6 == 0:
        #     self.frame = (self.frame + 1) % 4
        # monsterAniSpeed += 1
