from keras.datasets import imdb
from keras import preprocessing
from keras.models import Sequential
from keras.layers import Flatten, Dense, Embedding

max_features = 10000
maxlen = 20

def make_model(max_len):
    model = Sequential()
    model.add(Embedding(10000, 8, input_length=max_len))
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
    return model

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
# print(x_train.shape)

x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
# print(x_train.shape)
# print(x_train[0])

x_test = preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen)

model = make_model(maxlen)
model.summary()

history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
print(history.history)
