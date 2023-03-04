# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cR34C0wIMUbmKWG1GviaVsES_iegoU3R
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/BE project

"""# Importing lib"""

import numpy as np 
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import tensorflow as tf
import imageio

from imageio import imread
from skimage.transform import resize
from keras.applications.mobilenet_v2 import preprocess_input

import os
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.python.framework import ops
from tensorflow.python.framework import dtypes

"""# Preparing DataFrame"""

#File containing the path to images and the labels [path/to/images label]
filename = './5dbht54kw7-1/image_label_.txt'

#Lists where to store the paths and labels
filenames = []
labels = []

#Reading file and extracting paths and labels
with open(filename, 'r') as File:
    infoFile = File.readlines() #Reading all the lines from File
    for line in infoFile: #Reading line-by-line
        words = line.split() #Splitting lines in words using space character as separator
        #print(words[0]) #, words[1])
        filenames.append(words[0])
        labels.append(words[1])

filenames[0] = '5dbht54kw7-1/dog210422_04_02_33/pic0.jpg'

print(filenames)

print(labels)

images = pd.Series(filenames, name="Images").astype(str)
labels = pd.Series(labels, name="Labels").astype(str)

data = pd.concat([images, labels], axis = 1)
data = data.sample(frac = 1, random_state = 42).reset_index(drop = True)
data.head()

# small sample of the data
fig, axes = plt.subplots(2, 2, figsize = (8, 8))
for i, ax in enumerate(axes.flat):
  ax.imshow(imageio.imread('/content/drive/MyDrive/BE project/'+data.Images[i]))
  ax.set_title(data.Labels[i])
  ax.set_xticks([])
  ax.set_yticks([])
plt.tight_layout()
plt.show()

imageio.imread('/content/drive/MyDrive/BE project/'+data.Images[0]).shape

"""# Data Augumentation"""

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import mobilenet_v2

train_generator_mobile_net = ImageDataGenerator(
    preprocessing_function = mobilenet_v2.preprocess_input,
    validation_split = 0.1
)

test_generator_mobile_net = ImageDataGenerator(
    preprocessing_function = mobilenet_v2.preprocess_input
)

"""# Spliting data Into Train, test"""

from sklearn.model_selection import train_test_split
training_set, validation_set = train_test_split(data, random_state = 0, test_size = 0.2)

print(type(training_set), type(validation_set))

from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_dataGen = ImageDataGenerator(rescale = 1./255,
                                      shear_range = 0.2,
                                      zoom_range = 0.2,
                                      horizontal_flip = True)

validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_dataGen.flow_from_dataframe(dataframe = training_set,x_col="Images", y_col="Labels", class_mode="categorical", target_size=(224,224), batch_size=32)

validation_generator = validation_datagen.flow_from_dataframe(dataframe= validation_set, x_col="Images", y_col="Labels", class_mode="categorical", target_size=(224,224), batch_size=32)

train = train_generator_mobile_net.flow_from_dataframe(
    dataframe=train_df,
    x_col="Images",
    y_col="Labels",
    target_size=(224, 224),
    color_mode="rgb",
    class_mode="categorical",
    batch_size=32,
    subset='training',
    rotation_range=32,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    validate_filenames=False
)

validation = train_generator_mobile_net.flow_from_dataframe(
    dataframe=train_df,
    x_col="Images",
    y_col="Labels",
    target_size=(224, 224),
    color_mode="rgb",
    class_mode="categorical",
    batch_size=32,
    shuffle=True,
    seed=42,
    subset='validation',
    rotation_range=32,
    zoom_range=0.2,
    width_shift_range=0.2,
    height_shift_range=0.2,
    sheer_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest",
    validate_filenames=False
)

test = test_generator_mobile_net.flow_from_dataframe(
    dataframe=test_df,
    x_col="Images",
    y_col="Labels",
    target_size=(224, 224),
    color_mode="rgb",
    class_mode="categorical",
    batch_size=32,
    shuffle=False,
    validate_filenames=False
)

"""# Base Model - Mobilenetv2"""

from tensorflow.keras.applications import MobileNetV2

mobilenet_ = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    alpha=1.0,
    weights='imagenet',
    pooling='avg'
)

mobilenet_.trainable = False

"""# Modifying Layers"""

from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy

# building the Predictor layers
x = Dense(256, activation='relu')(mobilenet_.output)
x = Dense(128, activation='relu')(x)
x = Dropout(0.4)(x)

outputs = Dense(4, activation='softmax')(x)

mobilenet = Model(inputs=mobilenet_.inputs, outputs=outputs)

mobilenet.summary()

mobilenet.compile(
    optimizer=Adam(),
    loss=CategoricalCrossentropy(),
    metrics=[CategoricalAccuracy(), ['acc']]
)

CHECKPOINTS = Path("./checkpoints")
CHECKPOINTS.mkdir(exist_ok=True)

"""# Training"""

from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint

# training
results = mobilenet.fit(
    train_generator,
    validation_data = validation_generator,
    batch_size = 32,
    epochs = 20,
    callbacks = [
        EarlyStopping(
            monitor="val_loss",
            patience=4,
            restore_best_weights=True
        ), 
        ReduceLROnPlateau(patience=2),
        ModelCheckpoint(
            str(CHECKPOINTS),
            monitor="val_loss",
            save_best_only=True
        ),
    ]
)

save_model_path = "/content/drive/MyDrive/BE project/saved_model"

import tensorflow

tensorflow.saved_model.save(mobilenet_,save_model_path)

"""# Evaluation"""

pd.DataFrame(results.history)[['categorical_accuracy', 'val_categorical_accuracy']].plot()
plt.title("Accuracy")
plt.show()

pd.DataFrame(results.history)[['loss', 'val_loss']].plot()
plt.title("Loss")
plt.show()

MODEL_PATH = Path("./saved_model")
MODEL_PATH.mkdir(exist_ok=True)
mobilenet.save(str(MODEL_PATH))

results = mobilenet.evaluate(validation_generator)

np.save('model_history.npy', results.history)

predictions = np.argmax(mobilenet.predict(validation_generator), axis=1)

from sklearn.metrics import classification_report
labels = dict((v, k) for k, v in train_generator.class_indices.items())
actual = list(validation_set.Labels)
predictions = [labels[i] for i in predictions]
print(classification_report(actual, predictions))

from sklearn.metrics import confusion_matrix
import seaborn as sns
cf = confusion_matrix(actual, predictions, normalize = "true")
plt.figure(figsize=(10, 8))
sns.heatmap(cf, annot=True, xticklabels = sorted(set(actual)), yticklabels = sorted(set(actual)))
plt.title('Confusion Matrix')
plt.show()



import tensorflow as tf
print(tf.__version__)

new_model = tf.keras.models.load_model('/content/drive/MyDrive/BE project/checkpoints')
    # Check its architecture
    # model.summary()
print(new_model)
print(new_model.summary())

tf.keras.models.save_model(new_model, 'new_model.h5')
loaded_model_from_h5 = tf.keras.models.load_model('new_model.h5')

print(loaded_model_from_h5.summary())

