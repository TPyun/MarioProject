from pico2d import *

running = True
keepJump = True


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
            if charDir == -1: #a,d 동시입력하다가 손떼면 가던 방향 계속 갈수 있게끔
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


class Bgm:
    def __init__(self):
        self.marioWav = load_wav('sound/Mario.wav')
        self.jumpWav = load_wav('sound/jump.wav')
        if running is True:
            self.marioWav.play()

    def play(self):
        if jump is True and jumpHeight == 0:
            self.jumpWav.play()


class TimeUi:
    def __init__(self):
        self.imageClock = load_image('images/number/clock/clock.png')
        self.image0 = load_image('images/number/clock/w0.png')
        self.image1 = load_image('images/number/clock/w1.png')
        self.image2 = load_image('images/number/clock/w2.png')
        self.image3 = load_image('images/number/clock/w3.png')
        self.image4 = load_image('images/number/clock/w4.png')
        self.image5 = load_image('images/number/clock/w5.png')
        self.image6 = load_image('images/number/clock/w6.png')
        self.image7 = load_image('images/number/clock/w7.png')
        self.image8 = load_image('images/number/clock/w8.png')
        self.image9 = load_image('images/number/clock/w9.png')

    def update(self):
        global setTime
        global leftTime
        setTime = 250
        leftTime = str(setTime - int(get_time()))
        self.imageClock.draw(680, 570)

        if leftTime[0] == str(1):
            self.image1.draw(710, 570)
        elif leftTime[0] == str(2):
            self.image2.draw(710, 570)
        elif leftTime[0] == str(3):
            self.image3.draw(710, 570)
        elif leftTime[0] == str(4):
            self.image4.draw(710, 570)
        elif leftTime[0] == str(5):
            self.image5.draw(710, 570)
        elif leftTime[0] == str(6):
            self.image6.draw(710, 570)
        elif leftTime[0] == str(7):
            self.image7.draw(710, 570)
        elif leftTime[0] == str(8):
            self.image8.draw(710, 570)
        elif leftTime[0] == str(9):
            self.image9.draw(710, 570)

        if int(setTime - int(get_time())) < 10:
            pass
        elif leftTime[1] == str(0):
            self.image0.draw(740, 570)
        elif leftTime[1] == str(1):
            self.image1.draw(740, 570)
        elif leftTime[1] == str(2):
            self.image2.draw(740, 570)
        elif leftTime[1] == str(3):
            self.image3.draw(740, 570)
        elif leftTime[1] == str(4):
            self.image4.draw(740, 570)
        elif leftTime[1] == str(5):
            self.image5.draw(740, 570)
        elif leftTime[1] == str(6):
            self.image6.draw(740, 570)
        elif leftTime[1] == str(7):
            self.image7.draw(740, 570)
        elif leftTime[1] == str(8):
            self.image8.draw(740, 570)
        elif leftTime[1] == str(9):
            self.image9.draw(740, 570)

        if int(setTime - int(get_time())) < 100:
            pass
        elif leftTime[2] == str(0):
            self.image0.draw(770, 570)
        elif leftTime[2] == str(1):
            self.image1.draw(770, 570)
        elif leftTime[2] == str(2):
            self.image2.draw(770, 570)
        elif leftTime[2] == str(3):
            self.image3.draw(770, 570)
        elif leftTime[2] == str(4):
            self.image4.draw(770, 570)
        elif leftTime[2] == str(5):
            self.image5.draw(770, 570)
        elif leftTime[2] == str(6):
            self.image6.draw(770, 570)
        elif leftTime[2] == str(7):
            self.image7.draw(770, 570)
        elif leftTime[2] == str(8):
            self.image8.draw(770, 570)
        elif leftTime[2] == str(9):
            self.image9.draw(770, 570)


leftEnd = False


class Background:
    def __init__(self):
        self.image = load_image('images/background.png')
        # self.image = load_image('images/background_0000.gif')

    def update(self):
        if leftEnd is False:
            self.image.draw(x/8 + 1300, 420)  # 백그라운드가 움직이게 하기 위해서 x좌표 입력
        else:
            self.image.draw(1300, 420)


class Ground:
    def __init__(self):
        self.groundLong = load_image('images/groundLong.png')
        self.groundShort = load_image('images/groundShort.png')

    def update(self):
        if leftEnd is False:
            self.groundLong.draw(x + 1500, 30)
            self.groundShort.draw(x + 700, 103)
        else:
            self.groundLong.draw(1500, 30)
            self.groundShort.draw(700, 103)


monsterWalk = False
monsterX = 0
monsterFrame = 0
monsterAniSpeed = 1


class Monster:
    def __init__(self):
        self.imageL = load_image('images/monsterL.png')

    def update(self):
        global monsterWalk
        if x < -300:
            monsterWalk = True

    def draw(self):
        global monsterAniSpeed
        global monsterFrame
        global monsterX
        if monsterWalk:
            self.imageL.clip_draw(monsterFrame * 51, 0, 50, 60, 1200 + monsterX + leftEndMove + x, 95)
            monsterX -= 0.5
        if monsterAniSpeed % 6 == 0:
            monsterFrame = (monsterFrame + 1) % 4
        monsterAniSpeed += 1


x = 0
characterAniSpeed = 1 #캐릭터 애니 사진 넘어가는 속도 변수
frame = 0 #캐릭터 애니사진 파일 움직이기 위한 용도
charDir = 0 #-1이면 왼쪽으로 +1이면 오른쪽 방향으로 움직인다.
stopSide = 1
jump = False
jumpHeight = 0
highestJumpHeight = 100
leftEndMove = 0
i = 0
groundHeight = 100
moreHigher = 0


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
            jumpHeight = (2 * t ** 2 - 3 * t + 1) * 0 + (-4 * t ** 2 + 4 * t) * (highestJumpHeight + moreHigher) + (2 * t ** 2 - t) * 0# 마지막 groundHeight 만약 사물이 있을 경우에는 이걸로 안됨
            i += 1
            if keepJump is True:
                moreHigher += 3
                i -= 0.5 #더 점프할 시 하강속도 문제로 i 강제로 줄임
            else:
                pass
        if i == 49.5 or i == 50:
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
            self.imageR.clip_draw(frame * 60, 0, 56, 70, 300 + leftEndMove, 100 + jumpHeight)  # 숫자 5번째에 300으로 한 이유는 마리오의 위치 고정
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

        if x < 0:  #왼쪽 끝으로 가면 배경이 멈추고 캐릭터가 직접 움직인다
            leftEnd = False
        if x >= 0:
            leftEnd = True
            leftEndMove = x * -1
            if leftEndMove < -280:
                leftEndMove += 3
                x -= 3


open_canvas()

bgm = Bgm()

background = Background()
ground = Ground()
monster = Monster()
mario = Mario()
timeUi = TimeUi()

while running:

    handle_events()
    clear_canvas()

    background.update()
    ground.update()
    monster.update()
    mario.update()
    timeUi.update()

    print(jump, keepJump, i)

    monster.draw()
    mario.draw()
    bgm.play()

    update_canvas()
    delay(0.01)

close_canvas()