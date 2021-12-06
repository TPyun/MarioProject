from pico2d import *
import random

import monsters
import title_state
import game_framework
import terrain
import ui

from monsters import Monster
import character
from ui import TimeUi
from ui import Life
from ui import Point
from terrain import Ground
from terrain import Brick
from terrain import ShortGround
from background import Background
from background import Bgm
from terrain import Coin
from terrain import Goal

import game_world

name = "MainState"

mario = None
monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8 = None, None, None, None, None, None, None, None
brick0, brick1, brick2, brick3, brick4, brick5, brick6, brick7, brick8, brick9 = None, None, None, None, None, None, None, None, None, None
coin0, coin1, coin2, coin3, coin4, coin5 = None, None, None, None, None, None,
background = None
ground = None
timeUi = None
bgm = None
font = None
sg = None
life = None
goal = None

allmonsters = []
allbricks = []
allcoins = []


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def onlyleftright_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a + 3 > right_b: return False
    if right_a < left_b + 3: return False
    return True

def mario_feet_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mariofeetpos()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def mario_feet_onlyleftright_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mariofeetpos()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a + 3 > right_b: return True
    if right_a < left_b + 3: return True
    return False


def mario_side_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_sidepos()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def mario_monster_side_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_sidepos()
    left_b, bottom_b, right_b, top_b = b.get_monster_body_pos()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def mario_head_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_marioheadpos()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def mario_feet_monster_head_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mariofeetpos()
    left_b, bottom_b, right_b, top_b = b.get_monster_head()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def mario_feet_brickout1_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mariofeetpos()
    left_b, bottom_b, right_b, top_b = b.get_bb_out1()
    if left_a < left_b: return False
    if right_a > right_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def mario_feet_brickout2_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_mariofeetpos()
    left_b, bottom_b, right_b, top_b = b.get_bb_out2()
    if left_a < left_b: return False
    if right_a > right_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global mario
    mario = character.Mario()
    game_world.add_object(mario, 2)

    global ground
    ground = Ground()
    game_world.add_object(ground, 1)

    global allmonsters
    allmonsters = [Monster() for i in range(title_state.difficulty * 2)]
    game_world.add_objects(allmonsters, 2)

    global timeUi
    timeUi = TimeUi()
    game_world.add_object(timeUi, 2)

    global point
    point = Point()
    game_world.add_object(point, 2)


    global allbricks
    allbricks = [Brick() for i in range(5)]
    game_world.add_objects(allbricks, 1)

    global life
    life = Life()
    game_world.add_object(life, 2)

    global bgm
    bgm = Bgm()
    game_world.add_object(bgm, 2)

    global background
    background = Background()
    game_world.add_object(background, 0)

    global sg
    sg = ShortGround()
    game_world.add_object(sg, 1)

    global allcoins
    allcoins = [Coin() for i in range(3)]
    game_world.add_objects(allcoins, 1)

    global goal
    goal = Goal()
    game_world.add_object(goal, 1)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    character.handle_events()


damaged = None
i = 0
r = 0
t = 0
z = 0
a = 0
b = 0
onbrick = False


def update():
    global damaged, i, r, onbrick, t, z, a, b
    for game_object in game_world.all_objects():
        game_object.update()

    for monsters in allmonsters:
        if mario_feet_monster_head_collide(mario, monsters) and i == 0:
            ui.points += 10
            if character.velocity < 0 or character.stopSide < 0:
                monsters.x = random.randint(character.realXLocation // 1 + 1000, character.realXLocation // 1 + 1800)
            elif character.velocity > 0 or character.stopSide > 0:
                monsters.x = random.randint(character.realXLocation // 1 - 1000, character.realXLocation // 1 - 400)

        if mario_monster_side_collide(mario, monsters):
            damaged = True
            character.damaged = True
        if damaged:
            i += 1
            if i <= 1:
                character.leftLife -= 1
        if i > 2:
            r += 1
        if r > 500:
            damaged = False
            character.damaged = False
            i = 0
            r = 0

        if collide(sg, monsters) and a == 0:
            if onlyleftright_collide(sg, monsters):
                if character.velocity < 0 or character.stopSide < 0:
                    monsters.x = random.randint(character.realXLocation // 1 + 1000,
                                                character.realXLocation // 1 + 1800)
                elif character.velocity > 0 or character.stopSide > 0:
                    monsters.x = random.randint(character.realXLocation // 1 - 1000, character.realXLocation // 1 - 400)
            monsters.velocity *= -1
            a = 2
        if a == 2:
            b += 1
        if b > 30:
            a = 0
            b = 0

    for bricks in allbricks:
        if mario_feet_collide(mario, bricks) and character.i > 1:
            character.onbrick = bricks.y - 40
            onbrick = True
            character.jump = False
            character.jumpHeight = 0
            character.fall = False
            character.i = 0
            character.moreHigher = 0
            character.keepJump = True

        if mario_feet_brickout1_collide(mario, bricks) and character.onbrick > 0 and character.i < 1:
            character.fall = True
            onbrick = False

        if mario_feet_brickout2_collide(mario, bricks) and character.onbrick > 0 and character.i < 1:
            character.fall = True
            onbrick = False

        if mario_head_collide(mario, bricks) and character.i <= 25:
            character.keepJump = False
            character.JumpHeight = terrain.Brick().y - 30
            character.i = 37

            if character.velocity < 0 or character.stopSide < 0:
                bricks.x = random.randrange(character.realXLocation // 1 + 1000, character.realXLocation // 1 + 1800, 100)
                bricks.y = random.randrange(250, 400, 100)

            elif character.velocity > 0 or character.stopSide > 0:
                bricks.x = random.randrange(character.realXLocation // 1 - 1000, character.realXLocation // 1 - 400, 100)
                bricks.y = random.randrange(250, 400, 100)

        if mario_side_collide(mario, bricks) and character.i > 0:
            if character.charDir > 0 or character.charDir < 0:
                if character.charDir < 0:
                    character.velocity = 0
                if character.charDir > 0:
                    character.velocity = 0
                character.cankeyup = False

    for coins in allcoins:
        if mario_side_collide(mario, coins):
            ui.points += 5
            bgm.coinsound.play()
            if character.velocity < 0 or character.stopSide < 0:
                coins.x = random.randrange(character.realXLocation // 1 + 1000, character.realXLocation // 1 + 1800, 50)

            if character.velocity > 0 or character.stopSide > 0:
                coins.x = random.randrange(character.realXLocation // 1 - 1000, character.realXLocation // 1 - 400, 50)

    if mario_feet_collide(mario, sg):
        character.jumpHeight -= 5
        if character.jumpHeight < -90:
            character.leftLife = 0


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
