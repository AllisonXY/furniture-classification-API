from PIL import Image
from io import BytesIO
import tensorflow as tf
from tensorflow import keras
import numpy as np
import os

# dictionary that maps the class labels to the index from ImageDataGenerator
label_dict={0: 'Bed', 1: 'Chair', 2: 'Sofa'}

# load pre-trained custom CNN model
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'cnn_model')
    model = keras.models.load_model(model_path)
    return model

_model = load_model()

# read image from user input
def read_image(image):
    image = Image.open(BytesIO(image))
    return image

# preprocess image through scaling and resizing
def preprocess(image: Image.Image):
    image = np.array(image)
    processed_image = image / 255.0
    processed_image = tf.image.resize(processed_image, (64, 64))
    processed_image = np.expand_dims(processed_image, axis=0)
    return processed_image

# predict image category using loaded model
def predict(image: np.ndarray):
    predictions = _model.predict(image)  # predicted probabilities over 3 categorries
    label = np.argmax(predictions)       # choose the category with max prob
    label = label_dict[label]            # get the category name
    return label
