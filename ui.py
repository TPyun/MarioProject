from pico2d import *


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
