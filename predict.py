import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model


model = load_model("malaria_model_tf", compile=False)
IMG_SIZE = 224

classes = ["Parasitized","Uninfected"]

def predict_image(img_path):

    img = cv2.imread(img_path)

    img = cv2.resize(img,(IMG_SIZE,IMG_SIZE))

    img = img/255.0

    img = np.reshape(img, (1, IMG_SIZE, IMG_SIZE, 3)).astype(np.float32)

    prediction = model.signatures["serving_default"](tf.constant(img))
    prediction = list(prediction.values())[0].numpy()
    index = np.argmax(prediction)
    confidence = float(np.max(prediction)) * 100

    return classes[index], round(confidence,2)