import numpy as np
import cv2
import tensorflow as tf

def digit_detection(image):
    pred = tf.keras.models.load_model('final_model')
    image = image.reshape(1,28,28,1)
    image = (image - image.max())/(image.max() - image.min())
    print("The result is probably : ",np.argmax(pred.predict(image)))


for i in range(4):
    path = f'images\\{i}.png'
    img = cv2.imread(path,0)
    digit_detection(img)
    
    # cv2.imshow('image',img)
    # cv2.waitKey(0)