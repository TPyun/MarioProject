from pico2d import *

import game_framework
import title_state
import main_state
import monsters

PIXEL_PER_METER = (10.0 / 0.15)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 21

running = True
keepJump = True
velocity = 0
charDir = 0
cankeyup = False


def handle_events():
    global stopSide, running, charDir, jump, keepJump, velocity, cankeyup
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            velocity -= RUN_SPEED_PPS
            cankeyup = True
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            velocity += RUN_SPEED_PPS
            cankeyup = True
        if cankeyup:
            if event.type == SDL_KEYUP and event.key == SDLK_d:
                if charDir == -1:  # a,d 동시입력하다가 손떼면 가던 방향 계속 갈수 있게끔
                    velocity += RUN_SPEED_PPS
                else:
                    charDir = 0
                    stopSide = 1
                    velocity += RUN_SPEED_PPS
            elif event.type == SDL_KEYUP and event.key == SDLK_a:
                if charDir == 1:
                    velocity -= RUN_SPEED_PPS
                else:
                    charDir = 0
                    stopSide = -1
                    velocity -= RUN_SPEED_PPS
        if event.type == SDL_KEYDOWN and event.key == SDLK_w:
            jump = True
        elif event.type == SDL_KEYUP and event.key == SDLK_w:
            keepJump = False
    pass


realXLocation = 0
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
leftLife = 5
damaged = None
r = 0
onbrick = 0
fall = False

class Mario:
    def __init__(self):
        self.imageStandL = load_image('images/standL.png')
        self.imageStandR = load_image('images/standR.png')
        self.imageL = load_image('images/marioAniLeft1.png')
        self.imageR = load_image('images/marioAniRight1.png')
        self.imageStandR.draw(300, groundHeight + jumpHeight)
        self.frame = 0
        self.i = 0

    def update(self):
        global jump, jumpHeight, i, moreHigher, keepJump, realXLocation, charDir, leftLife, damaged, r, onbrick, fall
        realXLocation = x * -1
        charDir = clamp(-1, -1 * velocity, 1)  # -1이면 왼쪽으로 +1이면 오른쪽 방향으로 움직인다.

        if jump:
            fall = False
            t = i / 50
            if onbrick == 0:
                jumpHeight = (-4 * t ** 2 + 4 * t) * (highestJumpHeight + moreHigher) + (2 * t ** 2 - t) * 0  # 마지막 groundHeight 만약 사물이 있을 경우에는 이걸로 안됨
            else:
                jumpHeight = (-4 * t ** 2 + 4 * t) * (highestJumpHeight + moreHigher) + (2 * t ** 2 - t) * -1 * (onbrick)  # 마지막 groundHeight 만약 사물이 있을 경우에는 이걸로 안됨
            i += 0.0021629 * RUN_SPEED_PPS
            i -= 0.001 * moreHigher
            if keepJump is True:
                moreHigher += 0.010811 * RUN_SPEED_PPS
                # 더 점프할 시 하강속도 문제로 i 강제로 줄임
            else:
                pass

        if fall:
            print('fall')
            t = i / 50
            jumpHeight = (2 * t ** 2 - t) * -1 * onbrick
            i += 0.0021629 * RUN_SPEED_PPS
            if i > 50:
                fall = False
                onbrick = 0
                jumpHeight = 0
                i = 0

        if i >= 49:
            jump = False
            fall = False
            onbrick = 0
            jumpHeight = 0
            i = 0
            moreHigher = 0
        if jump is False:
            keepJump = True


        if damaged:
            r += 1
        else:
            self.imageL.opacify(1)
            self.imageR.opacify(1)
            self.imageStandR.opacify(1)
            self.imageStandL.opacify(1)
            r = 0

        if damaged is True and r % 20 < 10:
            self.imageL.opacify(0)
            self.imageR.opacify(0)
            self.imageStandR.opacify(0)
            self.imageStandL.opacify(0)
        elif damaged is True and r % 20 > 10:
            self.imageL.opacify(1)
            self.imageR.opacify(1)
            self.imageStandR.opacify(1)
            self.imageStandL.opacify(1)
        print(jump, fall, i, jumpHeight, onbrick, moreHigher)

    def draw(self):
        global frame, characterAniSpeed, x, leftEndMove, leftEnd, velocity, charDir, onbrick

        if charDir == 1:
            self.imageR.clip_draw(int(frame) * 60, 0, 56, 70, 300 + leftEndMove, 100 + jumpHeight + onbrick, 56, 70)  # 숫자 5번째에 300으로 한 이유는 마리오의 위치 고정

        elif charDir == -1:
            self.imageL.clip_draw(int(frame) * 60, 0, 56, 70, 300 + leftEndMove, 100 + jumpHeight + onbrick, 56, 70)

        elif stopSide == 1 and charDir == 0:
            self.imageStandR.draw(300 + leftEndMove, 100 + jumpHeight + onbrick, 56, 70)

        elif stopSide == -1 and charDir == 0:
            self.imageStandL.draw(300 + leftEndMove, 100 + jumpHeight + onbrick, 56, 70)

        frame = (frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION # 마리오 사진 넘기기

        # if monsters.Monster().stuckwith:
        #     frame = (frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 40
        # print(monsters.Monster().stuckwith)
        x += velocity * game_framework.frame_time

        if x < 0:  # 왼쪽 끝으로 가면 배경이 멈추고 캐릭터가 직접 움직인다
            leftEnd = False
        if x >= 0:
            leftEnd = True
            leftEndMove = x * -1
            if leftEndMove < -280:
                leftEndMove += 3
                x -= 3
        draw_rectangle(*self.get_sidepos())
        draw_rectangle(*self.get_marioheadpos())
        draw_rectangle(*self.get_mariofeetpos())

    def get_sidepos(self):
        return 300 - 15 + leftEndMove, 100 + jumpHeight + onbrick - 25, 300 + 15 + leftEndMove, 100 + jumpHeight + onbrick + 25

    def get_marioheadpos(self):
        return 300 - 10 + leftEndMove, 100 + jumpHeight + onbrick + 25, 300 + 10 + leftEndMove, 100 + jumpHeight + onbrick + 30

    def get_mariofeetpos(self):
        return 300 - 10 + leftEndMove, 100 + jumpHeight + onbrick - 35, 300 + 10 + leftEndMove, 100 + jumpHeight + onbrick - 25

