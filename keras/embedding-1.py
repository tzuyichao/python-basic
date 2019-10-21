from keras import models
from keras import layers
import numpy as np

model = models.Sequential()
model.add(layers.Embedding(1000, 64, input_length=10))

input_array = np.random.randint(1000, size=(32, 10))

model.summary()
model.compile('rmsprop', 'mse')
print(input_array.shape)
print(input_array)
output_array = model.predict(input_array)
print(output_array.shape)
# print(output_array)