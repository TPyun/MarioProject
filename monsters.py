import character
from pico2d import *

monsterWalk = False
monsterX = 0
monsterFrame = 0
monsterAniSpeed = 1


class Monster:
    def __init__(self):
        self.imageL = load_image('images/monsterL.png')

    def update(self):
        global monsterWalk
        if character.x < -300:
            monsterWalk = True

    def draw(self):
        global monsterAniSpeed
        global monsterFrame
        global monsterX
        if monsterWalk:
            self.imageL.clip_draw(monsterFrame * 51, 0, 50, 60, 1200 + monsterX + character.leftEndMove + character.x, 95)
            monsterX -= 0.5
        if monsterAniSpeed % 6 == 0:
            monsterFrame = (monsterFrame + 1) % 4
        monsterAniSpeed += 1
