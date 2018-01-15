import numpy as np
import pandas as pd
import os

from collections import Counter
from random import shuffle

datafile_name = 'training_data-'
datafile_no = 1
prefix_name = '-balanced'
extension = '.npy'

cwd = os.getcwd()

saved_data = []

for file_name in os.listdir(cwd):
    if file_name == (datafile_name + str(datafile_no) + extension):
        print('{} exists, loading previous data!'.format(file_name))

        train_data = np.load(file_name)

        df = pd.DataFrame(train_data)
        print(df.head())
        print(Counter(df[1].apply(str)))

        lefts = []
        rights = []
        forwards = []

        shuffle(train_data)

        for data in train_data:
            img = data[0]
            choice = data[1]

            if choice == [1, 0, 0]:
                lefts.append([img, choice])
            elif choice == [0, 1, 0]:
                forwards.append([img, choice])
            elif choice == [0, 0, 1]:
                rights.append([img, choice])
            else:
                print('no matches')

        forwards = forwards[:len(lefts)][:len(rights)]
        lefts = lefts[:len(forwards)]
        rights = rights[:len(forwards)]

        final_data = forwards + lefts + rights
        shuffle(final_data)

        np.save(datafile_name + str(datafile_no) + prefix_name, final_data)
        datafile_no += 1
