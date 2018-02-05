from keras.models import Sequential
from keras.layers import Conv2D, Cropping2D, Dense, Dropout, Flatten, Lambda, MaxPooling2D

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib
import numpy as np

import csv
import os
import math

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


samples = []
        
with open('data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        samples.append([line[0], line[3]])


# I had attempted to do preprocessing, but the model's driving was worse than without preprocessing and augmentation
def generator(samples , batch_size=30):    
    while True:
        i = 0
        for offset in range(0, len(samples), batch_size):
            batch_samples = samples[offset:offset+batch_size]
            images = []
            angles = []
            for i in range(len(batch_samples)):
                angle = float(batch_samples[i][1])
                img = mpimg.imread(batch_samples[i][0])
                images.append(img)
                angles.append(angle)
                
            yield np.array(images), np.array(angles)
            
test, train = train_test_split(samples, test_size=0.2)


batch = 10
epochs = 4
model = Sequential()
model.add(Cropping2D(cropping=((60, 25), (0, 0)), input_shape=(160, 320, 3)))
model.add(Lambda(lambda x: (x / 127.5) - 1))
model.add(Conv2D(24, (5, 5), strides=(2, 2), activation='elu'))
model.add(Conv2D(36, (5, 5), strides=(2, 2), activation='elu'))
model.add(Conv2D(48, (5, 5), strides=(2, 2), activation='elu'))
model.add(Conv2D(64, (3, 3), activation='elu'))
model.add(Conv2D(64, (3, 3), activation='elu'))
model.add(Flatten())
model.add(Dense(1162, activation='elu'))
model.add(Dense(100, activation='elu'))
model.add(Dense(50, activation='elu'))
model.add(Dense(10, activation='elu'))
model.add(Dense(1))

model.compile(optimizer='rmsprop', loss='mse')
model.summary()
print('Training the model')

# model.fit(images, labels, batch_size=batch, epochs=epochs)
model.fit_generator(
    generator=generator(train, batch),
    steps_per_epoch=int(len(train)/batch),
    epochs=epochs,
    validation_data=generator(test, batch),
    validation_steps=int(len(test)/batch),
    shuffle=True,
    workers=4
)

print('Saved the model')
model.save('model.h5')
