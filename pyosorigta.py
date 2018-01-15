# test_model.py

import numpy as np
import cv2
import time
import os

from grabscreen import grab_screen
from directkeys import PressKey, ReleaseKey, DirectionKey as dk
from alexnet import alexnet
from getkeys import key_check

cwd = os.getcwd()
for file_name in os.listdir(cwd):
    if file_name.startswith('Osori-SelfDrivingWithGTA5'):
        MODEL_NAME = file_name.split('.model')[0] + '.model'
        print('{} is selected'.format(MODEL_NAME))
        break

t_time = 0.1


def straight():
    PressKey(dk.W)
    ReleaseKey(dk.A)
    ReleaseKey(dk.D)


def left():
    ReleaseKey(dk.D)
    PressKey(dk.W)
    PressKey(dk.A)
    time.sleep(t_time)
    ReleaseKey(dk.A)


def right():
    ReleaseKey(dk.A)
    PressKey(dk.W)
    PressKey(dk.D)
    time.sleep(t_time)
    ReleaseKey(dk.D)

WIDTH = 160
HEIGHT = 120
LEARNING_RATE = 0.001

model = alexnet(WIDTH, HEIGHT, LEARNING_RATE)
model.load(MODEL_NAME)


def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)
    paused = False
    while True:

        if not paused:
            # 800x600 windowed mode
            # screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
            screen = grab_screen(region=(0, 40, 800, 640))
            print('loop took {} seconds'.format(time.time() - last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            input_screen = cv2.resize(screen, (160, 120))

            cv2.imshow('screen', screen)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

            prediction = model.predict([input_screen.reshape(160, 120, 1)])[0]
            print(prediction)

            dir = np.argmax(prediction)
            if prediction[1] > 0.2:
                straight()
            elif prediction[0] > prediction[2]:
                left()
            else:
                right()

        keys = key_check()
        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
            else:
                paused = True
                ReleaseKey(dk.A)
                ReleaseKey(dk.W)
                ReleaseKey(dk.D)

            time.sleep(1)


main()
