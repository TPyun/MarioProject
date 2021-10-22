import character
import ui
import background
import terrain
import monsters

from pico2d import *


open_canvas()

bgm = background.Bgm()
background = background.Background()
ground = terrain.Ground()
monster = monsters.Monster()
mario = character.Mario()
timeUi = ui.TimeUi()

while character.running:
    character.handle_events()
    clear_canvas()

    background.update()
    ground.update()
    monster.update()
    mario.update()
    timeUi.update()

    print(character.jump, character.keepJump, character.i, character.x)

    print_fps()

    monster.draw()
    mario.draw()
    bgm.play()

    update_canvas()
    delay(0.01)

close_canvas()
