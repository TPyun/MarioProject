import character
import main_state
import game_framework
from pico2d import *


name = "TitleState"
ready = None
howlong = None
easy = None
normal = None
hard = None
hell = None
waves = None
btnup = None
btndown = None
playbtn = None
mouse = None
x, y = 0, 0
click = False
difficulty = 2
wave = 1
i = 0
i1, i2, i3, i4, i5, i6, i7, i8, i9 = None,None,None,None,None,None,None,None,None
btnsound = None


def enter():
    global ready, howlong, easy, normal, hard, hell, waves, btnup, btndown, mouse, btnsound, playbtn, i1, i2, i3, i4, i5, i6, i7, i8, i9
    i1 = load_image('images/number/clock/w1.png')
    i2 = load_image('images/number/clock/w2.png')
    i3 = load_image('images/number/clock/w3.png')
    i4 = load_image('images/number/clock/w4.png')
    i5 = load_image('images/number/clock/w5.png')
    i6 = load_image('images/number/clock/w6.png')
    i7 = load_image('images/number/clock/w7.png')
    i8 = load_image('images/number/clock/w8.png')
    i9 = load_image('images/number/clock/w9.png')
    ready = load_image('images/ready-1.png')
    howlong = load_image('images/howlong.png')
    easy = load_image('images/easy.png')
    normal = load_image('images/normal.png')
    hard = load_image('images/hard.png')
    hell = load_image('images/hell.png')
    waves = load_image('images/waves.png')
    btnup = load_image('images/btnup.png')
    btndown = load_image('images/btndown.png')
    mouse = load_image('images/hand_arrow.png')
    btnsound = load_wav('sound/btnsound.wav')
    playbtn = load_image('images/playbtn.png')


def exit():
    global ready, howlong, easy, normal, hard, hell, waves, btnup, btndown, mouse, i1, i2, i3, i4, i5, i6, i7, i8, i9, btnsound, playbtn
    del(ready, howlong, easy, normal, hard, hell, waves, btnup, btndown, mouse, i1, i2, i3, i4, i5, i6, i7, i8, i9, btnsound, playbtn)


def handle_events():
    global x, y, click
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #     game_framework.change_state(main_state)

        if event.type == SDL_MOUSEMOTION:
            x = event.x
            y = event.y
        if event.type == SDL_MOUSEBUTTONDOWN:
            click = True


def draw():
    global i
    clear_canvas()
    hide_cursor()
    i += 1
    ready.draw(400, 300)
    if i > 100:
        howlong.draw(400, 300)
    if i > 200:
        waves.draw(400, 300)

        if difficulty == 1:
            easy.draw(400, 300)
            character.leftLife = 5

        if difficulty == 2:
            normal.draw(400, 300)
            character.leftLife = 4

        if difficulty == 3:
            hard.draw(400, 300)
            character.leftLife = 3

        if difficulty == 4:
            hell.draw(400, 300)
            character.leftLife = 2

        btnup.draw(110, 430)
        btndown.draw(110, 320)
        btnup.draw(540, 430)
        btndown.draw(540, 320)
        playbtn.draw(400, 300)

        if wave == 1:
            i1.draw(540, 380)
        if wave == 2:
            i2.draw(540, 380)
        if wave == 3:
            i3.draw(540, 380)
        if wave == 4:
            i4.draw(540, 380)
        if wave == 5:
            i5.draw(540, 380)
        if wave == 6:
            i6.draw(540, 380)
        if wave == 7:
            i7.draw(540, 380)
        if wave == 8:
            i8.draw(540, 380)
        if wave == 9:
            i9.draw(540, 380)

        mouse.draw(x + 20, -1 * y + 580)

    update_canvas()


def update():
    global difficulty, wave, click # 1 easy, 2 normal, 3 hard, 4 hell

    if click is True and 80 < x < 140 and 140 < y < 180:
        btnsound.play()
        difficulty += 1
    if click is True and 80 < x < 140 and 250 < y < 290:
        btnsound.play()
        difficulty -= 1
    if difficulty > 4:
        difficulty = 4
    if difficulty < 1:
        difficulty = 1
    if click is True and 500 < x < 570 and 140 < y < 180:
        btnsound.play()
        wave += 1
    if click is True and 500 < x < 570 and 250 < y < 290:
        btnsound.play()
        wave -= 1
    if wave > 9:
        wave = 9
    if wave < 1:
        wave = 1

    if click is True and 150 < x < 550 and 490 < y < 550:
        btnsound.play()
        game_framework.change_state(main_state)
        character.realXLocation = 0
        character.leftEndMove = 0
        character.stopSide = 1
        character.velocity = 0
        character.x = 0
        character.jumpHeight = 0
    click = False


def pause():
    pass


def resume():
    pass
