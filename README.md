# 🐾We care for Furs!

![dogs-collage](https://user-images.githubusercontent.com/65615660/224222549-23bea03f-27bb-4de7-be38-7fe995fa9c47.jpg)

Dogs were found to be the most popular pets in India, comprising 68 percent of pets owned, according to a January 2022 survey conducted by Rakuten Insight. Research has repeatedly demonstrated the significant role that pets play in an individual's life. Studies have indicated that pet ownership can lead to increased physical activity, lower serum cholesterol and triglyceride levels, and a reduced likelihood of cardiovascular events. Furthermore, owning a pet has been linked to lower levels of depression and mental stress, and greater self-esteem. While dogs can provide emotional and mental health benefits, they are also susceptible to various diseases and infections, which can pose a risk to certain groups such as young children, pregnant women, the elderly, and immunocompromised individuals. Direct or indirect contact with dogs has been identified as a risk factor for numerous zoonotic infections caused by bacteria, fungi, parasites, and viruses.

The objective of this project was to predict type of skin disease , a zoonotic disease, by utilizing diverse machine-learning models and evaluating their performance based on various parameters. The ultimate goal was to detect the type of disease an offer recommendations for precautions that should be taken to prevent the spread of the disease.

# Project Structure:

The project consists of the following components:

- A dataset of dog skin disease images
- Jupyter notebooks for training and evaluating models
- Python scripts for preprocessing data, training models, and generating predictions
- Django apps to create webapp for the project
- Dockerfile for building a Docker container
- Readme file for project documentation

# Requirements:

- python==3.9
- Django
- tensorflow==2.11.0
- keras==2.11.0
- opencv-python==4.7.0.72
- numpy==1.21.5
- django-compressor

# Dataset:

The dataset consists of images of various dog skin diseases available on internet.

# Preprocessing:

The images will be resized to a standard size of 224x224 pixels and normalized to have pixel values between 0 and 1. The data will also be split into training, validation, and testing sets.

# Model Training:

The deep learning models is built using TensorFlow and Keras libraries. The following models will be trained and evaluated:

- InceptionV3
- MobileNetV2

The models will be trained on the training data, and their performance will be evaluated on the validation data. The best performing model will be selected for deployment.

# Model Deployment:

The selected model will be deployed using a Docker container. The Dockerfile will include all the necessary dependencies to run the model, including the TensorFlow and Keras libraries.

# Steps to run:

**Docker image:** [vrukshali26/wecareforfurs:v1](https://hub.docker.com/repository/docker/vrukshali26/wecareforfurs/general)

**Run the container:** 
```
docker run -dit -p 8000:8000  --name=<name_of_container>  -v  <location_store_images>:/home/app/webapp/media/  vrukshali26/wecareforfurs:v1
```

https://user-images.githubusercontent.com/65615660/224222387-2609f137-6516-4c8c-8ea0-d047c14bd23c.mp4

# Conclusion:

This project aims to classify various types of dog skin diseases using deep learning models with images.
