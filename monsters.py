import character
import random
import game_framework
import main_state
import title_state

from pico2d import *

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 5.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


monsterFrame = 0
monsterAniSpeed = 1
spawnBlock = 1
r = 0
stuckwith = False

#
# class Monster:
#     def __init__(self):
#         global spawnBlock
#         self.imageL = load_image('images/monsterL.png')
#         self.imageR = load_image('images/monsterR.png')
#         self.frame = random.randint(0, 3)
#         self.monsterX = random.randint(1000, 1900)
#         self.over2200 = False
#         self.i = 0
#         self.dir = -1
#
#     def update(self):
#         global spawnBlock, monsterAniSpeed, r, stuckwith
#
#         # 마리오와 굼바 상호작용
#         if -1 * character.x - 40 <= self.monsterX + character.leftEndMove - 300 <= -1 * character.x + 40 and character.jumpHeight < 20 and stuckwith is False:
#             character.leftLife -= 1
#             stuckwith = True
#
#         if stuckwith is True:
#             r += 1
#d
#         if r == 900:
#             r = 0
#             stuckwith = False
#         print(r, stuckwith)
#         monsterAniSpeed += 1
#         if monsterAniSpeed % 7 == 0: # 속도조절장치인데 소수만 입력 가능함. 아니면 몇놈만 정해져서 프레임 안넘어감
#             self.frame = (self.frame + 1) % 4
#
#         spawnBlock = ((character.realXLocation + 800) // 3000 + 1)  # 800쓴 이유는 3000배수에서 2200을 넘기면 한칸 넘김
#
#         if 2197 <= character.realXLocation % 3000 <= 2200:
#             main_state.somemonsters = [Monster() for i in range(title_state.difficulty * 3)]
#             self.frame = random.randint(0, 3)
#
#         if character.realXLocation >= 2200 and self.over2200 is False:
#             self.monsterX = random.randint(3000 * (spawnBlock - 1) + 200, 3000 * spawnBlock - 1000)
#             self.over2200 = True
#
#         self.monsterX += 0.5 * self.dir * spawnBlock * 0.5
#         self.i += 1
#         if self.i > 1000:
#             self.dir *= -1
#             self.i = 0
#
#     def draw(self):
#         global monsterAniSpeed
#         if self.dir == -1:
#             self.imageL.clip_draw(self.frame * 51, 0, 50, 60, self.monsterX + character.leftEndMove + character.x, 95)
#         else:
#             self.imageR.clip_draw(self.frame * 51, 0, 50, 60, self.monsterX + character.leftEndMove + character.x, 95)
#
#         # if monsterAniSpeed % 6 == 0:
#         #     self.frame = (self.frame + 1) % 4
#         # monsterAniSpeed += 1


class Monster:
    image = None

    def __init__(self):
        self.velocity = 0
        self.x, self.y = random.randint(1000, 1900), 95
        self.frame = 0
        if Monster.image == None:
            self.ima = load_image('images/turtle.png')
            self.ima1 = load_image('images/monsterL.png')
        self.velocity -= RUN_SPEED_PPS
        self.dir = 0
        self.i = 0
        self.species = random.randint(0, 1)

    def update(self):
        self.i += 1
        if self.i > random.randint(100, 10000000):
            self.velocity *= -1
            self.i = 0
        # if self.x > 700:
        #     self.velocity = -1 * RUN_SPEED_PPS
        # elif self.x < 100:
        #     self.velocity = RUN_SPEED_PPS
        self.dir = clamp(-1, self.velocity, 1)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.velocity * game_framework.frame_time

        # 마리오 뒤에 몬스터 있으면 마리오 가는 방향에 다시 스폰
        if self.x + character.leftEndMove + 50 < character.realXLocation and character.velocity < 0:
            self.x = random.randint(character.realXLocation // 1 + 1000, character.realXLocation // 1 + 1800)
            self.species = random.randint(0, 1)

        if character.realXLocation + 600 < self.x + character.leftEndMove - 305 and character.velocity > 0:
            self.x = random.randint(character.realXLocation // 1 - 1000, character.realXLocation // 1 - 400)
            self.species = random.randint(0, 1)
        # print(character.velocity, self.x + character.leftEndMove - 305, character.realXLocation, character.velocity)

    def draw(self):
        if self.species == 0:
            if self.dir == -1:
                self.ima.clip_draw(int(self.frame) * 51, 0, 50, 60, self.x - character.realXLocation + character.leftEndMove, self.y)
            else:
                self.ima.clip_composite_draw(int(self.frame) * 51, 0, 50, 60, 0, 'h', self.x - character.realXLocation + character.leftEndMove, self.y, 50, 60)
        else:
            if self.dir == -1:
                self.ima1.clip_draw(int(self.frame) * 51, 0, 50, 60, self.x - character.realXLocation + character.leftEndMove, self.y)
            else:
                self.ima1.clip_composite_draw(int(self.frame) * 51, 0, 50, 60, 0, 'h', self.x - character.realXLocation + character.leftEndMove, self.y, 50, 60)

        draw_rectangle(*self.get_monster_head())
        draw_rectangle(*self.get_monster_body_pos())
        draw_rectangle(*self.get_bb())

    def get_monster_body_pos(self):
        return self.x - character.realXLocation + character.leftEndMove - 20, self.y - 20, self.x - character.realXLocation + character.leftEndMove + 20, self.y + 15

    def get_monster_head(self):
        return self.x - character.realXLocation + character.leftEndMove - 15, self.y + 15, self.x - character.realXLocation + character.leftEndMove + 15, self.y + 20

    def get_bb(self):
        return self.x - character.realXLocation + character.leftEndMove - 20, self.y - 30, self.x - character.realXLocation + character.leftEndMove + 20, self.y + 20