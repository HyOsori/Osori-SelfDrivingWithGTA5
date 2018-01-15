import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array

    [A,W,D] boolean values.
    '''
    output = [0, 0, 0]

    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output


datafile_name = 'training_data-'
datafile_no = 1
extension = '.npy'

training_data = []

cwd = os.getcwd()

for file_name in os.listdir(cwd):
    if file_name == (datafile_name + str(datafile_no) + extension):
        print('{} exists, loading previous data!', file_name)
        datafile_no += 1
        training_data.append(np.load(file_name))

if __name__ == "__main__":

    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    paused = False
    while True:

        if not paused:
            # 800x600 windowed mode
            screen = grab_screen(region=(0, 40, 800, 640))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            keys = key_check()
            output = keys_to_output(keys)

            cv2.imshow('screen', screen)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()

            # resize to something a bit more acceptable for a CNN
            input_screen = cv2.resize(screen, (160, 120))
            training_data.append([input_screen, output])

            if len(training_data) % 1000 == 0:
                print(len(training_data))
                np.save(datafile_name + str(datafile_no), training_data)
                datafile_no += 1

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('Resume!')
                time.sleep(1)
            else:
                paused = True
                print('Paused!')
                time.sleep(1)
