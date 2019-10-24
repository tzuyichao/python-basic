import pandas as pd

df = pd.read_csv("./diabetes.csv")

print(df.head())
print(df.shape)

import numpy as np
from keras import models
from keras import layers

dataset = df.values
np.random.shuffle(dataset)

# print(dataset)

x = dataset[:, 0:8]
y = dataset[:, 8]

# print(x)
# print(y)
model = models.Sequential()
model.add(layers.Dense(10, input_shape=(8, ), activation='relu'))
# model.add(layers.Dense(8, activation='relu'))
model.add(layers.Dense(6, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.summary()

# model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# model.fit(x, y, epochs=150, batch_size=10, validation_split=0.2)
model.fit(x, y, epochs=150, batch_size=10)

loss, accuracy = model.evaluate(x, y)
print("精準度 = {:.2f}".format(accuracy))