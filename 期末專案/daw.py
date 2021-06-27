#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.datasets import mnist
from tensorflow.python.keras.utils import np_utils
from matplotlib import pyplot as plt

x_train = np.zeros([1, 150, 150, 3])
y_train = np.zeros([1, 6])
x_test = np.zeros([1, 150, 150, 3])
y_test = np.zeros([1, 6])
model = Sequential()

for i in range(1, 100):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\buildings2191\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([0], 6), axis=0)

for i in range(100, 150):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\buildings2191\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([0], 6), axis=0)
for i in range(1, 100):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\forest2271\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([1], 6), axis=0)
for i in range(100, 150):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\forest2271\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([1], 6), axis=0)
for i in range(1, 100):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\glacier2404\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([2], 6), axis=0)
for i in range(100, 150):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\glacier2404\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([2], 6), axis=0)
for i in range(1, 100):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\mountain2512\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([3], 6), axis=0)
for i in range(100, 150):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\mountain2512\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([3], 6), axis=0)
for i in range(1, 100):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\sea2274\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([4], 6), axis=0)
for i in range(100, 150):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\sea2274\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([4], 6), axis=0)
for i in range(1, 100):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\street2382\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([5], 6), axis=0)
for i in range(100, 150):
    image = cv2.imread(
        'C:\\Users\\wwww0\Desktop\\image_set\\street2382\\'+str(i)+'.jpg')
    image = image.reshape(1, 150, 150, 3)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([5], 6), axis=0)
model = Sequential()

model.add(Conv2D(filters=3, kernel_size=(3, 3), activation='relu',
                 input_shape=(150, 150, 3), data_format="channels_last"))
model.add(Conv2D(filters=10, kernel_size=(3, 3), activation='relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=20, activation='relu'))
model.add(Dense(units=20, activation='relu'))
model.add(Dense(units=6, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='adagrad', metrics=['accuracy'])
train_history = model.fit(x=x_train, y=y_train, epochs=5, batch_size=200)
result = model.evaluate(x_test, y_test)
print("\nAccuracy of testing data = ", result)


# In[ ]:
