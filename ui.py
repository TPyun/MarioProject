from pico2d import *
import character
import game_framework
import start_state
import title_state
import main_state

setTime = 250
readyTime = 0
leftTime = setTime
i = 1


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
        global readyTime # mainstate 진입 후 시간 세기위한 장치
        global i
        # if character.x != 0 or character.jumpHeight != 0:
        if character.Mario and i == 1:
            readyTime = get_time()
            i = 0
        leftTime = str(setTime - int(get_time()) + readyTime)

    def draw(self):
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


class Life:
    def __init__(self):
        self.ima1 = load_image('images/life/l1.png')
        self.ima2 = load_image('images/life/l2.png')
        self.ima3 = load_image('images/life/l3.png')
        self.ima4 = load_image('images/life/l4.png')
        self.ima5 = load_image('images/life/l5.png')

    def update(self):
        pass

    def draw(self):
        if character.leftLife == 1:
            self.ima1.draw(80, 560)
        if character.leftLife == 2:
            self.ima2.draw(80, 560)
        if character.leftLife == 3:
            self.ima3.draw(80, 560)
        if character.leftLife == 4:
            self.ima4.draw(80, 560)
        if character.leftLife == 5:
            self.ima5.draw(80, 560)
