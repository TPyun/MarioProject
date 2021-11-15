from pico2d import *


import monsters
import title_state
import game_framework
import terrain


from monsters import Monster
import character
from ui import TimeUi
from ui import Life
from terrain import Ground
from terrain import Brick
from background import Background
from background import Bgm

import game_world




name = "MainState"

mario = None
monster = None
background = None
ground = None
timeUi = None
bgm = None
font = None
sg = None
# nbr = None
somemonsters = None
allbricks = None
life = None


def enter():
    global mario
    mario = character.Mario()
    game_world.add_object(mario, 1)

    global ground
    ground = Ground()
    game_world.add_object(ground, 1)

    # global somemonsters
    # somemonsters = [monsters.Monster() for i in range(title_state.difficulty * 3)]
    # # game_world.add_object(somemonsters, 1)

    global monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8
    monster1 = Monster()
    monster2 = Monster()
    monster3 = Monster()
    monster4 = Monster()
    monster5 = Monster()
    monster6 = Monster()
    monster7 = Monster()
    monster8 = Monster()
    game_world.add_object(monster1, 1)
    game_world.add_object(monster2, 1)
    game_world.add_object(monster3, 1)
    game_world.add_object(monster4, 1)
    game_world.add_object(monster5, 1)
    game_world.add_object(monster6, 1)
    game_world.add_object(monster7, 1)
    game_world.add_object(monster8, 1)


    global timeUi
    timeUi = TimeUi()
    game_world.add_object(timeUi, 1)

    global allbricks
    allbricks = [terrain.Brick() for i in range(10)]
    # game_world.add_object(allbricks, 1)

    global life
    life = Life()
    game_world.add_object(life, 1)

    global bgm
    bgm = Bgm()
    # game_world.add_object(bgm, 0)

    global background
    background = Background()
    game_world.add_object(background, 0)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    character.handle_events()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # for monsters.monster in somemonsters:
    #     monsters.monster.update()

    # fill here for collision check



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    # for monsters.monster in somemonsters:
    #     monsters.monster.draw()

    for terrain.brick in allbricks:
        terrain.brick.draw()
    update_canvas()



#  ---------------------------------------------------
#
# name = "MainState"
#
# mario = None
# # monster = None
# background1 = None
# ground = None
# timeUi = None
# bgm = None
# font = None
# sg = None
# # nbr = None
# somemonsters = None
# allbricks = None
# life = None
#
#
# def enter():
#     global mario, background1, ground, timeUi, bgm, sg, somemonsters, allbricks, life
#     background1 = background.Background()
#     bgm = background.Bgm()
#     ground = terrain.Ground()
#     sg = terrain.ShortGround()
#     # nbr = terrain.Brick()
#     allbricks = [terrain.Brick() for i in range(10)]
#     # monster = monsters.Monster()
#     somemonsters = [monsters.Monster() for i in range(title_state.difficulty * 3)]
#     mario = character.Mario()
#     timeUi = ui.TimeUi()
#     life = ui.Life()
#
#
# def exit():
#
#     global mario, background1, ground, timeUi, bgm, sg, somemonsters, allbricks, life
#     del(mario)
#     # del(monster)
#     del(somemonsters)
#     del(background1)
#     del(ground)
#     del(sg)
#     del(timeUi)
#     del(bgm)
#     # del(nbr)
#     del(allbricks)
#     del(life)
#
#
# def pause():
#     pass
#
#
# def resume():
#     pass
#
#
# def handle_events():
#     character.handle_events()
#
#
# def update():
#     mario.update()
#     # background1.update()
#     ground.update()
#     # monster.update()
#     for monsters.monster in somemonsters:
#         monsters.monster.update()
#     timeUi.update()
#     bgm.update()
#
#
# def draw():
#     clear_canvas()
#
#     background1.draw()
#     ground.draw()
#     sg.draw()
#     # monster.draw()
#     for monsters.monster in somemonsters:
#         monsters.monster.draw()
#     for terrain.brick in allbricks:
#         terrain.brick.draw()
#     mario.draw()
#     timeUi.draw()
#     life.draw()
#
#     update_canvas()
#
#     delay(0.006)
