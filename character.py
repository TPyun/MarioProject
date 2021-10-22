from pico2d import *


running = True
keepJump = True
charDir = 0  # -1이면 왼쪽으로 +1이면 오른쪽 방향으로 움직인다.


def handle_events():
    global stopSide
    global running
    global charDir
    global jump
    global keepJump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            charDir = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            charDir = -1

        elif event.type == SDL_KEYUP and event.key == SDLK_d:
            if charDir == -1:  # a,d 동시입력하다가 손떼면 가던 방향 계속 갈수 있게끔
                charDir = -1
            else:
                charDir = 0
                stopSide = 1
        elif event.type == SDL_KEYUP and event.key == SDLK_a:
            if charDir == 1:
                charDir = 1
            else:
                charDir = 0
                stopSide = -1

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            jump = True
        elif event.type == SDL_KEYUP and event.key == SDLK_w:
            keepJump = False
    pass


x = 0
characterAniSpeed = 1  # 캐릭터 애니 사진 넘어가는 속도 변수
frame = 0  # 캐릭터 애니사진 파일 움직이기 위한 용도
stopSide = 1
jump = False
jumpHeight = 0
highestJumpHeight = 100
leftEndMove = 0
i = 0
groundHeight = 100
moreHigher = 0
leftEnd = False


class Mario:
    def __init__(self):
        self.imageStandL = load_image('images/standL.png')
        self.imageStandR = load_image('images/standR.png')
        self.imageL = load_image('images/marioAniLeft1.png')
        self.imageR = load_image('images/marioAniRight1.png')
        self.imageStandR.draw(300, groundHeight + jumpHeight)
        self.frame = 0

    def update(self):
        global jump
        global jumpHeight
        global i
        global moreHigher
        global keepJump
        if jump:
            t = i / 50
            jumpHeight = (2 * t ** 2 - 3 * t + 1) * 0 + (-4 * t ** 2 + 4 * t) * (highestJumpHeight + moreHigher) + (
            2 * t ** 2 - t) * 0  # 마지막 groundHeight 만약 사물이 있을 경우에는 이걸로 안됨
            i += 0.8
            i -= 0.001 * moreHigher
            if keepJump is True:
                moreHigher += 5
                # i -= 0.3 + 0.001 * moreHigher # 더 점프할 시 하강속도 문제로 i 강제로 줄임
            else:
                pass

        if i >= 50:
            jump = False
            jumpHeight = 0
            i = 0
            moreHigher = 0
        if jump is False:
            keepJump = True

        # if jumpHeight > highestJumpHeight:
        #     jump = False
        # if jump is False and jumpHeight > 0:
        #     jumpHeight -= 5

    def draw(self):
        global frame
        global characterAniSpeed
        global x
        global leftEndMove
        global leftEnd
        if charDir == 1:
            self.imageR.clip_draw(frame * 60, 0, 56, 70, 300 + leftEndMove,
                                  100 + jumpHeight)  # 숫자 5번째에 300으로 한 이유는 마리오의 위치 고정
        elif charDir == -1:
            self.imageL.clip_draw(frame * 60, 0, 56, 70, 300 + leftEndMove, 100 + jumpHeight)

        elif stopSide == 1 and charDir == 0:
            self.imageStandR.draw(300 + leftEndMove, 100 + jumpHeight)
        elif stopSide == -1 and charDir == 0:
            self.imageStandL.draw(300 + leftEndMove, 100 + jumpHeight)

        if characterAniSpeed % 2 == 0:  # 캐릭터 애니사진 넘어가는 속도 조절 장치
            frame = (frame + 1) % 21  # 마리오 사진 넘기기
        characterAniSpeed += 1
        x += charDir * -3  # 속도 올리기

        if x < 0:  # 왼쪽 끝으로 가면 배경이 멈추고 캐릭터가 직접 움직인다
            leftEnd = False
        if x >= 0:
            leftEnd = True
            leftEndMove = x * -1
            if leftEndMove < -280:
                leftEndMove += 3
                x -= 3
