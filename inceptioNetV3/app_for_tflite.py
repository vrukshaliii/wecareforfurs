import numpy as np
import tensorflow as tf
import cv2
import pathlib
import matplotlib.pyplot as plt


# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="inceptionetv3/model/model_fit_tf10-0.99.tflite")

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.allocate_tensors()

#--- input details
#print(input_details)
#--- output details
#print(output_details)

input_image = "E:/Ishika/BE/project/inceptionetv3/data/val/bacterial/bacterial (20).jpg"
classes=['bacterial', 'fungal', 'healthy', 'hypersensitivity']

def load_image(filename):
    img = cv2.imread(filename)
    new_img = cv2.resize(img, (224, 224))
    new_img = new_img.astype(np.float32)
    new_img = new_img / 255

    return new_img

def predict(image):
    # input_details[0]['index'] = the index which accepts the input
    interpreter.set_tensor(input_details[0]['index'], [image])
    
    # run the inference
    interpreter.invoke()
    
    # output_details[0]['index'] = the index which provides the input
    output_data = interpreter.get_tensor(output_details[0]['index'])
    class_idx = np.argmax(output_data[0])

    #print(class_idx)
    return {classes[class_idx]: output_data[0][class_idx]}

img = load_image(str(input_image))
prediction = predict(img)
print("PREDICTED: class: {}, confidence: {}".format(str(list(prediction.keys())[0]), float(list(prediction.values())[0])))
plt.imshow(img)
plt.show()

