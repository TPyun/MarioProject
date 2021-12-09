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


class Monster:
    image = None

    def __init__(self):
        self.velocity = 0
        self.x, self.y = random.randint(1000, 1900), 95
        self.frame = 0
        if Monster.image is None:
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
                self.ima.clip_draw(int(self.frame) * 51, 0, 48, 60, self.x - character.realXLocation + character.leftEndMove, self.y)
            else:
                self.ima.clip_composite_draw(int(self.frame) * 51, 0, 48, 60, 0, 'h', self.x - character.realXLocation + character.leftEndMove, self.y, 50, 60)
        else:
            if self.dir == -1:
                self.ima1.clip_draw(int(self.frame) * 51, 0, 50, 60, self.x - character.realXLocation + character.leftEndMove, self.y)
            else:
                self.ima1.clip_composite_draw(int(self.frame) * 51, 0, 50, 60, 0, 'h', self.x - character.realXLocation + character.leftEndMove, self.y, 50, 60)

        # draw_rectangle(*self.get_monster_head())
        # draw_rectangle(*self.get_monster_body_pos())
        # draw_rectangle(*self.get_bb())

    def get_monster_body_pos(self):
        return self.x - character.realXLocation + character.leftEndMove - 20, self.y - 20, self.x - character.realXLocation + character.leftEndMove + 20, self.y + 5

    def get_monster_head(self):
        return self.x - character.realXLocation + character.leftEndMove - 20, self.y + 5, self.x - character.realXLocation + character.leftEndMove + 20, self.y + 20

    def get_bb(self):
        return self.x - character.realXLocation + character.leftEndMove - 20, self.y - 30, self.x - character.realXLocation + character.leftEndMove + 20, self.y + 20