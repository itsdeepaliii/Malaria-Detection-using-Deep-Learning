# Malaria Detection using Deep Learning

This project implements an AI-powered malaria detection system that classifies blood smear microscopy images as Parasitized (infected) or Uninfected (healthy) using a Deep Learning model.

The model is trained using Transfer Learning with MobileNetV2 and deployed using a Flask web application so users can upload microscopy images and receive predictions.
## 📌 Project Overview

Malaria is a life-threatening disease caused by parasites transmitted through mosquito bites. Early and accurate diagnosis is critical for effective treatment.

Traditional diagnosis requires manual examination of blood smear slides under a microscope, which can be time-consuming and dependent on expert knowledge.

This project aims to assist medical diagnostics by building a Deep Learning based automated malaria detection system.
## 📊 Dataset

The dataset used for this project is the Malaria Cell Images Dataset.

Dataset Source:
https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria
Dataset information:
Total Images: 27,558
Classes: 2
Parasitized
Uninfected
Image Type: Thin blood smear microscopy images
Color Space: RGB

## Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- Flask
- HTML/CSS

## Model

The model is trained using MobileNetV2 on the Malaria Cell Images dataset.

Classes:
- Parasitized
- Uninfected

## Features

- Upload microscopy image
- Detect malaria infection
- Display prediction and confidence score
- Simple web interface using Flask

## How to Run

Clone the repository:

git clone <repo_link>

Install dependencies:

pip install -r requirements.txt

Run the app:

python app.py

Open browser:

http://127.0.0.1:5000

## Model Performance

### Accuracy Graph

![Accuracy Graph](assets/accuracy_graph.png)

### Loss Graph

![Loss Graph](assets/loss_graph.png)

### Confusion Matrix

![Confusion Matrix](assets/confusion_matrix.png)

### ROC Curve

![ROC Curve](assets/roc_curve.png)

## Web Application Interface

### Upload Page

![Upload Page](assets/upload.png)

### Prediction Result

![Prediction Result](assets/prediction_result.png)

## Model Training Notebook

The deep learning model was trained using Google Colab.

You can view the full training notebook here:

[Open Training Notebook](notebooks/malaria.ipynb)

