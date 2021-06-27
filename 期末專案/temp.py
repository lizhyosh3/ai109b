import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.datasets import mnist
from tensorflow.python.keras.utils import np_utils
from matplotlib import pyplot as plt
# def load_data():
#    (x_train, y_train), (x_test, y_test) = mnist.load_data()

#    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
#    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
#    x_train = x_train.astype('float32')
#    x_test = x_test.astype('float32')

#    y_train = np_utils.to_categorical(y_train, 10)
#    y_test = np_utils.to_categorical(y_test, 10)

#   return (x_train, y_train), (x_test, y_test)

#(x_train, y_train), (x_test, y_test) = load_data()
x_train = np.zeros([1, 28, 28, 1])
y_train = np.zeros([1, 6])
x_test = np.zeros([1, 28, 28, 1])
y_test = np.zeros([1, 6])
model = Sequential()

model.add(Conv2D(filters=3, kernel_size=(3, 3), activation='relu',
                 input_shape=(28, 28, 1), data_format="channels_last"))
model.add(Conv2D(filters=10, kernel_size=(3, 3), activation='relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=20, activation='relu'))
model.add(Dense(units=20, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='adagrad', metrics=['accuracy'])
train_history = model.fit(x=x_train, y=y_train, epochs=5, batch_size=200)
result = model.evaluate(x_test, y_test)
print("\nAccuracy of testing data = ", result)
# deep learning

for i in range(1, 1800):
    image = cv2.imread('.\\image_set\\buildings2191\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([0], 6), axis=0)

for i in range(1800, 2191):
    image = cv2.imread('.\\image_set\\buildings2191\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([0], 6), axis=0)
for i in range(1, 1800):
    image = cv2.imread('.\\image_set\\forest2271\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([1], 6), axis=0)
for i in range(1800, 2271):
    image = cv2.imread('.\\image_set\\forest2271\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([0], 6), axis=0)
for i in range(1, 1800):
    image = cv2.imread('.\\image_set\\glacier2404\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([1], 6), axis=0)
for i in range(1800, 2404):
    image = cv2.imread('.\\image_set\\glacier2404\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([0], 6), axis=0)
for i in range(1, 1800):
    image = cv2.imread('.\\image_set\\mountain2512\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([1], 6), axis=0)
for i in range(1800, 2512):
    image = cv2.imread('.\\image_set\\mountain2512\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([0], 6), axis=0)
for i in range(1, 1800):
    image = cv2.imread('.\\image_set\\sea2274\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([1], 6), axis=0)
for i in range(1800, 2274):
    image = cv2.imread('.\\image_set\\sea2274\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([0], 6), axis=0)
for i in range(1, 1800):
    image = cv2.imread('.\\image_set\\street2382\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_train = np.append(x_train, image, axis=0)
    y_train = np.append(y_train, np_utils.to_categorical([1], 6), axis=0)
for i in range(1800, 2382):
    image = cv2.imread('.\\image_set\\street2382\\'+str(i)+'.jpg')
    image = image.reshape(1, 28, 28, 1)
    x_test = np.append(x_test, image, axis=0)
    y_test = np.append(y_test, np_utils.to_categorical([0], 6), axis=0)
model = Sequential()
