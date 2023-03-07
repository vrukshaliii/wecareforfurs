import tensorflow as tf
from keras.models import load_model
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import keras.utils as image
from keras.utils import load_img

new_model = tf.keras.models.load_model('E:/Ishika/BE/project/inceptionetv3/model/model_finetuned1_10-0.98.h5')
input = "E:/Ishika/BE/project/Data_orginal_divided/bacterial/bacterial (1).jpg"
def load_image(filename):
    IMAGE_SIZE = IMAGE_SIZE = [224, 224]
    img = cv2.imread(filename)
    img = cv2.resize(img, (IMAGE_SIZE[0], IMAGE_SIZE[1]) )
    img = img /255
    
    return img

classes=['bacterial', 'fungal', 'healthy', 'hypersensitivity']

def predict(image):
    probabilities = new_model.predict(np.asarray([image]))[0]
    class_idx = np.argmax(probabilities)
    
    return {classes[class_idx]: probabilities[class_idx]}

img = load_image(str(input))
prediction = predict(img)
print("ACTUAL CLASS: %s, PREDICTED: class: %s, confidence: %f" % (os.path.basename(input), list(prediction.keys())[0], list(prediction.values())[0]))
plt.imshow(img)
plt.show()