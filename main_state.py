from pico2d import *

import character
import ui
import background
import terrain
import monsters
import start_state

name = "MainState"

mario = None
# monster = None
background1 = None
ground = None
timeUi = None
bgm = None
font = None
sg = None
nbr = None
somemonsters = None


def enter():
    global mario, background1, ground, timeUi, bgm, sg, nbr, somemonsters
    background1 = background.Background()
    bgm = background.Bgm()
    ground = terrain.Ground()
    sg = terrain.ShortGround()
    nbr = terrain.Brick()
    # monster = monsters.Monster()
    somemonsters = [monsters.Monster() for i in range(5)]
    mario = character.Mario()
    timeUi = ui.TimeUi()

def exit():

    global mario, background1, ground, timeUi, bgm, sg, nbr, somemonsters
    del(mario)
    # del(monster)
    del(somemonsters)
    del(background1)
    del(ground)
    del(sg)
    del(timeUi)
    del(bgm)
    del(nbr)


def pause():
    pass


def resume():
    pass


def handle_events():
    character.handle_events()


def update():
    mario.update()
    # background1.update()
    ground.update()
    # monster.update()
    for monsters.monster in somemonsters:
        monsters.monster.update()
    timeUi.update()
    bgm.update()


def draw():
    clear_canvas()

    background1.draw()
    ground.draw()
    sg.draw()
    # monster.draw()
    for monsters.monster in somemonsters:
        monsters.monster.draw()
    nbr.draw()
    mario.draw()
    timeUi.draw()
    update_canvas()

    delay(0.006)
