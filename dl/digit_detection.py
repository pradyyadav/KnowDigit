import numpy as np
import cv2
import tensorflow as tf
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def digit_detection(image_path):
    pred = tf.keras.models.load_model(str(BASE_DIR)+'/final_model')
    image = cv2.imread(image_path,0)
    image = cv2.resize(image,(28,28))
    image = np.array(image)
    image = image.reshape(1,28,28,1)
    image = (image - image.max())/(image.max() - image.min())
    return np.argmax(pred.predict(image))
    #return image.shape


# path = f'media.png'
# img = cv2.imread(path,0)
# digit_detection(img)

    # cv2.imshow('image',img)
    # cv2.waitKey(0)