import title_state
import game_framework
from pico2d import *


name = "StartState"
image = None
loadingbar = None
loadcolor = None
logo_time = 0.0
x = 0


def enter():
    global image, loadingbar, loadcolor, x
    image = load_image('images/loadingImage.jpg')
    loadingbar = load_image('images/loadingbar.png')
    loadcolor = load_image('images/loadbar.png')


def exit():
    global image, loadingbar, loadcolor
    del(image, loadingbar, loadcolor)


def update():
    global logo_time, x
    if logo_time > 1.0:
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01
    x += 10
    if x > 450:
        x = 450


def draw():
    global image, loadingbar, loadcolor
    clear_canvas()
    image.draw(400, 300)
    loadcolor.clip_draw(0, 0, x, 33, 400, 90)
    loadingbar.draw(400, 200)

    update_canvas()


def handle_events():
    events = get_events()


def pause(): pass


def resume(): pass
