from pico2d import *

import character
import ui
import background
import terrain
import monsters


name = "MainState"

mario = None
monster = None
background1 = None
ground = None
timeUi = None
bgm = None
font = None


def enter():
    global mario, monster, background1, ground, timeUi, bgm
    background1 = background.Background()
    bgm = background.Bgm()
    ground = terrain.Ground()
    monster = monsters.Monster()
    mario = character.Mario()
    timeUi = ui.TimeUi()


def exit():
    # global boy, grass
    # del(boy)
    # del(grass)
    global mario, monster, background1, ground, timeUi, bgm
    del(mario)
    del(monster)
    del(background1)
    del(ground)
    del(timeUi)
    del(bgm)


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
    monster.update()
    timeUi.update()
    bgm.update()


def draw():
    clear_canvas()

    background1.draw()
    ground.draw()
    monster.draw()
    mario.draw()
    timeUi.draw()
    update_canvas()

    delay(0.006)
