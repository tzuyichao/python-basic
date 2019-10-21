from keras import models
from keras import layers

def build_dropout_model():
    model = models.Sequential()
    model.add(layers.Dense(16, activation='relu', input_shape=(10000, )))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(16, activation='relu', input_shape=(10000, )))
    model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    return model


    