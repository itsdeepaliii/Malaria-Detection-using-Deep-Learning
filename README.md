# Malaria Detection using Deep Learning

This project detects malaria infection from blood smear microscopy images using a deep learning model.

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

notebooks/malaria.ipynb
