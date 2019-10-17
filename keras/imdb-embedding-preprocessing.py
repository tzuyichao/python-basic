from keras.datasets import imdb
from keras import preprocessing

max_features = 10000
maxlen = 20

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(x_train.shape)

x_train = preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
print(x_train.shape)
print(x_train[0])

x_test = preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen)
