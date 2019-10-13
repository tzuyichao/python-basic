from keras import layers
from keras import models

def build_model():
    model = models.Sequential()
    model.add(layers.Conv3D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))    

