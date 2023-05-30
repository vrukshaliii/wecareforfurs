from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
import cv2
import numpy as np


interpreter = tf.lite.Interpreter(model_path="model_finetuned1_10-0.98.tflite")


input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


interpreter.allocate_tensors()


classes=['Bacterial', 'Fungal', 'Healthy', 'Hypersensitivity']


def load_image(filename):
    img = cv2.imread(filename)
    new_img = cv2.resize(img, (224, 224))
    new_img = new_img.astype(np.float32)
    new_img = new_img / 255

    return new_img    


def predDisease(request):
    if request.method == 'POST'  and request.FILES['img']:
        uploaded_file= request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)

        input = f"./media/{uploaded_file}"
        img = load_image(str(input))

        interpreter.set_tensor(input_details[0]['index'], [img])
    
        # run the inference
        interpreter.invoke()
    
        # output_details[0]['index'] = the index which provides the input
        output_data = interpreter.get_tensor(output_details[0]['index'])
        class_idx = np.argmax(output_data[0])

        return render(request, 'wecareforfurs/show.html', {
            'prediction': classes[class_idx],
            'accuracy': round(output_data[0][class_idx] * 100)
        })
    return render(request, 'wecareforfurs/show.html')
