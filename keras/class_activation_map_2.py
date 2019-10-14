from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions
import numpy as np

model = VGG16(weights='imagenet')
image_path = '.\\creative_commons_elephant.jpg'
img = image.load_img(image_path, target_size=(224, 224))
print(type(img))
print(img.size)
x = image.img_to_array(img)
print(x.shape)
x =  np.expand_dims(x, axis=0)
print(x.shape)
x = preprocess_input(x)

preds = model.predict(x)
print('預測結果', decode_predictions(preds, top=3)[0])