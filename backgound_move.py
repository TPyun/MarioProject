from pico2d import *


def handle_events():
    global stopSide
    global running
    global dir
    global jump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            dir = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            dir = -1

        elif event.type == SDL_KEYUP and event.key == SDLK_d:
            if dir == -1:   #a,d 동시입력하다가 손떼면 가던 방향 계속 갈수 있게끔
                dir = -1
            else:
                dir = 0
                stopSide = 1
        elif event.type == SDL_KEYUP and event.key == SDLK_a:
            if dir == 1:
                dir = 1
            else:
                dir = 0
                stopSide = -1

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            jump = True
    pass


open_canvas()
ground = load_image('images/groundLong.png')
characterRight = load_image('images/marioAniRight1.png')
characterLeft = load_image('images/marioAniLeft1.png')
characterStandLeft = load_image('images/standL.png')
characterStandRight = load_image('images/standR.png')
background = load_image('images/background.png')

running = True
x = 0
jumpHeight = 1
highestJumpHeight = 90
jump = False
frame = 0 #캐릭터 애니사진 파일 움직이기 위한 용도
dir = 0 #-1이면 왼쪽으로 +1이면 오른쪽 방향으로 움직인다.
characterAniSpeed = 1 #캐릭터 애니 사진 넘어가는 속도 변수
stopSide = 1


while running:
    clear_canvas()
    background.draw(x + 930, 420) #백그라운드가 움직이게 하기 위해서 x좌표 입력
    ground.draw(x + 930, 30)
    if dir == 1:
        characterRight.clip_draw(frame * 60, 0, 56, 70, 300, 100 + jumpHeight) #숫자 5번째에 300으로 한 이유는 마리오의 위치 고정
    elif dir == -1:
        characterLeft.clip_draw(frame * 60, 0, 56, 70, 300, 100 + jumpHeight)

    elif stopSide == 1 and dir == 0:
        characterStandRight.draw(300, 100 + jumpHeight)
    elif stopSide == -1 and dir == 0:
        characterStandLeft.draw(300, 100 + jumpHeight)

    if jump:
        jumpHeight += 6
    if jumpHeight > highestJumpHeight:
        jump = False
    if jump == False and jumpHeight > 0:
        jumpHeight -= 6


    update_canvas()
    handle_events()
    if characterAniSpeed % 2 == 0: #캐릭터 애니사진 넘어가는 속도 조절 장치
        frame = (frame + 1) % 21 #마리오 사진 넘기기
    characterAniSpeed += 1
    x += dir * -3 #속도 올리기

    delay(0.01)

close_canvas()