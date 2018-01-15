import numpy as np
import os
from alexnet import alexnet

datafile_name = 'training_data-'
datafile_no = 1
prefix_name = '-balanced'
extension = '.npy'

cwd = os.getcwd()
for file_name in os.listdir(cwd):
    print('{}-'.format(datafile_no) +  file_name)
    if file_name.startswith(datafile_name) and file_name.find('-balanced.npy') != -1:
        print('{} exists, loading previous data!'.format(file_name))
        datafile_no += 1

WIDTH = 160
HEIGHT = 120
LEARNING_RATE = 0.001
EPOCHS = datafile_no

MODELER = 'sikurity'
MODEL_NAME = 'Osori-SelfDrivingWithGTA5_{}_{}_{}-epochs-300K-data.model'.format(MODELER, LEARNING_RATE, EPOCHS)

model = alexnet(WIDTH, HEIGHT, LEARNING_RATE)
for epoch in range(1, EPOCHS):
    train_data = np.load(datafile_name + str(epoch) + prefix_name + extension)

    train = train_data[:-100]
    test = train_data[-100:]

    X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
    test_y = [i[1] for i in test]

    model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}),
        snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

    model.save(MODEL_NAME)

# tensorboard --logdir=./log
