# wecareforfurs

Dogs were found to be the most popular pets in India, comprising 68 percent of pets owned, according to a January 2022 survey conducted by Rakuten Insight. Research has repeatedly demonstrated the significant role that pets play in an individual's life. Studies have indicated that pet ownership can lead to increased physical activity, lower serum cholesterol and triglyceride levels, and a reduced likelihood of cardiovascular events. Furthermore, owning a pet has been linked to lower levels of depression and mental stress, and greater self-esteem. While dogs can provide emotional and mental health benefits, they are also susceptible to various diseases and infections, which can pose a risk to certain groups such as young children, pregnant women, the elderly, and immunocompromised individuals. Direct or indirect contact with dogs has been identified as a risk factor for numerous zoonotic infections caused by bacteria, fungi, parasites, and viruses.

The objective of this project was to predict type of skin disease , a zoonotic disease, by utilizing diverse machine-learning models and evaluating their performance based on various parameters. The ultimate goal was to detect the type of disease an offer recommendations for precautions that should be taken to prevent the spread of the disease.

# Project Structure:

The project consists of the following components:

A dataset of dog skin disease images

Jupyter notebooks for training and evaluating models

Python scripts for preprocessing data, training models, and generating predictions

Dockerfile for building a Docker container

Jenkinsfile for continuous integration and deployment using Jenkins
Readme file for project documentation

# Requirements:
python 3.9.13

TensorFlow 2.11.0

Keras 2.11.0

Docker

Jenkins

# Dataset:

The dataset consists of images of various dog skin diseases available on internet.

# Preprocessing:

The images will be resized to a standard size of 224x224 pixels and normalized to have pixel values between 0 and 1. The data will also be split into training, validation, and testing sets.

# Model Training:

The deep learning models will be built using TensorFlow and Keras libraries. The following models will be trained and evaluated:

InceptionV3
MobileNetV2

The models will be trained on the training data, and their performance will be evaluated on the validation data. The best performing model will be selected for deployment.

# Model Deployment:

The selected model will be deployed using a Docker container. The Dockerfile will include all the necessary dependencies to run the model, including the TensorFlow and Keras libraries.

# Continuous Integration and Deployment:

Jenkins will be used for continuous integration and deployment. The Jenkinsfile will include the necessary stages to build the Docker container, push the container to a Docker registry, and deploy the container to a server. The server will be configured to listen for requests and generate predictions based on the deployed model.

# Conclusion:

This project aims to classify various types of dog skin diseases using deep learning models with images. DevOps tools will be used for continuous integration and deployment, ensuring that the project can be easily deployed and maintained.
