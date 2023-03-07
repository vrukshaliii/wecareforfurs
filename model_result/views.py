from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
import cv2
import numpy as np


new_model = tf.keras.models.load_model('model_finetuned1_10-0.98.h5')


def home(request):
    return render(request, 'wecareforfurs/index.html')


def load_image(filename):
    IMAGE_SIZE = IMAGE_SIZE = [224, 224]
    img = cv2.imread(filename)
    img = cv2.resize(img, (IMAGE_SIZE[0], IMAGE_SIZE[1]) )
    img = img /255
    
    return img


classes=['Bacterial', 'Fungal', 'Healthy', 'Hypersensitivity']


# def predict(image):
#     probabilities = new_model.predict(np.asarray([image]))[0]
#     class_idx = np.argmax(probabilities)
    
#     return f"{classes[class_idx]} with confidence of {round(probabilities[class_idx]*100)}%"


def predDisease(request):
    if request.method == 'POST'  and request.FILES['img']:
        uploaded_file= request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_url = fs.url(filename)

        input = f"./media/{uploaded_file}"
        img = load_image(str(input))
        # prediction = predict(img)

        probabilities = new_model.predict(np.asarray([img]))[0]
        class_idx = np.argmax(probabilities)

        return render(request, 'wecareforfurs/show.html', {
            'prediction': classes[class_idx],
            # 'precautions': json.dumps(cure[class_idx], indent=1),

        })
    return render(request, 'wecareforfurs/show.html')