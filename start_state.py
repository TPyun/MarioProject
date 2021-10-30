import title_state
import game_framework
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('images/loadingImage.jpg')


def exit():
    global image
    del(image)


def update():
    global logo_time

    if logo_time > 1.0:
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()


def pause(): pass


def resume(): pass



