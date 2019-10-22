from keras.preprocessing import sequence
from keras.datasets import imdb
from keras import models
from keras import layers
import numpy as np

max_features = 20000
maxlen = 100
batch_size = 32
epochs = 4

print('Loading Data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)
# print(x_train[0])
y_train = np.array(y_train)
y_test = np.array(y_test)

print(y_train.shape)
print(y_train)

model = models.Sequential()
model.add(layers.Embedding(max_features, 128, input_length=maxlen))
model.add(layers.Bidirectional(layers.LSTM(64)))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()

model.compile('adam', 'binary_crossentropy', metrics=['accuracy'])

print('Training...')
history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.2)