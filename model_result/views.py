# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import default_storage
# from tensorflow.keras.applications.vgg19 import preprocess_input
# from keras.models import load_model
# from tensorflow.keras import utils
# from tensorflow.keras.preprocessing.image import load_img
# from tensorflow.keras.utils import load_img
# from keras.preprocessing.image import load_img, img_to_array
# from keras.preprocessing import image
# from keras.preprocessing.image import img_to_array, load_img
from django.conf.urls import url
# import numpy as np

# model = load_model('new_model.h5')

def home(request):
    return render(request, 'wecareforfurs/index.html')

def predDisease(request):
    # if request.method == 'POST':
    #     uploaded_file= request.FILES['img']
    #     response = {}
    #     file_name = "pic.jpg"
    #     file_name_2 = default_storage.save(file_name, uploaded_file)
    #     file_url = default_storage.url(file_name_2)
    #     img = load_img(file_url, target_size=(224, 224))

    #     x = img_to_array(img)
    #     x = np.expand_dims(x, axis=0)
    #     x = preprocess_input(x)

    #     y_prob = model.predict(x)
    #     print("y_prob: ",y_prob)
    #     y_class = y_prob.argmax(axis=-1)
    #     # y_class = y_class[0]
    #     label = y_class[0]
    #     y_confidence = int(y_prob[0][y_class] * 100)
    #     response['name'] = str(label)
    #     return render(request,'wecareforfurs/show.html',response)
    # else:
    return render(request,'wecareforfurs/show.html')



# def predDisease(request):
#     context = {} 
#     # if request.method == 'POST':
#     uploaded_file= request.FILES['img']
#     fs = FileSystemStorage()
#     name = fs.save(uploaded_file.name, uploaded_file)
#     context["url"] = fs.url(name)
#     print(context["url"])
#     testimage = '.'+context["url"] 
#     img = image.load_img(testimage, target_size=(224, 224)) 
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)

#     y_prob = model.predict(x)
#     print("y_prob: ",y_prob)
#     y_class = y_prob.argmax(axis=-1)
#     y_class = y_class[0]
#     y_confidence = int(y_prob[0][y_class] * 100)

        # context['predictedClass'] = labels[np.argmax(pred[0])] 
        # context['probability'] = "{:.2f}".format(round(np.max(pred), 2)*100)
        # context['predictedClass'] = y_prob.argmax(axis=-1).y_class[0]
        # context['probability'] = int(y_prob[0][y_class] * 100)

    # print("predicted label: {} (prob = {})".format(y_class, y_confidence))
    
    # return HttpResponseRedirect(request, 'wecareforfurs/show.html')
    # else:
    #     return HttpResponse("Something went wrong!!")



# https://github.com/zekaouinoureddine/Plants_Identification_DL_Model_Deployment_Django


# https://medium.com/analytics-vidhya/image-classification-with-django-deployment-d18dfc224270